# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## What this repo is

`gkm-core` defines the **core classes and schemas shared by all GA4GH GKM specifications** (VRS, Cat-VRS, VA-Spec, etc.). It is a schema-definition repo, not an application: the deliverable is JSON Schema (draft 2020-12) generated from a single hand-authored source document.

> **Naming:** GKM = *Genomic Knowledge Models*. This is a recent rebrand from GKS (*Genomic Knowledge Standards*); the module was renamed `gks-core` → `gkm-core`. If you find lingering `gks-core`/`GKS` references, they are almost certainly stale — the one intentional exception is `.github/workflows/tests.yml`, whose `PYTHONPATH` (`/home/runner/work/gks-core/gks-core/`) is derived from the **GitHub repo name** and stays `gks-core` until the repo itself is renamed.

## The source-of-truth → generated-artifacts pipeline

There is exactly one source file, and everything else under `schema/gkm-core/` is generated from it:

- **`schema/gkm-core/gkm-core-source.yaml`** — the *only* file you hand-edit. A custom GA4GH metaschema YAML dialect (not plain JSON Schema).
- **`schema/gkm-core/json/<ClassName>`** — generated split JSON Schema, one file per class, **no file extension**. Committed.
- **`schema/gkm-core/def/<ClassName>.rst`** — generated RST docs. Committed.
- **`schema/gkm-core/build/*`** — generated build tags. **Gitignored** (`schema/*/build/`).

**Never edit the `json/` or `def/` files by hand** — they are overwritten on every build. Change `gkm-core-source.yaml` and regenerate.

Regenerate after editing the source:

```bash
cd schema
make all      # runs source2classes, source2splitjs, y2t, then prune.mk in each schema/*/ subdir
make clean    # removes build/, def/, json/ contents
```

The build tools (`source2classes`, `source2splitjs`, `y2t`) come from the `ga4gh.gkm.metaschema` package — the "metaschema processor" (MSP). It is pinned in `.requirements.txt` to a git ref of `ga4gh/gks-metaschema` (the 0.4.0-line MSP with the abstract-class convention), since that release is not yet on PyPI. Note the package was renamed `ga4gh.gks.metaschema` → `ga4gh.gkm.metaschema` as part of the GKS→GKM rebrand; imports use the `ga4gh.gkm.metaschema` path. `prune.mk` deletes any `json/`/`def/` files whose class no longer exists in the source.

A **pre-commit hook** (`pre-commit-hooks/update-json-def-files.sh`, wired in `.pre-commit-config.yaml`) auto-runs `make all` and stages regenerated `json/`/`def/` files whenever a `*-source.yaml` is staged — so committing a source change keeps generated artifacts in sync automatically. Install it once with `pre-commit install`.

## Source-YAML dialect conventions

`gkm-core-source.yaml` uses GA4GH-specific keys beyond standard JSON Schema. Key idioms (see `Entity`/`Element` for the canonical examples):

- **`inherits: <Class>`** — class inheritance. `Entity` and `Element` are abstract roots; concrete classes (`Coding`, `MappableConcept`, `ConceptMapping`, `ConceptSet`, `Extension`) inherit from one of them.
- **`abstract: true`** — marks a class as abstract (used on `Entity`/`Element`). Abstract classes emit `type: object` and are left "open" (no `additionalProperties`/`unevaluatedProperties` closure); concrete classes are closed (`additionalProperties: false`, or `unevaluatedProperties: false` when composed via inheritance). The processor injects `type: object` automatically, so concrete classes no longer declare it.
- **`properties` / `required`** — on an abstract base class these descend to all subclasses (superclass-first). *(Superseded the old `heritableProperties` / `heritableRequired` keys under the 0.4.0 MSP abstract-class convention.)*
- **`maturity`** (e.g. `trial use`), **`strict: true`**, **`ordered: false`** on arrays — metaschema annotations carried into generated output.
- **`$id`** is a versioned w3id URL: `https://w3id.org/ga4gh/schema/gkm-core/<VERSION>/gkm-core-source.yaml`. The `<VERSION>` token is branch-specific (see Versioning) — preserve it across edits; only change it deliberately as part of a release.

## Testing

```bash
make test                                    # = pytest tests/
pytest tests/test_examples.py                # one test file
pytest tests/test_examples.py::test_examples # one test
```

CI (`.github/workflows/tests.yml`) runs `pytest` on Python 3.12 with `PYTHONPATH` set to the repo root (required so `tests/config.py` is importable). Locally, `make test` handles paths via `pytest tests/`.

How the tests work:

- **`tests/config.py`** builds a `referencing` Registry + `Draft202012Validator` per class. Its `retrieve_rel_ref` resolves any `$ref` of the form `.../ga4gh/schema/<module>/<version>/<localpath>` to the on-disk file `schema/<module>/<localpath>` — **the version segment is intentionally ignored**, and it loads every `schema/*/json/*` file. This is why generated `json/` files must be present and current before tests run.
- **`tests/test_basic.py`** — asserts the source YAML parses through `YamlSchemaProcessor` (metaschema tooling).
- **`tests/test_examples.py`** — validates each `examples/*.yaml` instance against the generated JSON Schema for the class named in **`tests/test_definitions.yaml`** (`schema:` = module dir, `definition:` = class). To add an example test: drop a YAML instance in `examples/`, add a `tests:` entry pointing at it.

Note: the root `Makefile` comment references pytest config "in pyproject.toml", but `pyproject.toml` is gitignored/absent — there is no committed pytest configuration.

## First-time setup

```bash
make devready                      # creates venv/3.12, installs .requirements.txt
source venv/3.12/bin/activate
pre-commit install                 # enables the source→json/def auto-regeneration hook
```

## Versioning and branches

This repo is developed across **multiple long-lived version branches**, not just `main`. The schema version lives in the `$id` of the source and generated files, and differs per branch — e.g. `1.2.0-ballot.2026-07.1` on the ballot branch, `v1` / `1.1.0` on dev branches. When making changes, confirm which branch/version you are basing work on, and keep the `<VERSION>` token in `$id`/`$ref` paths consistent across the source and all generated files. Changing the module or version in `$id` alters the canonical schema identity, which downstream GA4GH schemas (VRS, VA-Spec, Cat-VRS) and w3id.org redirects depend on — treat such changes as coordinated, cross-repo events.

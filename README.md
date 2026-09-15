# gkm-core

Core classes and schemas used by all GKM specifications (ie. VR, Cat-VRS, VA, etc..)

For more info
[GKM Repository Organization](https://docs.google.com/document/d/16SrjqPJ1ct_z8OK6kNcu3KO1ia6LAyVriSbuDLXRAI8/edit)

## Installing for development

Fork the repo at <https://github.com/ga4gh/gkm-core>.

    git clone git@github.com:YOUR_GITHUB_ID/gkm-core.git
    cd gkm-core
    make devready
    source venv/3.12/bin/activate
    pre-commit install

## Contributing to the schema

GKM Core uses the following source document for JSON Schema:

* [gkm-core-source.yaml](./schema/gkm-core/gkm-core-source.yaml)

To create the corresponding def and json files after making changes to any of of the
source documents, from the root directory:

    cd schema
    make all

> _Note: We have a custom pre-commit hook to run these commands after you stage a source
> document_

These commands are powered by the GA4GH metaschema processor
([ga4gh/gks-metaschema](https://github.com/ga4gh/gks-metaschema)), which defines the
`*-source.yaml` dialect and generates the split JSON Schema/RST files from it. See that
repo for details on how source documents are processed.

## Testing

To run the tests:

    (from the root directory of the project)
    make test

The suite validates example instances against the generated schemas. Valid
examples live in [`examples/`](./examples) (registered in
[`tests/test_definitions.yaml`](./tests/test_definitions.yaml)); instances that
must be _rejected_ live in [`examples/invalid/`](./examples/invalid) (registered
in [`tests/test_invalid_definitions.yaml`](./tests/test_invalid_definitions.yaml)).
To cover a new case, drop a YAML instance in the appropriate directory and add a
matching entry to its manifest.

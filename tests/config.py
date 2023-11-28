from pathlib import Path

root_dir = Path(__file__).parent.parent
schema_dir = root_dir / "schema"
test_dir = root_dir / "tests"
examples_dir = root_dir / "examples"
gks_common_source = schema_dir / "gks.common-source.yaml"
gks_common_json = schema_dir / "gks.common.json"

from pathlib import Path

root_dir = Path(__file__).parent.parent
schema_dir = root_dir / "schema" 
test_dir = root_dir / "tests"
examples_dir = root_dir / "examples"
gks_commons_source = schema_dir / "commons" / "commons-source.yaml"
gks_domain_entities_source = schema_dir / "domain-entities" / "domain-entities-source.yaml"
from pathlib import Path

root_dir = Path(__file__).parent.parent
schema_dir = root_dir / "schema" 
test_dir = root_dir / "tests"
examples_dir = root_dir / "examples"
gks_core_im_source = schema_dir / "core-im" / "core-im-source.yaml"
gks_domain_entities_source = schema_dir / "domain-entities" / "domain-entities-source.yaml"
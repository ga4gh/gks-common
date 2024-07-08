from ga4gh.gks.metaschema.tools.source_proc import YamlSchemaProcessor

from config import gks_common_source

# Is the YAML parseable?
p = YamlSchemaProcessor(gks_common_source)


def test_yaml_process():
    assert p.for_js, "processor loads and processes yaml"

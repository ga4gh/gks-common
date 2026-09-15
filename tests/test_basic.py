from ga4gh.gkm.metaschema.tools.source_proc import YamlSchemaProcessor

from config import gkm_core_source

# Is the YAML parseable?
p = YamlSchemaProcessor(gkm_core_source)

def test_yaml_process():
    assert p.for_js, "processor loads and processes yaml"

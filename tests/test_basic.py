import json
import yaml
from ga4gh.gks.metaschema.tools.source_proc import YamlSchemaProcessor

from config import gks_common_json, gks_common_source

# Are the yaml and json parsable and do they match?
p = YamlSchemaProcessor(gks_common_source)
j = json.load(open(gks_common_json))


def test_json_yaml_match():
    assert p.for_js == j, "parsed yaml and json do not match"

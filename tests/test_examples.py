import pytest

from config import test_path, examples_path
import yaml
from config import validator


# def get_schema(schema_file, schema_class, kw="$defs"):
#     return {
#       "$ref": schema_path.as_uri() + f"/{schema_file}.json#/{kw}/{schema_class}"
#     }


# def test_examples():
#     with open(test_path / 'test_definitions.yaml') as def_file:
#         test_spec = yaml.safe_load(def_file)
#     for test in test_spec['tests']:
#         with open(examples_path / test['test_file']) as datafile:
#             data = yaml.safe_load(datafile)
#             print(f"Testing {datafile.name}")
#         schema = get_schema(
#             test['schema'],
#             test['definition'],
#             test.get('kw', '$defs')
#         )
#         try:
#             assert validate(data, schema) is None
#         except AssertionError as e:
#             raise AssertionError(f"AssertionError in {test['test_file']}: {e}")

def test_examples():
    with open(test_path / 'test_definitions.yaml') as def_file:
        test_spec = yaml.safe_load(def_file)
    for test in test_spec['tests']:
        with open(examples_path / test['test_file']) as datafile:
            data = yaml.safe_load(datafile)
        class_validator = validator[test['definition']]
        try:
            assert class_validator.validate(data) is None
        except AssertionError as e:
            raise AssertionError(f"AssertionError in {test['test_file']}: {e}")

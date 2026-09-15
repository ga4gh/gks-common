"""Structural invariants of the generated JSON Schema.

These tests assert the abstract-class convention that the metaschema
processor (MSP) is expected to apply, independent of any example instance:

* abstract classes (e.g. Entity, Element) are left *open* -- no
  ``additionalProperties``/``unevaluatedProperties`` closure.
* concrete object classes are *closed* -- via ``additionalProperties: false``
  (flat classes) or ``unevaluatedProperties: false`` (classes composed with
  ``anyOf``/``allOf``).

They exist to catch a silent regression in the generated output when the MSP
pin is bumped -- the kind of change that no example-instance test would notice.
"""
import yaml

from config import gkm_core_source, js_def


def _abstract_class_names():
    source = yaml.safe_load(gkm_core_source.read_text())
    return {
        name for name, defn in source['$defs'].items()
        if isinstance(defn, dict) and defn.get('abstract') is True
    }


def _is_object_class(schema):
    return schema.get('type') == 'object' or 'properties' in schema


def _is_closed(schema):
    return (
        schema.get('additionalProperties') is False
        or schema.get('unevaluatedProperties') is False
    )


def test_abstract_classes_are_open():
    abstract = _abstract_class_names()
    assert abstract, "expected at least one abstract class in the source"
    for name in abstract:
        schema = js_def[name]
        assert not _is_closed(schema), (
            f"abstract class {name} should be open (no additionalProperties/"
            f"unevaluatedProperties closure)"
        )


def test_concrete_object_classes_are_closed():
    abstract = _abstract_class_names()
    checked = []
    for name, schema in js_def.items():
        if name in abstract or not _is_object_class(schema):
            continue
        checked.append(name)
        assert _is_closed(schema), (
            f"concrete object class {name} should be closed via "
            f"additionalProperties/unevaluatedProperties: false"
        )
    assert checked, "expected at least one concrete object class to check"

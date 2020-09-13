import re

from lxml import etree


def object_to_etree(obj):
    name = None
    if hasattr(obj, "Meta") and hasattr(obj.Meta, "element_name"):
        name = obj.Meta.element_name
    else:
        name = re.sub(r"(?<!^)(?=[A-Z])", "-", obj.__class__.__name__).lower()
    root = etree.Element(name)
    for key, val in obj.__dict__.items():
        if hasattr(val, "to_etree") and callable(getattr(val, "to_etree")):
            el = val.to_etree()
            root.append(el)
        else:
            el = etree.Element(key.replace("_", "-"))
            el.text = str(val)
            root.append(el)
    return root


def object_to_xml_string(obj, encoding="utf-8"):
    root = obj.to_etree()

    return etree.tostring(
        root, encoding=encoding, xml_declaration=True, pretty_print=True
    )

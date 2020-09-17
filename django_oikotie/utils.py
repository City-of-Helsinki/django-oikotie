import re

from lxml import etree

from django_oikotie.enums import Case


def object_to_etree(obj, case=Case.PASCAL):
    name = None
    if hasattr(obj, "Meta") and hasattr(obj.Meta, "element_name"):
        name = obj.Meta.element_name
    elif case == Case.KEBAB:
        name = re.sub(r"(?<!^)(?=[A-Z])", "-", obj.__class__.__name__).lower()
    else:
        name = obj.__class__.__name__

    root = etree.Element(name)
    for key, val in obj.__dict__.items():
        if hasattr(val, "to_etree") and callable(getattr(val, "to_etree")):
            el = val.to_etree(case)
            root.append(el)
        else:
            if case == Case.KEBAB:
                name = key.replace("_", "-")
            else:
                name = key.title().replace("_", "")
            el = etree.Element(name)
            el.text = str(val)
            root.append(el)
    return root


def object_to_xml_string(obj, encoding="utf-8"):
    root = obj.to_etree()

    return etree.tostring(
        root, encoding=encoding, xml_declaration=True, pretty_print=True
    )

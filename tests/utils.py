import logging
import os

from lxml import etree

from django_oikotie.xml_models import XMLModel

_logger = logging.getLogger()


def obj_to_xml_str(obj: XMLModel) -> str:
    root = obj.to_etree()
    xml = etree.tostring(root, encoding="utf-8", pretty_print=True)
    return xml.decode("utf-8")


def get_tests_base_path() -> str:
    path = os.path.dirname(os.path.abspath(__file__))
    _logger.debug("Tests base path: '%s'", path)

    return path

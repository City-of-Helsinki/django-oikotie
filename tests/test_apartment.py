from .factories.apartment import ApartmentFactory
from .utils import obj_to_xml_str


def test__apartment__xml_serialization_does_not_crash():
    obj = ApartmentFactory()
    xml = obj_to_xml_str(obj)
    assert "<Apartment" in xml
    assert "</Apartment>" in xml


# TODO: Test that XML is correct

from datetime import datetime

from django.test import override_settings
import pytest

from django_oikotie.enums import ApartmentType
from django_oikotie.oikotie import create_housing_companies
from django_oikotie.utils import yes_no_bool

from .factories.housing_company import (
    AddressFactory,
    ApartmentFactory,
    BuilderFactory,
    CityPlanPictureFactory,
    ConstructionDetailsFactory,
    CoordinatesFactory,
    HousingCompanyFactory,
    MoreInfoFactory,
    PictureFactory,
    PropertyDevelopmentFactory,
    RealEstateAgentFactory,
    VirtualPresentationFactory,
)
from .utils import obj_to_xml_str


def test__address__minimal_xml_serialization():
    obj = AddressFactory(region=None)
    xml = obj_to_xml_str(obj)
    assert xml == (
        f"<address>\n"
        f"  <street>{obj.street}</street>\n"
        f"  <postal-code>{obj.postal_code}</postal-code>\n"
        f"  <city>{obj.city}</city>\n"
        f"</address>\n"
    )


def test__address__complete_xml_serialization():
    obj = AddressFactory()
    xml = obj_to_xml_str(obj)
    assert xml == (
        f"<address>\n"
        f"  <street>{obj.street}</street>\n"
        f"  <postal-code>{obj.postal_code}</postal-code>\n"
        f"  <city>{obj.city}</city>\n"
        f"  <region>{obj.region}</region>\n"
        f"</address>\n"
    )


def test__apartment__xml_serialization():
    obj = ApartmentFactory(
        types=[
            ApartmentType.BLOCK_OF_FLATS,
            ApartmentType.HOUSE,
        ]
    )
    xml = obj_to_xml_str(obj)
    assert xml == "<apartment>\n  <types>KT, OT</types>\n</apartment>\n"


def test__city_plan_picture__xml_serialization():
    obj = CityPlanPictureFactory(timestamp=datetime(2020, 1, 1, 12, 0, 0))
    xml = obj_to_xml_str(obj)
    assert xml == (
        f'<city-plan-picture timestamp="20200101120000">{obj.image_url}</city-plan-picture>\n'
    )


def test__builder__xml_serialization():
    obj = BuilderFactory()
    xml = obj_to_xml_str(obj)
    assert xml == f"<builder>\n  <logo-url>{obj.logo_url}</logo-url>\n</builder>\n"


@pytest.mark.parametrize(
    "is_complete,is_complete_str",
    (
        (True, "K"),
        (False, "E"),
    ),
)
def test__construction_details__minimal_xml_serialization(is_complete, is_complete_str):
    obj = ConstructionDetailsFactory(
        construction_complete=is_complete,
        construction_company_name=None,
        estimated_completion_time=None,
        availability=None,
        funding_type=None,
    )
    xml = obj_to_xml_str(obj)
    assert xml == (
        f"<construction-details>\n"
        f"  <construction-complete>{is_complete_str}</construction-complete>\n"
        f"</construction-details>\n"
    )


def test__construction_details__complete_xml_serialization():
    obj = ConstructionDetailsFactory(construction_complete=True)
    xml = obj_to_xml_str(obj)
    assert xml == (
        f"<construction-details>\n"
        f"  <construction-complete>K</construction-complete>\n"
        f"  <construction-company-name>{obj.construction_company_name}</construction-company-name>\n"
        f"  <estimated-completion-time>{obj.estimated_completion_time}</estimated-completion-time>\n"
        f"  <availability>{obj.availability.value}</availability>\n"
        f"  <funding-type>{obj.funding_type}</funding-type>\n"
        f"</construction-details>\n"
    )


def test__coordinates__xml_serialization():
    obj = CoordinatesFactory(
        latitude=12.3456789,
        longitude=12.3456789,
    )
    xml = obj_to_xml_str(obj)
    assert xml == (
        "<coordinates>\n"
        "  <latitude>12.34567</latitude>\n"
        "  <longitude>12.34567</longitude>\n"
        "</coordinates>\n"
    )


def test__more_info__minimal_xml_serialization():
    obj = MoreInfoFactory(
        link_text=None,
        link_image_url=None,
    )
    xml = obj_to_xml_str(obj)
    assert xml == f'<more-info url="{obj.url}"/>\n'


def test__more_info__complete_xml_serialization():
    obj = MoreInfoFactory()
    xml = obj_to_xml_str(obj)
    assert xml == (
        f'<more-info url="{obj.url}">\n'
        f"  <link-text>{obj.link_text}</link-text>\n"
        f"  <link-image-url>{obj.link_image_url}</link-image-url>\n"
        f"</more-info>\n"
    )


def test__picture__xml_serialization():
    obj = PictureFactory(timestamp=datetime(2020, 1, 1, 12, 0, 0))
    xml = obj_to_xml_str(obj)
    assert xml == f'<picture timestamp="20200101120000">{obj.image_url}</picture>\n'


def test__virtual_presentation__xml_serialization():
    obj = VirtualPresentationFactory()
    xml = obj_to_xml_str(obj)
    assert xml == (
        f'<virtual-presentation url="{obj.url}">{obj.link_text}</virtual-presentation>\n'
    )


def test__property_development__xml_serialization():
    mi = MoreInfoFactory()
    vp1 = VirtualPresentationFactory()
    vp2 = VirtualPresentationFactory()
    obj = PropertyDevelopmentFactory(more_info=mi, virtual_presentations=[vp1, vp2])
    xml = obj_to_xml_str(obj)
    assert xml == (
        f"<property-development>\n"
        f'  <more-info url="{mi.url}">\n'
        f"    <link-text>{mi.link_text}</link-text>\n"
        f"    <link-image-url>{mi.link_image_url}</link-image-url>\n"
        f"  </more-info>\n"
        f"  <virtual-presentations>\n"
        f'    <virtual-presentation url="{vp1.url}">{vp1.link_text}</virtual-presentation>\n'
        f'    <virtual-presentation url="{vp2.url}">{vp2.link_text}</virtual-presentation>\n'
        f"  </virtual-presentations>\n"
        f"</property-development>\n"
    )


def test__property_development__xml_serialization_sans_virtual_presentations():
    mi = MoreInfoFactory()
    obj = PropertyDevelopmentFactory(more_info=mi, virtual_presentations=None)
    xml = obj_to_xml_str(obj)
    assert xml == (
        f"<property-development>\n"
        f'  <more-info url="{mi.url}">\n'
        f"    <link-text>{mi.link_text}</link-text>\n"
        f"    <link-image-url>{mi.link_image_url}</link-image-url>\n"
        f"  </more-info>\n"
        f"</property-development>\n"
    )


def test__property_development__xml_serialization_sans_more_info():
    vp1 = VirtualPresentationFactory()
    vp2 = VirtualPresentationFactory()
    obj = PropertyDevelopmentFactory(more_info=None, virtual_presentations=[vp1, vp2])
    xml = obj_to_xml_str(obj)
    assert xml == (
        f"<property-development>\n"
        f"  <virtual-presentations>\n"
        f'    <virtual-presentation url="{vp1.url}">{vp1.link_text}</virtual-presentation>\n'
        f'    <virtual-presentation url="{vp2.url}">{vp2.link_text}</virtual-presentation>\n'
        f"  </virtual-presentations>\n"
        f"</property-development>\n"
    )


def test__real_estate_agent__xml_serialization():
    obj = RealEstateAgentFactory()
    xml = obj_to_xml_str(obj)
    assert xml == (
        f"<real-estate-agent>\n"
        f"  <vendor-id>{obj.vendor_id}</vendor-id>\n"
        f"  <contact-email>{obj.contact_email}</contact-email>\n"
        f"</real-estate-agent>\n"
    )


def test__housing_company__minimal_xml_serialization():
    rea = RealEstateAgentFactory()
    apt = ApartmentFactory()
    adr = AddressFactory()
    obj = HousingCompanyFactory(
        real_estate_agent=rea,
        real_estate_code=None,
        builder=None,
        apartment=apt,
        presentation_text=None,
        address=adr,
        coordinates=None,
        construction_details=None,
        pictures=None,
        city_plan_pictures=None,
        property_development=None,
        publication_start_date=datetime(2020, 1, 1, 12, 15, 00),
        publication_end_date=datetime(2020, 1, 1, 12, 15, 00),
    )
    xml = obj_to_xml_str(obj)
    assert xml == (
        f"<housing-company>\n"
        f"  <key>{obj.key}</key>\n"
        f"  <name>{obj.name}</name>\n"
        f"  <real-estate-agent>\n"
        f"    <vendor-id>{rea.vendor_id}</vendor-id>\n"
        f"    <contact-email>{rea.contact_email}</contact-email>\n"
        f"  </real-estate-agent>\n"
        f"  <apartment>\n"
        f"    <types>{apt.format_types()}</types>\n"
        f"  </apartment>\n"
        f"  <address>\n"
        f"    <street>{adr.street}</street>\n"
        f"    <postal-code>{adr.postal_code}</postal-code>\n"
        f"    <city>{adr.city}</city>\n"
        f"    <region>{adr.region}</region>\n"
        f"  </address>\n"
        f"  <publication-start-date>\n"
        f"    <year>2020</year>\n"
        f"    <month>01</month>\n"
        f"    <day>01</day>\n"
        f"    <hour>12:15</hour>\n"
        f"  </publication-start-date>\n"
        f"  <publication-end-date>\n"
        f"    <year>2020</year>\n"
        f"    <month>01</month>\n"
        f"    <day>01</day>\n"
        f"    <hour>12:15</hour>\n"
        f"  </publication-end-date>\n"
        f"</housing-company>\n"
    )


def test__housing_company__complete_xml_serialization():
    rea = RealEstateAgentFactory()
    bld = BuilderFactory()
    apt = ApartmentFactory()
    adr = AddressFactory()
    crd = CoordinatesFactory()
    cd = ConstructionDetailsFactory()
    pic = PictureFactory()
    cpp = CityPlanPictureFactory()
    vp = VirtualPresentationFactory()
    mi = MoreInfoFactory()
    pd = PropertyDevelopmentFactory(more_info=mi, virtual_presentations=[vp])
    obj = HousingCompanyFactory(
        real_estate_agent=rea,
        builder=bld,
        apartment=apt,
        address=adr,
        coordinates=crd,
        construction_details=cd,
        pictures=[pic],
        city_plan_pictures=[cpp],
        property_development=pd,
        publication_start_date=datetime(2020, 1, 1, 12, 15, 00),
        publication_end_date=datetime(2020, 1, 1, 12, 15, 00),
    )
    xml = obj_to_xml_str(obj)
    assert xml == (
        f"<housing-company>\n"
        f"  <key>{obj.key}</key>\n"
        f"  <name>{obj.name}</name>\n"
        f"  <real-estate-agent>\n"
        f"    <vendor-id>{rea.vendor_id}</vendor-id>\n"
        f"    <contact-email>{rea.contact_email}</contact-email>\n"
        f"  </real-estate-agent>\n"
        f"  <apartment>\n"
        f"    <types>{apt.format_types()}</types>\n"
        f"  </apartment>\n"
        f"  <address>\n"
        f"    <street>{adr.street}</street>\n"
        f"    <postal-code>{adr.postal_code}</postal-code>\n"
        f"    <city>{adr.city}</city>\n"
        f"    <region>{adr.region}</region>\n"
        f"  </address>\n"
        f"  <publication-start-date>\n"
        f"    <year>2020</year>\n"
        f"    <month>01</month>\n"
        f"    <day>01</day>\n"
        f"    <hour>12:15</hour>\n"
        f"  </publication-start-date>\n"
        f"  <publication-end-date>\n"
        f"    <year>2020</year>\n"
        f"    <month>01</month>\n"
        f"    <day>01</day>\n"
        f"    <hour>12:15</hour>\n"
        f"  </publication-end-date>\n"
        f"  <real-estate-code>{obj.real_estate_code}</real-estate-code>\n"
        f"  <builder>\n"
        f"    <logo-url>{bld.logo_url}</logo-url>\n"
        f"  </builder>\n"
        f"  <presentation-text>{obj.presentation_text}</presentation-text>\n"
        f"  <coordinates>\n"
        f"    <latitude>{crd.format_latitude()}</latitude>\n"
        f"    <longitude>{crd.format_longitude()}</longitude>\n"
        f"  </coordinates>\n"
        f"  <construction-details>\n"
        f"    <construction-complete>{yes_no_bool(cd.construction_complete)}</construction-complete>\n"
        f"    <construction-company-name>{cd.construction_company_name}</construction-company-name>\n"
        f"    <estimated-completion-time>{cd.estimated_completion_time}</estimated-completion-time>\n"
        f"    <availability>{cd.availability.value}</availability>\n"
        f"    <funding-type>{cd.funding_type}</funding-type>\n"
        f"  </construction-details>\n"
        f"  <pictures>\n"
        f'    <picture timestamp="{pic.format_timestamp()}">{pic.image_url}</picture>\n'
        f"  </pictures>\n"
        f"  <city-plan-pictures>\n"
        f'    <city-plan-picture timestamp="{cpp.format_timestamp()}">{cpp.image_url}</city-plan-picture>\n'
        f"  </city-plan-pictures>\n"
        f"  <property-development>\n"
        f'    <more-info url="{mi.url}">\n'
        f"      <link-text>{mi.link_text}</link-text>\n"
        f"      <link-image-url>{mi.link_image_url}</link-image-url>\n"
        f"    </more-info>\n"
        f"    <virtual-presentations>\n"
        f'      <virtual-presentation url="{vp.url}">{vp.link_text}</virtual-presentation>\n'
        f"    </virtual-presentations>\n"
        f"  </property-development>\n"
        f"</housing-company>\n"
    )


@override_settings(OIKOTIE_TRANSFER_ID="test", OIKOTIE_COMPANY_NAME="ATT", OIKOTIE_ENTRYPOINT='test')
def test_appartment_xml_created(test_folder):
    housing_company = HousingCompanyFactory.create_batch(1)
    test_file = create_housing_companies(
        housing_company, test_folder)
    test_xml = open(test_file, "r")
    test_xml = test_xml.read()

    expected = ["<?xml version='1.0' encoding='utf-8'?>",
                '<housing-company>', '<key>', '<real-estate-agent>', '<vendor-id>']

    assert all(item in test_xml for item in expected)

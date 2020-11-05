from dataclasses import dataclass
from datetime import datetime
from typing import List, Optional

from lxml import etree

from ..enums import ApartmentType, Availability, Case
from ..utils import truncate_to_n_decimal_places
from . import XMLModel

# Housing company picture models
# ==========================================


@dataclass
class _BasePicture(XMLModel):
    timestamp: datetime
    image_url: str

    def format_timestamp(self) -> str:
        return self.timestamp.strftime("%Y%m%d%H%M%S")

    def to_etree(self) -> etree._Element:
        element = etree.Element(
            self.Meta.element_name, timestamp=self.format_timestamp()
        )
        element.text = self.image_url
        return element


@dataclass
class Picture(_BasePicture):
    class Meta:
        element_name = "picture"
        case = Case.KEBAB


@dataclass
class CityPlanPicture(_BasePicture):
    class Meta:
        element_name = "city-plan-picture"
        case = Case.KEBAB


# Miscellaneous housing company models
# ==========================================


@dataclass
class Address(XMLModel):
    street: str
    postal_code: str
    city: str
    region: Optional[str] = None

    class Meta:
        element_name = "address"
        case = Case.KEBAB


@dataclass
class Apartment(XMLModel):
    types: List[ApartmentType]

    class Meta:
        element_name = "apartment"
        case = Case.KEBAB

    def format_types(self) -> str:
        return ", ".join([v.value for v in self.types])


@dataclass
class Builder(XMLModel):
    logo_url: str

    class Meta:
        element_name = "builder"
        case = Case.KEBAB


@dataclass
class ConstructionDetails(XMLModel):
    construction_complete: bool
    construction_company_name: Optional[str] = None
    estimated_completion_time: Optional[str] = None
    availability: Optional[Availability] = None
    funding_type: Optional[str] = None

    class Meta:
        element_name = "construction-details"
        case = Case.KEBAB


@dataclass
class Coordinates(XMLModel):
    latitude: float
    longitude: float

    class Meta:
        element_name = "coordinates"
        case = Case.KEBAB

    def format_latitude(self) -> str:
        return "{:.5f}".format(truncate_to_n_decimal_places(self.latitude, n=5))

    def format_longitude(self) -> str:
        return "{:.5f}".format(truncate_to_n_decimal_places(self.longitude, n=5))


@dataclass
class MoreInfo(XMLModel):
    url: str
    link_text: Optional[str] = None
    link_image_url: Optional[str] = None

    class Meta:
        element_name = "more-info"
        case = Case.KEBAB
        attributes = ["url"]


@dataclass
class VirtualPresentation(XMLModel):
    url: str
    link_text: str

    class Meta:
        element_name = "virtual-presentation"
        case = Case.KEBAB

    def to_etree(self) -> etree._Element:
        element = etree.Element(self.Meta.element_name, url=self.url)
        element.text = self.link_text
        return element


@dataclass
class PropertyDevelopment(XMLModel):
    more_info: MoreInfo
    virtual_presentations: List[VirtualPresentation]

    class Meta:
        element_name = "property-development"
        case = Case.KEBAB


@dataclass
class RealEstateAgent(XMLModel):
    vendor_id: str
    contact_email: str

    class Meta:
        element_name = "real-estate-agent"
        case = Case.KEBAB


@dataclass
class HousingCompany(XMLModel):
    key: str
    name: str
    real_estate_agent: RealEstateAgent
    apartment: Apartment
    address: Address
    publication_start_date: datetime
    publication_end_date: datetime
    real_estate_code: Optional[str] = None
    builder: Optional[List[Builder]] = None
    presentation_text: Optional[str] = None
    coordinates: Optional[Coordinates] = None
    construction_details: Optional[ConstructionDetails] = None
    pictures: Optional[List[Picture]] = None
    city_plan_pictures: Optional[List[CityPlanPicture]] = None
    property_development: Optional[PropertyDevelopment] = None

    class Meta:
        element_name = "housing-company"
        case = Case.KEBAB

    def _format_publication_date(self, name: str, value: datetime) -> etree._Element:
        element = etree.Element(name)
        child_elements = {
            "year": value.strftime("%Y"),
            "month": value.strftime("%m"),
            "day": value.strftime("%d"),
            "hour": value.strftime("%H:%M"),
        }

        for key, value in child_elements.items():
            child = etree.Element(key)
            child.text = value
            element.append(child)

        return element

    def format_publication_start_date(self) -> etree._Element:
        return self._format_publication_date(
            "publication-start-date", self.publication_start_date
        )

    def format_publication_end_date(self) -> etree._Element:
        return self._format_publication_date(
            "publication-end-date", self.publication_end_date
        )

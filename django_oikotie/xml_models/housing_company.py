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
    image_url: str
    timestamp: Optional[datetime] = None

    def format_timestamp(self) -> str:
        if self.timestamp:
            return self.timestamp.strftime("%Y%m%d%H%M%S")

    def to_etree(self) -> etree._Element:
        kwargs = {}

        timestamp_formatted = self.format_timestamp()
        if timestamp_formatted:
            kwargs["timestamp"] = timestamp_formatted

        element = etree.Element(self.Meta.element_name, **kwargs)
        element.text = self.format_image_url()
        return element

    def format_image_url(self) -> str:
        return self.image_url[:200]


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

    def format_street(self) -> str:
        return self.street[:100]

    def format_postal_code(self) -> str:
        return self.postal_code[:6]

    def format_city(self) -> str:
        return self.city[:50]

    def format_region(self) -> str:
        return self.region[:100]


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

    def format_construction_company_name(self) -> str:
        return self.construction_company_name[:100]


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

    def format_url(self) -> str:
        return self.url[:200]

    def format_link_text(self) -> str:
        return self.link_text[:50]

    def format_link_image_url(self) -> str:
        return self.link_image_url[:200]


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

    def format_url(self) -> str:
        return self.url[:200]

    def format_link_text(self) -> str:
        return self.link_text[:50]


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

    def format_key(self) -> str:
        return self.key[:100]

    def format_name(self) -> str:
        return self.name[:100]

    def format_real_estate_code(self) -> str:
        return self.real_estate_code[:200]

    def format_presentation_text(self) -> str:
        return self.presentation_text[:10000]

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

from dataclasses import dataclass

from django_oikotie.utils import object_to_etree


class BaseClass:
    def to_etree(self, case):
        return object_to_etree(self, case)


@dataclass
class RealEstateAgent(BaseClass):
    vendor_id = str
    contact_email = str


@dataclass
class Apartment(BaseClass):
    types: str
    presentation_text: str


@dataclass
class Address(BaseClass):
    street: str
    postal_code: str
    city: str


@dataclass
class HousingCompany(BaseClass):
    key: str
    name: str
    real_estate_code: str
    real_estate_agent: object
    apartment: object
    address: object

from dataclasses import dataclass

from django_oikotie.housing_company import BaseClass


@dataclass
class ModeOfHabitation(BaseClass):
    pass


@dataclass
class Apartment(BaseClass):
    key: str
    VendorIdentifier: str
    ModeOfHabitation: object
    StreetAddress: str
    City: str

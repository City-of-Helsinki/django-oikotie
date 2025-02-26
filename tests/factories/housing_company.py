import factory
import faker
from django.utils import timezone
from factory import fuzzy

from django_oikotie.enums import ApartmentType, Availability
from django_oikotie.xml_models.housing_company import (
    Address,
    Apartment,
    Builder,
    CityPlanPicture,
    ConstructionDetails,
    Coordinates,
    HousingCompany,
    MoreInfo,
    Picture,
    PropertyDevelopment,
    RealEstateAgent,
    VirtualPresentation,
)

fake = faker.Faker()


class AddressFactory(factory.Factory):
    class Meta:
        model = Address

    street = fuzzy.FuzzyText()
    postal_code = fuzzy.FuzzyText(length=6)
    city = fuzzy.FuzzyText()
    region = fuzzy.FuzzyText()


class ApartmentFactory(factory.Factory):
    class Meta:
        model = Apartment

    types = factory.List([fuzzy.FuzzyChoice([c for c in ApartmentType])])


class BuilderFactory(factory.Factory):
    class Meta:
        model = Builder

    logo_url = fuzzy.FuzzyText()


class CityPlanPictureFactory(factory.Factory):
    class Meta:
        model = CityPlanPicture

    timestamp = fuzzy.FuzzyDateTime(start_dt=timezone.now())
    image_url = fuzzy.FuzzyText()


class ConstructionDetailsFactory(factory.Factory):
    class Meta:
        model = ConstructionDetails

    construction_company_name = fuzzy.FuzzyText()
    construction_complete = fuzzy.FuzzyChoice([True, False])
    estimated_completion_time = fuzzy.FuzzyText()
    availability = fuzzy.FuzzyChoice([c for c in Availability])
    funding_type = fuzzy.FuzzyText()


class CoordinatesFactory(factory.Factory):
    class Meta:
        model = Coordinates

    x = fuzzy.FuzzyFloat(-90, 90)
    y = fuzzy.FuzzyFloat(-180, 180)


class MoreInfoFactory(factory.Factory):
    class Meta:
        model = MoreInfo

    url = fuzzy.FuzzyText()
    link_text = fuzzy.FuzzyText()
    link_image_url = fuzzy.FuzzyText()


class PictureFactory(factory.Factory):
    class Meta:
        model = Picture

    timestamp = fuzzy.FuzzyDateTime(start_dt=timezone.now())
    image_url = fuzzy.FuzzyText()


class VirtualPresentationFactory(factory.Factory):
    class Meta:
        model = VirtualPresentation

    url = fuzzy.FuzzyText()
    link_text = fuzzy.FuzzyText()


class PropertyDevelopmentFactory(factory.Factory):
    class Meta:
        model = PropertyDevelopment

    more_info = factory.SubFactory(MoreInfoFactory)
    virtual_presentations = factory.List(
        [factory.SubFactory(VirtualPresentationFactory) for _ in range(2)]
    )


class RealEstateAgentFactory(factory.Factory):
    class Meta:
        model = RealEstateAgent

    vendor_id = fuzzy.FuzzyText()
    contact_email = fake.email()


class HousingCompanyFactory(factory.Factory):
    class Meta:
        model = HousingCompany

    key = fuzzy.FuzzyText()
    name = fuzzy.FuzzyText()
    real_estate_code = fuzzy.FuzzyText()
    real_estate_agent = factory.SubFactory(RealEstateAgentFactory)
    builder = factory.SubFactory(BuilderFactory)
    apartment = factory.SubFactory(ApartmentFactory)
    presentation_text = fuzzy.FuzzyText()
    address = factory.SubFactory(AddressFactory)
    coordinates = factory.SubFactory(CoordinatesFactory)
    construction_details = factory.SubFactory(ConstructionDetailsFactory)
    pictures = factory.List([factory.SubFactory(PictureFactory) for _ in range(2)])
    city_plan_pictures = factory.List(
        [factory.SubFactory(CityPlanPictureFactory) for _ in range(2)]
    )
    property_development = factory.SubFactory(PropertyDevelopmentFactory)
    publication_start_date = fuzzy.FuzzyDateTime(start_dt=timezone.now())
    publication_end_date = fuzzy.FuzzyDateTime(start_dt=timezone.now())

import factory
from django.utils import timezone
from factory import fuzzy

from django_oikotie.enums import (
    ApartmentAction,
    ApartmentType,
    BuildingRightAmountType,
    EstateType,
    GeneralConditionLevel,
    LivingAreaType,
    ModeOfHabitationRentType,
    ModeOfHabitationType,
    NewDevelopmentStatusChoices,
    ParkingSpaceHeatingType,
    ParkingSpaceType,
    ShoreType,
    SiteType,
)
from django_oikotie.xml_models.apartment import (
    Apartment,
    Attachments,
    Balcony,
    BuildingRightsAmount,
    CableTvCharge,
    CampaignLink,
    CarParkingCharge,
    ChargeFee,
    City,
    CityPlanPicture,
    DebtPayable,
    ElectricityConsumptionCharge,
    Estate,
    EstateAgentRating,
    EstateAgentSocialMedia,
    FinancingFee,
    FinancingOffer1,
    FinancingOffer2,
    FloorArea,
    FloorLocation,
    GeneralCondition,
    HeatingCosts,
    HousingCompanyFee,
    Lift,
    LivingArea,
    MaintenanceFee,
    ModeOfHabitation,
    NewDevelopmentStatus,
    OnlineOfferLabel,
    ParkingSpace,
    Picture,
    PictureDescription,
    PromotionalOffer,
    RedemptionPrice,
    RentComission,
    Rented,
    RentFixedTerm,
    RentFurnished,
    RentPerDay,
    RentPerMonth,
    RentPerWeek,
    RentPerWeekEnd,
    RentPerYear,
    RentSecurityDeposit2,
    SalesPrice,
    Sauna,
    SaunaCharge,
    Shore,
    ShowingDate1,
    Site,
    SiteArea,
    TotalArea,
    UnencumberedSalesPrice,
    WaterFee,
    YearOfBuilding,
)


class CableTvChargeFactory(factory.Factory):
    class Meta:
        model = CableTvCharge

    value = fuzzy.FuzzyDecimal(0, 100)
    unit = fuzzy.FuzzyText()


class CarParkingChargeFactory(factory.Factory):
    class Meta:
        model = CarParkingCharge

    value = fuzzy.FuzzyDecimal(0, 100)
    unit = fuzzy.FuzzyText()


class ChargeFeeFactory(factory.Factory):
    class Meta:
        model = ChargeFee

    value = fuzzy.FuzzyDecimal(0, 100)
    unit = fuzzy.FuzzyText()


class ElectricityConsumptionChargeFactory(factory.Factory):
    class Meta:
        model = ElectricityConsumptionCharge

    value = fuzzy.FuzzyDecimal(0, 100)
    unit = fuzzy.FuzzyText()


class FinancingFeeFactory(factory.Factory):
    class Meta:
        model = FinancingFee

    value = fuzzy.FuzzyDecimal(0, 100)
    unit = fuzzy.FuzzyText()


class HeatingCostsFactory(factory.Factory):
    class Meta:
        model = HeatingCosts

    value = fuzzy.FuzzyDecimal(0, 100)
    unit = fuzzy.FuzzyText()


class HousingCompanyFeeFactory(factory.Factory):
    class Meta:
        model = HousingCompanyFee

    value = fuzzy.FuzzyDecimal(0, 100)
    unit = fuzzy.FuzzyText()


class MaintenanceFeeFactory(factory.Factory):
    class Meta:
        model = MaintenanceFee

    value = fuzzy.FuzzyDecimal(0, 100)
    unit = fuzzy.FuzzyText()


class RentPerDayFactory(factory.Factory):
    class Meta:
        model = RentPerDay

    value = fuzzy.FuzzyDecimal(0, 100)
    unit = fuzzy.FuzzyText()


class RentPerMonthFactory(factory.Factory):
    class Meta:
        model = RentPerMonth

    value = fuzzy.FuzzyDecimal(0, 100)
    unit = fuzzy.FuzzyText()


class RentPerWeekFactory(factory.Factory):
    class Meta:
        model = RentPerWeek

    value = fuzzy.FuzzyDecimal(0, 100)
    unit = fuzzy.FuzzyText()


class RentPerWeekEndFactory(factory.Factory):
    class Meta:
        model = RentPerWeekEnd

    value = fuzzy.FuzzyDecimal(0, 100)
    unit = fuzzy.FuzzyText()


class RentPerYearFactory(factory.Factory):
    class Meta:
        model = RentPerYear

    value = fuzzy.FuzzyDecimal(0, 100)
    unit = fuzzy.FuzzyText()


class SaunaChargeFactory(factory.Factory):
    class Meta:
        model = SaunaCharge

    value = fuzzy.FuzzyDecimal(0, 100)
    unit = fuzzy.FuzzyText()


class WaterFeeFactory(factory.Factory):
    class Meta:
        model = WaterFee

    value = fuzzy.FuzzyDecimal(0, 100)
    unit = fuzzy.FuzzyText()


class RedemptionPriceFactory(factory.Factory):
    class Meta:
        model = RedemptionPrice

    value = fuzzy.FuzzyDecimal(0, 100)
    currency = fuzzy.FuzzyText()


class RentComissionFactory(factory.Factory):
    class Meta:
        model = RentComission

    value = fuzzy.FuzzyDecimal(0, 100)
    currency = fuzzy.FuzzyText()


class SalesPriceFactory(factory.Factory):
    class Meta:
        model = SalesPrice

    value = fuzzy.FuzzyDecimal(0, 100)
    currency = fuzzy.FuzzyText()


class UnencumberedSalesPriceFactory(factory.Factory):
    class Meta:
        model = UnencumberedSalesPrice

    value = fuzzy.FuzzyDecimal(0, 100)
    currency = fuzzy.FuzzyText()


class AttachmentsFactory(factory.Factory):
    class Meta:
        model = Attachments

    url = fuzzy.FuzzyText()
    link_text = fuzzy.FuzzyText()


class BalconyFactory(factory.Factory):
    class Meta:
        model = Balcony

    value = fuzzy.FuzzyChoice([True, False])
    description = fuzzy.FuzzyText()


class BuildingRightsAmountFactory(factory.Factory):
    class Meta:
        model = BuildingRightsAmount

    type = fuzzy.FuzzyChoice([x for x in BuildingRightAmountType])
    amount = fuzzy.FuzzyFloat(0)


class CampaignLinkFactory(factory.Factory):
    class Meta:
        model = CampaignLink

    target_url = fuzzy.FuzzyText()
    picture_url = fuzzy.FuzzyText()


class CityFactory(factory.Factory):
    class Meta:
        model = City

    id = fuzzy.FuzzyInteger(0, 9999)
    value = fuzzy.FuzzyText()


class CityPlanPictureFactory(factory.Factory):
    class Meta:
        model = CityPlanPicture

    index = factory.Sequence(lambda n: n + 1)
    url = fuzzy.FuzzyText()


class DebtPayableFactory(factory.Factory):
    class Meta:
        model = DebtPayable

    value = fuzzy.FuzzyChoice([True, False])


class EstateFactory(factory.Factory):
    class Meta:
        model = Estate

    type = fuzzy.FuzzyChoice([x for x in EstateType])


class EstateAgentRatingFactory(factory.Factory):
    class Meta:
        model = EstateAgentRating

    value = fuzzy.FuzzyInteger(1, 5)


class EstateAgentSocialMediaFactory(factory.Factory):
    class Meta:
        model = EstateAgentSocialMedia

    url = fuzzy.FuzzyText()
    description = fuzzy.FuzzyText()


class FinancingOffer1Factory(factory.Factory):
    class Meta:
        model = FinancingOffer1

    percentage = fuzzy.FuzzyInteger(0, 100)
    price = fuzzy.FuzzyInteger(0, 100000)
    fee = fuzzy.FuzzyText()


class FinancingOffer2Factory(factory.Factory):
    class Meta:
        model = FinancingOffer2

    percentage = fuzzy.FuzzyInteger(0, 100)
    price = fuzzy.FuzzyInteger(0, 100000)
    fee = fuzzy.FuzzyText()


class FloorAreaFactory(factory.Factory):
    class Meta:
        model = FloorArea

    unit = fuzzy.FuzzyText()
    area = fuzzy.FuzzyFloat(0)


class FloorLocationFactory(factory.Factory):
    class Meta:
        model = FloorLocation

    high = fuzzy.FuzzyChoice([True, False])
    low = fuzzy.FuzzyChoice([True, False])
    number = fuzzy.FuzzyInteger(1, 8)
    count = fuzzy.FuzzyInteger(1, 8)
    description = fuzzy.FuzzyText()


class GeneralConditionFactory(factory.Factory):
    class Meta:
        model = GeneralCondition

    level = fuzzy.FuzzyChoice([x for x in GeneralConditionLevel])
    description = fuzzy.FuzzyText()


class LiftFactory(factory.Factory):
    class Meta:
        model = Lift

    value = fuzzy.FuzzyChoice([True, False])
    description = fuzzy.FuzzyText()


class LivingAreaFactory(factory.Factory):
    class Meta:
        model = LivingArea

    unit = fuzzy.FuzzyText()
    area = fuzzy.FuzzyFloat(0)


class ModeOfHabitationFactory(factory.Factory):
    class Meta:
        model = ModeOfHabitation

    type = fuzzy.FuzzyChoice([x for x in ModeOfHabitationType])
    rent_type = fuzzy.FuzzyChoice([x for x in ModeOfHabitationRentType])


class NewDevelopmentStatusFactory(factory.Factory):
    class Meta:
        model = NewDevelopmentStatus

    value = fuzzy.FuzzyChoice([x for x in NewDevelopmentStatusChoices])


class OnlineOfferLabelFactory(factory.Factory):
    class Meta:
        model = OnlineOfferLabel

    background_color = fuzzy.FuzzyText()
    text_color = fuzzy.FuzzyText()
    text_value = fuzzy.FuzzyText()


class ParkingSpaceFactory(factory.Factory):
    class Meta:
        model = ParkingSpace

    type = fuzzy.FuzzyChoice([x for x in ParkingSpaceType])
    heated = fuzzy.FuzzyChoice([x for x in ParkingSpaceHeatingType])
    electricity_outlet = fuzzy.FuzzyChoice([True, False])
    text_value = fuzzy.FuzzyText()


class PictureFactory(factory.Factory):
    class Meta:
        model = Picture

    is_floor_plan = fuzzy.FuzzyChoice([True, False])
    url = fuzzy.FuzzyText()
    index = factory.Sequence(lambda n: n + 1)


class PictureDescriptionFactory(factory.Factory):
    class Meta:
        model = PictureDescription

    index = factory.Sequence(lambda n: n + 1)
    description = fuzzy.FuzzyText()


class PromotionalOfferFactory(factory.Factory):
    class Meta:
        model = PromotionalOffer

    value = fuzzy.FuzzyChoice([True, False])


class RentedFactory(factory.Factory):
    class Meta:
        model = Rented

    value = fuzzy.FuzzyChoice([True, False])


class RentFixedTermFactory(factory.Factory):
    class Meta:
        model = RentFixedTerm

    value = fuzzy.FuzzyChoice([True, False])


class RentFurnishedFactory(factory.Factory):
    class Meta:
        model = RentFurnished

    value = fuzzy.FuzzyChoice([True, False])


class RentSecurityDeposit2Factory(factory.Factory):
    class Meta:
        model = RentSecurityDeposit2

    value = fuzzy.FuzzyInteger(0)
    currency = fuzzy.FuzzyText()


class SaunaFactory(factory.Factory):
    class Meta:
        model = Sauna

    own = fuzzy.FuzzyChoice([True, False])
    common = fuzzy.FuzzyChoice([True, False])
    description = fuzzy.FuzzyText()


class ShoreFactory(factory.Factory):
    class Meta:
        model = Shore

    type = fuzzy.FuzzyChoice([x for x in ShoreType])


class ShowingDate1Factory(factory.Factory):
    class Meta:
        model = ShowingDate1

    value = fuzzy.FuzzyDate(timezone.now().date())
    first_showing = fuzzy.FuzzyChoice([True, False])


class SiteFactory(factory.Factory):
    class Meta:
        model = Site

    type = fuzzy.FuzzyChoice([x for x in SiteType])


class SiteAreaFactory(factory.Factory):
    class Meta:
        model = SiteArea

    area = fuzzy.FuzzyFloat(0)
    unit = fuzzy.FuzzyText()


class TotalAreaFactory(factory.Factory):
    class Meta:
        model = TotalArea

    unit = fuzzy.FuzzyText()
    min = fuzzy.FuzzyInteger(0)
    max = fuzzy.FuzzyInteger(0)
    area = fuzzy.FuzzyFloat(0)


class YearOfBuildingFactory(factory.Factory):
    class Meta:
        model = YearOfBuilding

    original = fuzzy.FuzzyInteger(0)
    description = fuzzy.FuzzyText()


class MinimalApartmentFactory(factory.Factory):
    class Meta:
        model = Apartment

    type = fuzzy.FuzzyChoice([x for x in ApartmentType])
    new_houses = fuzzy.FuzzyChoice([True, False])
    key = fuzzy.FuzzyText()
    vendor_identifier = fuzzy.FuzzyText()
    mode_of_habitation = factory.SubFactory(ModeOfHabitationFactory)
    street_address = fuzzy.FuzzyText()
    city = factory.SubFactory(CityFactory)


class ApartmentFactory(factory.Factory):
    class Meta:
        model = Apartment

    action = fuzzy.FuzzyChoice([x for x in ApartmentAction])
    type = fuzzy.FuzzyChoice([x for x in ApartmentType])
    new_houses = fuzzy.FuzzyChoice([True, False])
    new_apartment_reserved = fuzzy.FuzzyChoice([True, False])

    key = fuzzy.FuzzyText()
    vendor_identifier = fuzzy.FuzzyText()
    estate = factory.SubFactory(EstateFactory)
    mode_of_habitation = factory.SubFactory(ModeOfHabitationFactory)
    mode_of_financing = fuzzy.FuzzyText()
    apartment_city_plan_id = fuzzy.FuzzyText()
    hide_building_data = fuzzy.FuzzyChoice([True, False])

    street_address = fuzzy.FuzzyText()
    postal_code = fuzzy.FuzzyText()
    other_post_code = fuzzy.FuzzyText()
    post_office = fuzzy.FuzzyText()
    city = factory.SubFactory(CityFactory)
    region = fuzzy.FuzzyText()
    country = fuzzy.FuzzyText()
    latitude = fuzzy.FuzzyFloat(-90, 90)
    longitude = fuzzy.FuzzyFloat(-180, 180)

    oikotie_id = fuzzy.FuzzyText()
    title = fuzzy.FuzzyText()
    description = fuzzy.FuzzyText()
    supplementary_information = fuzzy.FuzzyText()
    direction = fuzzy.FuzzyText()
    pictures = factory.List([factory.SubFactory(PictureFactory) for _ in range(2)])
    picture_gallery_promotion = fuzzy.FuzzyText()
    picture_gallery_promotion_url = fuzzy.FuzzyText()
    picture_descriptions = factory.List(
        [factory.SubFactory(PictureDescriptionFactory) for _ in range(2)]
    )
    city_plan_pictures = factory.List(
        [factory.SubFactory(CityPlanPictureFactory) for _ in range(2)]
    )
    virtual_presentation = fuzzy.FuzzyText()
    video_presentation_url = fuzzy.FuzzyText()
    listing_background_image = fuzzy.FuzzyText()
    listing_background_color = fuzzy.FuzzyText()

    floor_location = factory.SubFactory(FloorLocationFactory)
    number_of_rooms = fuzzy.FuzzyInteger(1, 5)
    room_types = fuzzy.FuzzyText()
    other_space_description = fuzzy.FuzzyText()
    balcony = factory.SubFactory(BalconyFactory)
    has_terrace = fuzzy.FuzzyChoice([True, False])
    terrace = fuzzy.FuzzyText()
    direction_of_windows = fuzzy.FuzzyText()
    view = fuzzy.FuzzyText()
    cellar = fuzzy.FuzzyChoice([True, False])

    living_area = factory.SubFactory(LivingAreaFactory)
    living_area_type = fuzzy.FuzzyChoice([x for x in LivingAreaType])
    total_area = factory.SubFactory(TotalAreaFactory)
    floor_area = factory.SubFactory(FloorAreaFactory)
    residental_apartment_area = fuzzy.FuzzyFloat(0)
    office_area = fuzzy.FuzzyFloat(0)
    estate_area = fuzzy.FuzzyText()
    forest_amount = fuzzy.FuzzyText()
    land_area = fuzzy.FuzzyText()

    real_estate_id = fuzzy.FuzzyText()
    real_estate_code = fuzzy.FuzzyText()
    housing_company_name = fuzzy.FuzzyText()
    housing_company_key = fuzzy.FuzzyText()
    business_id = fuzzy.FuzzyText()
    disponent = fuzzy.FuzzyText()
    real_estate_management = fuzzy.FuzzyText()
    number_of_apartments = fuzzy.FuzzyInteger(1, 999)
    lift = factory.SubFactory(LiftFactory)

    year_of_building = factory.SubFactory(YearOfBuildingFactory)
    year_start_of_use = fuzzy.FuzzyInteger(1990, 2020)
    basic_renovations = fuzzy.FuzzyText()
    renovation_year_facade = fuzzy.FuzzyText()
    renovation_year_roof = fuzzy.FuzzyText()
    renovation_year_plumbing = fuzzy.FuzzyText()
    renovation_year_bathrooms = fuzzy.FuzzyText()
    future_renovations = fuzzy.FuzzyText()
    future_renovation_year_facade = fuzzy.FuzzyText()
    future_renovation_year_roof = fuzzy.FuzzyText()
    future_renovation_year_plumbing = fuzzy.FuzzyText()
    future_renovation_year_bathrooms = fuzzy.FuzzyText()

    heating = fuzzy.FuzzyText()
    roof_type = fuzzy.FuzzyText()
    building_rights = fuzzy.FuzzyText()
    building_rights_amount = factory.SubFactory(BuildingRightsAmountFactory)
    number_of_offices = fuzzy.FuzzyInteger(1, 5)

    sanitation = fuzzy.FuzzyText()
    water_and_sewage = fuzzy.FuzzyText()
    sewer_system = fuzzy.FuzzyText()
    use_of_water = fuzzy.FuzzyText()
    ventilation_system = fuzzy.FuzzyText()
    other_buildings = fuzzy.FuzzyText()
    more_estate_information = fuzzy.FuzzyText()

    general_condition = factory.SubFactory(GeneralConditionFactory)
    condition_inspection = fuzzy.FuzzyText()

    estate_name_and_number = fuzzy.FuzzyText()
    site = factory.SubFactory(SiteFactory)
    site_rent = fuzzy.FuzzyText()
    site_rent_contract_end_date = fuzzy.FuzzyDate(timezone.now().date())
    site_area = factory.SubFactory(SiteAreaFactory)
    area_description = fuzzy.FuzzyText()
    shore = factory.SubFactory(ShoreFactory)
    shores_description = fuzzy.FuzzyText()
    shore_direction = fuzzy.FuzzyText()
    shore_length = fuzzy.FuzzyText()
    waters_description = fuzzy.FuzzyText()
    building_plan_information = fuzzy.FuzzyText()
    building_plan_situation = fuzzy.FuzzyText()
    grounds = fuzzy.FuzzyText()
    yard_description = fuzzy.FuzzyText()
    yard_direction = fuzzy.FuzzyText()

    heating_costs = factory.SubFactory(HeatingCostsFactory)
    sauna_charge = factory.SubFactory(SaunaChargeFactory)
    estate_tax = fuzzy.FuzzyText()
    housing_company_fee = factory.SubFactory(HousingCompanyFeeFactory)
    financing_fee = factory.SubFactory(FinancingFeeFactory)
    maintenance_fee = factory.SubFactory(MaintenanceFeeFactory)
    water_fee = factory.SubFactory(WaterFeeFactory)
    water_fee_explanation = fuzzy.FuzzyText()
    electricity_consumption = fuzzy.FuzzyText()
    electricity_consumption_charge = factory.SubFactory(
        ElectricityConsumptionChargeFactory
    )
    cable_tv_charge = factory.SubFactory(CableTvChargeFactory)
    road_costs = fuzzy.FuzzyText()
    other_fees = fuzzy.FuzzyText()
    share_of_debt_85 = fuzzy.FuzzyDecimal(0, 100)
    share_of_debt_70 = fuzzy.FuzzyDecimal(0, 100)
    charge_fee = factory.SubFactory(ChargeFeeFactory)
    car_parking_charge = factory.SubFactory(CarParkingChargeFactory)

    building_material = fuzzy.FuzzyText()
    foundation = fuzzy.FuzzyText()
    wall_construction = fuzzy.FuzzyText()
    roof_material = fuzzy.FuzzyText()
    floor = fuzzy.FuzzyText()
    bedroom_floor = fuzzy.FuzzyText()
    kitchen_floor = fuzzy.FuzzyText()
    living_room_floor = fuzzy.FuzzyText()
    bathroom_floor = fuzzy.FuzzyText()
    bedroom_wall = fuzzy.FuzzyText()
    kitchen_wall = fuzzy.FuzzyText()
    living_room_wall = fuzzy.FuzzyText()
    bathroom_wall = fuzzy.FuzzyText()
    other_rooms_materials = fuzzy.FuzzyText()
    kitchen_appliances = fuzzy.FuzzyText()
    bathroom_appliances = fuzzy.FuzzyText()
    bedroom_appliances = fuzzy.FuzzyText()
    living_room_appliances = fuzzy.FuzzyText()
    non_included_appliances = fuzzy.FuzzyText()
    other_included_appliances = fuzzy.FuzzyText()
    sauna = factory.SubFactory(SaunaFactory)
    storage_space = fuzzy.FuzzyText()
    parking_space = factory.SubFactory(ParkingSpaceFactory)
    car_storage = fuzzy.FuzzyText()
    common_areas = fuzzy.FuzzyText()
    antenna_system = fuzzy.FuzzyText()
    tv_appliances = fuzzy.FuzzyText()
    internet_appliances = fuzzy.FuzzyText()

    date_when_available = fuzzy.FuzzyDate(timezone.now().date())
    becomes_available = fuzzy.FuzzyText()
    rent_fixed_term_start = fuzzy.FuzzyDate(timezone.now().date())
    rent_fixed_term_end = fuzzy.FuzzyDate(timezone.now().date())
    rent_min_length = fuzzy.FuzzyText()
    extra_visibility_start_date_time = fuzzy.FuzzyDateTime(timezone.now())

    rented = factory.SubFactory(RentedFactory)
    rent_furnished = factory.SubFactory(RentFurnishedFactory)
    municipal_development = fuzzy.FuzzyText()
    honoring_clause = fuzzy.FuzzyText()
    lease_holder = fuzzy.FuzzyText()
    term_of_lease = fuzzy.FuzzyText()
    encumbrances = fuzzy.FuzzyText()
    mortgages = fuzzy.FuzzyText()
    rent_increase = fuzzy.FuzzyText()
    renting_terms = fuzzy.FuzzyText()
    rent_fixed_term = factory.SubFactory(RentFixedTermFactory)

    services = fuzzy.FuzzyText()
    connections = fuzzy.FuzzyText()
    driving_instructions = fuzzy.FuzzyText()

    rent_per_month = factory.SubFactory(RentPerMonthFactory)
    rent_per_day = factory.SubFactory(RentPerDayFactory)
    rent_per_week = factory.SubFactory(RentPerWeekFactory)
    rent_per_year = factory.SubFactory(RentPerYearFactory)
    rent_per_week_end = factory.SubFactory(RentPerWeekEndFactory)
    unencumbered_sales_price = factory.SubFactory(UnencumberedSalesPriceFactory)
    sales_price = factory.SubFactory(SalesPriceFactory)
    debt_payable = factory.SubFactory(DebtPayableFactory)
    redemption_price = factory.SubFactory(RedemptionPriceFactory)
    buyer_costs = fuzzy.FuzzyText()
    apartment_rent_income = fuzzy.FuzzyDecimal(100, 1000)
    rent_comission = factory.SubFactory(RentComissionFactory)
    rent_security_deposit = fuzzy.FuzzyText()
    rent_security_deposit2 = factory.SubFactory(RentSecurityDeposit2Factory)
    financing_offer1 = factory.SubFactory(FinancingOffer1Factory)
    financing_offer2 = factory.SubFactory(FinancingOffer2Factory)
    site_repurchase_price = fuzzy.FuzzyDecimal(100, 1000)
    site_condominium_fee = fuzzy.FuzzyDecimal(100, 1000)

    magazine_identifier = fuzzy.FuzzyText()
    print_media_text = fuzzy.FuzzyText()

    estate_agent_contact_person = fuzzy.FuzzyText()
    estate_agent_email = fuzzy.FuzzyText()
    estate_agent_telephone = fuzzy.FuzzyText()
    estate_agent_title = fuzzy.FuzzyText()
    estate_agent_degrees = fuzzy.FuzzyText()
    estate_agent_rating = factory.SubFactory(EstateAgentRatingFactory)
    estate_agent_social_media = factory.SubFactory(EstateAgentSocialMediaFactory)
    estate_agent_contact_person_picture_url = fuzzy.FuzzyText()

    inquiries = fuzzy.FuzzyText()
    showing_date1 = factory.SubFactory(ShowingDate1Factory)
    showing_start_time1 = fuzzy.FuzzyText()
    showing_end_time1 = fuzzy.FuzzyText()
    showing_date_explanation1 = fuzzy.FuzzyText()
    showing_date2 = fuzzy.FuzzyDate(timezone.now().date())
    showing_start_time2 = fuzzy.FuzzyText()
    showing_end_time2 = fuzzy.FuzzyText()
    showing_date_explanation2 = fuzzy.FuzzyText()
    contact_request_email = fuzzy.FuzzyText()
    electronic_brochure_request_email = fuzzy.FuzzyText()
    electronic_brochure_request_url = fuzzy.FuzzyText()
    application_url = fuzzy.FuzzyText()
    show_lead_form = fuzzy.FuzzyChoice([True, False])

    more_info_url = fuzzy.FuzzyText()
    attachments = factory.SubFactory(AttachmentsFactory)
    campaign_link = factory.SubFactory(CampaignLinkFactory)
    banner_html = fuzzy.FuzzyText()
    promotional_offer = factory.SubFactory(PromotionalOfferFactory)
    promotional_offer_title = fuzzy.FuzzyText()
    promotional_offer_description = fuzzy.FuzzyText()
    promotional_offer_url = fuzzy.FuzzyText()
    promotional_offer_url_text = fuzzy.FuzzyText()
    promotional_offer_logo = fuzzy.FuzzyText()
    promotional_offer_color = fuzzy.FuzzyText()
    online_offer = fuzzy.FuzzyChoice([True, False])
    online_offer_logo = fuzzy.FuzzyText()
    online_offer_url = fuzzy.FuzzyText()
    online_offer_highest_bid = fuzzy.FuzzyDecimal(100, 1000)
    online_offer_label = factory.SubFactory(OnlineOfferLabelFactory)
    online_offer_search_logo = fuzzy.FuzzyText()
    rc_energy_flag = fuzzy.FuzzyText()
    rc_energyclass = fuzzy.FuzzyText()
    rc_wastewater_flag = fuzzy.FuzzyText()

    estate_division = fuzzy.FuzzyText()

    new_development_status = factory.SubFactory(NewDevelopmentStatusFactory)
    time_of_completion = fuzzy.FuzzyDate(timezone.now().date())

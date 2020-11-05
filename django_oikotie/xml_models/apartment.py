from dataclasses import dataclass
from datetime import date, datetime
from decimal import Decimal
from typing import Generator, List, Literal, Optional

from lxml import etree

from ..enums import (
    ApartmentAction,
    ApartmentType,
    BuildingRightAmountType,
    Case,
    EstateType,
    GeneralConditionLevel,
    LivingAreaType,
    ModeOfHabitationRentType,
    ModeOfHabitationType,
    NewDevelopmentStatusChoices,
    ParkingSpaceHeatingType,
    ParkingSpaceType,
    ShoreType,
    Site,
)
from ..utils import truncate_to_n_decimal_places, yes_no_bool
from . import XMLModel

# Fees & Costs
# ================================


@dataclass
class _Cost(XMLModel):
    value: Decimal
    unit: str

    class Meta:
        case = Case.PASCAL

    def format_value(self) -> str:
        return str(truncate_to_n_decimal_places(self.value, n=2))

    def to_etree(self) -> etree._Element:
        element = etree.Element(self.Meta.element_name, unit=self.unit)
        element.text = self.format_value()
        return element


@dataclass
class CableTvCharge(_Cost):
    class Meta(_Cost.Meta):
        element_name = "CableTvCharge"


@dataclass
class CarParkingCharge(_Cost):
    class Meta(_Cost.Meta):
        element_name = "CarParkingCharge"


@dataclass
class ChargeFee(_Cost):
    class Meta(_Cost.Meta):
        element_name = "ChargeFee"


@dataclass
class ElectricityConsumption(_Cost):
    class Meta(_Cost.Meta):
        element_name = "ElectricityConsumption"


@dataclass
class FinancingFee(_Cost):
    class Meta(_Cost.Meta):
        element_name = "FinancingFee"


@dataclass
class HeatingCosts(_Cost):
    class Meta(_Cost.Meta):
        element_name = "HeatingCosts"


@dataclass
class HousingCompanyFee(_Cost):
    class Meta(_Cost.Meta):
        element_name = "HousingCompanyFee"


@dataclass
class MaintenanceFee(_Cost):
    class Meta(_Cost.Meta):
        element_name = "MaintenanceFee"


@dataclass
class RentPerDay(_Cost):
    class Meta(_Cost.Meta):
        element_name = "RentPerDay"


@dataclass
class RentPerMonth(_Cost):
    class Meta(_Cost.Meta):
        element_name = "RentPerMonth"


@dataclass
class RentPerWeek(_Cost):
    class Meta(_Cost.Meta):
        element_name = "RentPerWeek"


@dataclass
class RentPerWeekEnd(_Cost):
    class Meta(_Cost.Meta):
        element_name = "RentPerWeekEnd"


@dataclass
class RentPerYear(_Cost):
    class Meta(_Cost.Meta):
        element_name = "RentPerYear"


@dataclass
class SaunaCharge(_Cost):
    class Meta(_Cost.Meta):
        element_name = "SaunaCharge"


@dataclass
class WaterFee(_Cost):
    class Meta(_Cost.Meta):
        element_name = "WaterFee"


# Prices
# ================================


@dataclass
class _Price(XMLModel):
    value: Decimal
    currency: str

    class Meta:
        case = Case.PASCAL

    def format_value(self) -> str:
        return str(truncate_to_n_decimal_places(self.value, n=2))

    def to_etree(self) -> etree._Element:
        element = etree.Element(self.Meta.element_name, currency=self.currency)
        element.text = self.format_value()
        return element


@dataclass
class RedemptionPrice(_Price):
    class Meta(_Price.Meta):
        element_name = "RedemptionPrice"


@dataclass
class RentComission(_Price):
    class Meta(_Price.Meta):
        element_name = "RentComission"


@dataclass
class SalesPrice(_Price):
    class Meta(_Price.Meta):
        element_name = "SalesPrice"


@dataclass
class UnencumberedSalesPrice(_Price):
    class Meta(_Price.Meta):
        element_name = "UnencumberedSalesPrice"


# Miscellaneous
# ================================


@dataclass
class Attachments(XMLModel):
    url: str
    link_text: str

    class Meta:
        element_name = "Attachments"
        case = Case.PASCAL

    def to_etree(self) -> etree._Element:
        element = etree.Element(self.Meta.element_name, url=self.url)
        element.text = self.link_text
        return element


@dataclass
class Balcony(XMLModel):
    value: bool
    description: str

    class Meta:
        element_name = "Balcony"
        case = Case.PASCAL

    def to_etree(self) -> etree._Element:
        element = etree.Element(self.Meta.element_name, value=yes_no_bool(self.value))
        element.text = self.description
        return element


@dataclass
class BuildingRightsAmount(XMLModel):
    type: BuildingRightAmountType
    amount: float

    class Meta:
        element_name = "BuildingRightsAmount"
        case = Case.PASCAL

    def format_amount(self) -> str:
        return str(truncate_to_n_decimal_places(self.amount, n=2))

    def to_etree(self) -> etree._Element:
        element = etree.Element(self.Meta.element_name, type=self.type.value)
        element.text = self.format_amount()
        return element


@dataclass
class CampaignLink(XMLModel):
    target_url: str
    picture_url: str

    class Meta:
        element_name = "CampaignLink"
        case = Case.PASCAL
        case_overrides = {
            "target_url": Case.CAMEL,
            "picture_url": Case.CAMEL,
        }
        attributes = ["target_url", "picture_url"]


@dataclass
class City(XMLModel):
    id: int
    value: str

    class Meta:
        element_name = "City"
        case = Case.PASCAL

    def to_etree(self) -> etree._Element:
        element = etree.Element(self.Meta.element_name, id=str(self.id))
        element.text = self.value
        return element


@dataclass
class CityPlanPicture(XMLModel):
    index: int
    url: str

    class Meta:
        element_name = "CityPlanPicture"
        case = Case.PASCAL

    def to_etree(self) -> etree._Element:
        element = etree.Element(f"{self.Meta.element_name}{self.index}")
        element.text = self.url
        return element


@dataclass
class DebtPayable(XMLModel):
    value: bool

    class Meta:
        element_name = "DebtPayable"
        case = Case.PASCAL
        case_overrides = {
            "value": Case.CAMEL,
        }
        attributes = ["value"]

    def format_value(self) -> str:
        return yes_no_bool(self.value)


@dataclass
class Estate(XMLModel):
    type: EstateType

    class Meta:
        element_name = "Estate"
        case = Case.PASCAL
        case_overrides = {
            "type": Case.CAMEL,
        }
        attributes = ["type"]


@dataclass
class EstateAgentRating(XMLModel):
    value: Literal[1, 2, 3, 4, 5]

    class Meta:
        element_name = "EstateAgentRating"
        case = Case.PASCAL
        case_overrides = {
            "value": Case.CAMEL,
        }
        attributes = ["value"]


@dataclass
class EstateAgentSocialMedia(XMLModel):
    url: str
    description: str

    class Meta:
        element_name = "EstateAgentSocialMedia"
        case = Case.PASCAL

    def to_etree(self) -> etree._Element:
        element = etree.Element(self.Meta.element_name, url=self.url)
        element.text = self.description
        return element


@dataclass
class _FinancingOffer(XMLModel):
    percentage: int
    price: int
    fee: str

    class Meta:
        case = Case.PASCAL
        case_overrides = {
            "percentage": Case.CAMEL,
            "price": Case.CAMEL,
            "fee": Case.CAMEL,
        }
        attributes = ["percentage", "price", "fee"]


@dataclass
class FinancingOffer1(_FinancingOffer):
    class Meta(_FinancingOffer.Meta):
        element_name = "FinancingOffer1"


@dataclass
class FinancingOffer2(_FinancingOffer):
    class Meta(_FinancingOffer.Meta):
        element_name = "FinancingOffer2"


@dataclass
class FloorArea(XMLModel):
    unit: str
    area: float

    class Meta:
        element_name = "FloorArea"
        case = Case.PASCAL

    def format_area(self) -> str:
        return str(truncate_to_n_decimal_places(self.area, n=2))

    def to_etree(self) -> etree._Element:
        element = etree.Element(self.Meta.element_name, unit=self.unit)
        element.text = self.format_area()
        return element


@dataclass
class FloorLocation(XMLModel):
    high: bool
    low: bool
    number: int
    count: int
    description: str

    class Meta:
        element_name = "FloorLocation"
        case = Case.PASCAL

    def to_etree(self) -> etree._Element:
        element = etree.Element(
            self.Meta.element_name,
            high=yes_no_bool(self.high),
            low=yes_no_bool(self.low),
            number=str(self.number),
            count=str(self.count),
        )
        element.text = self.description
        return element


@dataclass
class GeneralCondition(XMLModel):
    level: GeneralConditionLevel
    description: str

    class Meta:
        element_name = "GeneralCondition"
        case = Case.PASCAL

    def to_etree(self) -> etree._Element:
        element = etree.Element(self.Meta.element_name, level=str(self.level.value))
        element.text = self.description
        return element


@dataclass
class Lift(XMLModel):
    value: bool
    description: str

    class Meta:
        element_name = "Lift"
        case = Case.PASCAL

    def to_etree(self) -> etree._Element:
        element = etree.Element(self.Meta.element_name, value=yes_no_bool(self.value))
        element.text = self.description
        return element


@dataclass
class LivingArea(XMLModel):
    unit: str
    area: float

    class Meta:
        element_name = "LivingArea"
        case = Case.PASCAL

    def format_area(self) -> str:
        return str(truncate_to_n_decimal_places(self.area, n=2))

    def to_etree(self) -> etree._Element:
        element = etree.Element(self.Meta.element_name, unit=self.unit)
        element.text = self.format_area()
        return element


@dataclass
class ModeOfHabitation(XMLModel):
    type: ModeOfHabitationType
    rent_type: ModeOfHabitationRentType

    class Meta:
        element_name = "ModeOfHabitation"
        case = Case.PASCAL
        case_overrides = {
            "type": Case.CAMEL,
            "rent_type": Case.CAMEL,
        }
        attributes = ["type", "rent_type"]


@dataclass
class NewDevelopmentStatus(XMLModel):
    value: NewDevelopmentStatusChoices

    class Meta:
        element_name = "NewDevelopmentStatus"
        case = Case.PASCAL
        case_overrides = {
            "value": Case.CAMEL,
        }
        attributes = ["value"]


@dataclass
class OnlineOfferLabel(XMLModel):
    background_color: str
    text_color: str
    text_value: str

    class Meta:
        element_name = "OnlineOfferLabel"
        case = Case.PASCAL

    def to_etree(self) -> etree._Element:
        element = etree.Element(
            self.Meta.element_name,
            backgroundColor=self.background_color,
            textColor=self.text_color,
        )
        element.text = self.text_value
        return element


@dataclass
class ParkingSpace(XMLModel):
    type: ParkingSpaceType
    heated: ParkingSpaceHeatingType
    electricity_outlet: bool
    text_value: str

    class Meta:
        element_name = "ParkingSpace"
        case = Case.PASCAL

    def to_etree(self) -> etree._Element:
        element = etree.Element(
            self.Meta.element_name,
            type=str(self.type.value),
            heated=str(self.heated.value),
            electricityOutlet=yes_no_bool(self.electricity_outlet),
        )
        element.text = self.text_value
        return element


@dataclass
class Picture(XMLModel):
    index: int
    is_floor_plan: bool
    url: str

    class Meta:
        element_name = "PictureX"
        case = Case.PASCAL

    def to_etree(self) -> etree._Element:
        element = etree.Element(
            self.Meta.element_name.replace("X", str(self.index)),
            isFloorPlan=yes_no_bool(self.is_floor_plan),
        )
        element.text = self.url
        return element


@dataclass
class PictureDescription(XMLModel):
    index: int
    description: str

    class Meta:
        element_name = "PictureXDescription"
        case = Case.PASCAL

    def to_etree(self) -> etree._Element:
        element = etree.Element(self.Meta.element_name.replace("X", str(self.index)))
        element.text = self.description
        return element


@dataclass
class _ValueAttrModel(XMLModel):
    value: bool

    class Meta:
        case = Case.CAMEL
        attributes = ["value"]

    def format_value(self) -> str:
        return yes_no_bool(self.value)


@dataclass
class PromotionalOffer(_ValueAttrModel):
    class Meta(_ValueAttrModel.Meta):
        element_name = "PromotionalOffer"


@dataclass
class Rented(_ValueAttrModel):
    class Meta(_ValueAttrModel.Meta):
        element_name = "Rented"


@dataclass
class RentFixedTerm(_ValueAttrModel):
    class Meta(_ValueAttrModel.Meta):
        element_name = "RentFixedTerm"


@dataclass
class RentFurnished(_ValueAttrModel):
    class Meta(_ValueAttrModel.Meta):
        element_name = "RentFurnished"


@dataclass
class RentSecurityDeposit2(XMLModel):
    value: int
    currency: str

    class Meta:
        element_name = "RentSecurityDeposit2"
        case = Case.PASCAL

    def format_value(self) -> str:
        return str(truncate_to_n_decimal_places(self.value, n=2))

    def to_etree(self) -> etree._Element:
        element = etree.Element(self.Meta.element_name, currency=self.currency)
        element.text = self.format_value()
        return element


@dataclass
class Sauna(XMLModel):
    own: bool
    common: bool
    description: str

    class Meta:
        element_name = "Sauna"
        case = Case.PASCAL

    def to_etree(self) -> etree._Element:
        element = etree.Element(
            self.Meta.element_name,
            own=yes_no_bool(self.own),
            common=yes_no_bool(self.common),
        )
        element.text = self.description
        return element


@dataclass
class Shore(XMLModel):
    type: ShoreType

    class Meta:
        element_name = "Shore"
        case = Case.CAMEL
        attributes = ["type"]


@dataclass
class ShowingDate1(XMLModel):
    value: date
    first_showing: bool

    class Meta:
        element_name = "ShowingDate1"
        case = Case.PASCAL

    def to_etree(self) -> etree._Element:
        element = etree.Element(
            self.Meta.element_name,
            firstShowing=yes_no_bool(self.first_showing),
        )
        element.text = self.value.strftime("%d.%m.%Y")
        return element


@dataclass
class SiteArea(XMLModel):
    area: float
    unit: str

    class Meta:
        element_name = "SiteArea"
        case = Case.PASCAL

    def format_area(self) -> str:
        return "{:.2f}".format(truncate_to_n_decimal_places(self.area, n=2))

    def to_etree(self) -> etree._Element:
        element = etree.Element(
            self.Meta.element_name,
            unit=self.unit,
        )
        element.text = self.format_area()
        return element


@dataclass
class TotalArea(XMLModel):
    unit: str
    area: float
    min: Optional[int]
    max: Optional[int]

    class Meta:
        element_name = "TotalArea"
        case = Case.PASCAL

    def format_area(self) -> str:
        return "{:.2f}".format(truncate_to_n_decimal_places(self.area, n=2))

    def to_etree(self) -> etree._Element:
        element = etree.Element(
            self.Meta.element_name,
            unit=self.unit,
            min=str(self.min),
            max=str(self.max),
        )
        element.text = self.format_area()
        return element


@dataclass
class YearOfBuilding(XMLModel):
    original: int
    description: str

    class Meta:
        element_name = "YearOfBuilding"
        case = Case.PASCAL

    def to_etree(self) -> etree._Element:
        element = etree.Element(self.Meta.element_name, original=str(self.original))
        element.text = self.description
        return element


@dataclass
class Apartment(XMLModel):
    action: Optional[ApartmentAction]
    type: ApartmentType
    new_houses: bool
    new_apartment_reserved: Optional[bool]

    key: str
    vendor_identifier: str
    estate: Optional[Estate]
    mode_of_habitation: ModeOfHabitation
    mode_of_financing: Optional[str]
    apartment_city_plan_id: Optional[str]
    hide_building_data: Optional[bool]

    street_address: str
    postal_code: Optional[str]
    other_post_code: Optional[str]
    post_office: Optional[str]
    city: City
    region: Optional[str]
    country: Optional[str]
    latitude: Optional[float]
    longitude: Optional[float]

    oikotie_id: Optional[str]
    title: Optional[str]
    description: Optional[str]
    supplementary_information: Optional[str]
    direction: Optional[str]
    pictures: Optional[List[Picture]]
    picture_gallery_promotion: Optional[str]
    picture_gallery_promotion_url: Optional[str]
    picture_descriptions: Optional[List[PictureDescription]]
    city_plan_pictures: Optional[List[CityPlanPicture]]
    virtual_presentation_url: Optional[str]
    video_presentation_url: Optional[str]
    listing_background_image_url: Optional[str]
    listing_background_color_hex: Optional[str]

    floor_location: Optional[FloorLocation]
    number_of_rooms: Optional[int]
    room_types: Optional[str]
    other_space_description: Optional[str]
    balcony: Optional[str]
    has_terrace: Optional[bool]
    terrace: Optional[str]
    direction_of_windows: Optional[str]
    view: Optional[str]
    cellar: Optional[bool]

    living_area: Optional[LivingArea]
    living_area_type: Optional[LivingAreaType]
    total_area: Optional[TotalArea]
    floor_area: Optional[FloorArea]
    residental_apartment_area: Optional[float]
    office_area: Optional[float]
    estate_area: Optional[str]
    forest_amount: Optional[str]
    land_area: Optional[str]

    real_estate_id: Optional[str]
    real_estate_code: Optional[str]
    housing_company_name: Optional[str]
    housing_company_key: Optional[str]
    business_id: Optional[str]
    disponent: Optional[str]
    real_estate_management: Optional[str]
    number_of_apartments: Optional[str]
    lift: Optional[Lift]

    year_of_building: Optional[YearOfBuilding]
    year_start_of_use: Optional[int]
    basic_renovations: Optional[str]
    renovation_year_facade: Optional[str]
    renovation_year_roof: Optional[str]
    renovation_year_plumbing: Optional[str]
    renovation_year_bathrooms: Optional[str]
    future_renovations: Optional[str]
    future_renovation_year_facade: Optional[str]
    future_renovation_year_roof: Optional[str]
    future_renovation_year_plumbing: Optional[str]
    future_renovation_year_bathrooms: Optional[str]

    heating: Optional[str]
    roof_type: Optional[str]
    building_rights: Optional[str]
    building_rights_amount: Optional[BuildingRightsAmount]
    number_of_offices: Optional[int]

    sanitation: Optional[str]
    water_and_sewage: Optional[str]
    sewer_system: Optional[str]
    use_of_water: Optional[str]
    ventilation_system: Optional[str]
    other_buildings: Optional[str]
    more_estate_information: Optional[str]

    general_condition: Optional[str]
    condition_inspection: Optional[str]

    estate_name_and_number: Optional[str]
    site: Optional[Site]
    site_rent: Optional[str]
    site_rent_contract_end_date: Optional[date]
    site_area: Optional[SiteArea]
    area_description: Optional[str]
    shore: Optional[Shore]
    shores_description: Optional[str]
    shore_direction: Optional[str]
    shore_length: Optional[str]
    waters_description: Optional[str]
    building_plan_information: Optional[str]
    building_plan_situation: Optional[str]
    grounds: Optional[str]
    yard_description: Optional[str]
    yard_direction: Optional[str]

    heating_costs: Optional[HeatingCosts]
    sauna_charge: Optional[SaunaCharge]
    estate_tax: Optional[str]
    housing_company_fee: Optional[HousingCompanyFee]
    financing_fee: Optional[FinancingFee]
    maintenance_fee: Optional[MaintenanceFee]
    water_fee: Optional[WaterFee]
    water_fee_explanation: Optional[str]
    electricity_consumption: Optional[ElectricityConsumption]
    cable_tv_charge: Optional[CableTvCharge]
    road_costs: Optional[str]
    other_fees: Optional[str]
    share_of_debt_85: Optional[Decimal]
    share_of_debt_70: Optional[Decimal]
    charge_fee: Optional[ChargeFee]
    car_parking_charge: Optional[CarParkingCharge]

    building_material: Optional[str]
    foundation: Optional[str]
    wall_construction: Optional[str]
    roof_material: Optional[str]
    floor: Optional[str]
    bedroom_floor: Optional[str]
    kitchen_floor: Optional[str]
    living_room_floor: Optional[str]
    bathroom_floor: Optional[str]
    bedroom_wall: Optional[str]
    kitchen_wall: Optional[str]
    living_room_wall: Optional[str]
    bathroom_wall: Optional[str]
    other_rooms_materials: Optional[str]
    kitchen_appliances: Optional[str]
    bathroom_appliances: Optional[str]
    bedroom_appliances: Optional[str]
    living_room_appliances: Optional[str]
    non_included_appliances: Optional[str]
    other_included_appliances: Optional[str]
    sauna: Optional[Sauna]
    storage_space: Optional[str]
    parking_space: Optional[ParkingSpace]
    car_storage: Optional[str]
    common_areas: Optional[str]
    antenna_system: Optional[str]
    tv_appliances: Optional[str]
    internet_appliances: Optional[str]

    date_when_available: Optional[date]
    becomes_available: Optional[str]
    rent_fixed_term_start: Optional[date]
    rent_fixed_term_end: Optional[date]
    rent_min_length: Optional[str]
    extra_visibility_start_date_time: Optional[datetime]

    rented: Optional[Rented]
    rent_furnished: Optional[RentFurnished]
    municipal_development: Optional[str]
    honoring_clause: Optional[str]
    lease_holder: Optional[str]
    term_of_lease: Optional[str]
    encumbrances: Optional[str]
    mortgages: Optional[str]
    rent_increase: Optional[str]
    renting_terms: Optional[str]
    rent_fixed_term: Optional[RentFixedTerm]

    services: Optional[str]
    connections: Optional[str]
    driving_instructions: Optional[str]

    rent_per_month: Optional[RentPerMonth]
    rent_per_day: Optional[RentPerDay]
    rent_per_week: Optional[RentPerWeek]
    rent_per_year: Optional[RentPerYear]
    rent_per_week_end: Optional[RentPerWeekEnd]
    unencumbered_sales_price: Optional[UnencumberedSalesPrice]
    sales_price: Optional[SalesPrice]
    debt_payable: Optional[DebtPayable]
    redemption_price: Optional[RedemptionPrice]
    buyer_costs: Optional[str]
    apartment_rent_income: Optional[Decimal]
    rent_comission: Optional[RentComission]
    rent_security_deposit: Optional[str]
    rent_security_deposit2: Optional[RentSecurityDeposit2]
    financing_offer1: Optional[FinancingOffer1]
    financing_offer2: Optional[FinancingOffer2]
    site_repurchase_price: Optional[Decimal]
    site_condominium_fee: Optional[Decimal]

    magazine_identifier: Optional[str]
    print_media_text: Optional[str]

    estate_agent_contact_person: Optional[str]
    estate_agent_email: Optional[str]
    estate_agent_telephone: Optional[str]
    estate_agent_title: Optional[str]
    estate_agent_degrees: Optional[str]
    estate_agent_rating: Optional[EstateAgentRating]
    estate_agent_social_media: Optional[EstateAgentSocialMedia]
    estate_agent_contact_person_picture_url: Optional[str]

    inquiries: Optional[str]
    showing_date1: Optional[ShowingDate1]
    showing_start_time1: Optional[str]
    showing_end_time1: Optional[str]
    showing_date_explanation1: Optional[str]
    showing_date2: Optional[date]
    showing_start_time2: Optional[str]
    showing_end_time2: Optional[str]
    showing_date_explanation2: Optional[str]
    contact_request_email: Optional[str]
    electronic_brochure_request_email: Optional[str]
    electronic_brochure_request_url: Optional[str]
    application_url: Optional[str]
    show_lead_form: Optional[bool]

    more_info_url: Optional[str]
    attachments: Optional[Attachments]
    campaign_link: Optional[CampaignLink]
    banner_html: Optional[str]
    promotional_offer: Optional[PromotionalOffer]
    promotional_offer_title: Optional[str]
    promotional_offer_description: Optional[str]
    promotional_offer_url: Optional[str]
    promotional_offer_url_text: Optional[str]
    promotional_offer_logo: Optional[str]
    promotional_offer_color: Optional[str]
    online_offer: Optional[bool]
    online_offer_logo: Optional[str]
    online_offer_url: Optional[str]
    online_offer_highest_bid: Optional[Decimal]
    online_offer_label: Optional[OnlineOfferLabel]
    online_offer_search_logo: Optional[str]
    rc_energy_flag: Optional[str]
    rc_energyclass: Optional[str]
    rc_wastewater_flag: Optional[str]

    estate_division: Optional[str]

    new_development_status: Optional[NewDevelopmentStatus]
    time_of_completion: Optional[date]

    class Meta:
        element_name = "Apartment"
        case = Case.PASCAL
        case_overrides = {
            "action": Case.CAMEL,
            "type": Case.CAMEL,
            "new_houses": Case.CAMEL,
            "new_apartment_reserved": Case.CAMEL,
            "rc_energy_flag": Case.KEBAB,
            "rc_energyclass": Case.KEBAB,
            "rc_wastewater_flag": Case.KEBAB,
        }
        element_name_overrides = {
            "oikotie_id": "OikotieID",
            "real_estate_id": "RealEstateID",
        }
        attributes = ["action", "type", "new_houses" "new_apartment_reserved"]

    def format_pictures(self) -> Generator[etree._Element, None, None]:
        for picture in self.pictures:
            yield picture.to_etree()

    def format_picture_descriptions(self) -> Generator[etree._Element, None, None]:
        for picture_description in self.picture_descriptions:
            yield picture_description.to_etree()

    def format_city_plan_pictures(self) -> Generator[etree._Element, None, None]:
        for city_plan_picture in self.city_plan_pictures:
            yield city_plan_picture.to_etree()

    def format_new_houses(self) -> str:
        return yes_no_bool(self.new_houses)

    def format_new_apartment_reserved(self) -> str:
        return yes_no_bool(self.new_apartment_reserved)

    def format_hide_building_data(self) -> str:
        return yes_no_bool(self.hide_building_data)

    def format_latitude(self) -> str:
        return "{:.5f}".format(truncate_to_n_decimal_places(self.latitude, n=5))

    def format_longitude(self) -> str:
        return "{:.5f}".format(truncate_to_n_decimal_places(self.longitude, n=5))

    def format_has_terrace(self) -> str:
        return yes_no_bool(self.has_terrace)

    def format_cellar(self) -> str:
        return yes_no_bool(self.cellar)

    def format_residental_apartment_area(self) -> str:
        return str(truncate_to_n_decimal_places(self.residental_apartment_area, n=2))

    def format_office_area(self) -> str:
        return str(truncate_to_n_decimal_places(self.office_area, n=2))

    def format_site_rent_contract_end_date(self) -> str:
        return self.site_rent_contract_end_date.strftime("%d.%m.%Y")

    def format_share_of_debt_85(self) -> str:
        return str(truncate_to_n_decimal_places(self.share_of_debt_85, n=2))

    def format_share_of_debt_70(self) -> str:
        return str(truncate_to_n_decimal_places(self.share_of_debt_70, n=2))

    def format_date_when_available(self) -> str:
        return self.date_when_available.strftime("%d.%m.%Y")

    def format_rent_fixed_term_start(self) -> str:
        return self.rent_fixed_term_start.strftime("%d.%m.%Y")

    def format_rent_fixed_term_end(self) -> str:
        return self.rent_fixed_term_end.strftime("%d.%m.%Y")

    def format_extra_visibility_start_date_time(self) -> str:
        return self.extra_visibility_start_date_time.strftime("%Y-%m-%dT%H:%M:%S")

    def format_apartment_rent_income(self) -> str:
        return str(truncate_to_n_decimal_places(self.apartment_rent_income, n=2))

    def format_site_repurchase_price(self) -> str:
        return str(truncate_to_n_decimal_places(self.site_repurchase_price, n=2))

    def format_site_condominium_fee(self) -> str:
        return str(truncate_to_n_decimal_places(self.site_condominium_fee, n=2))

    def format_showing_date2(self) -> str:
        return self.showing_date2.strftime("%d.%m.%Y")

    def format_online_offer_highest_bid(self) -> str:
        return str(truncate_to_n_decimal_places(self.online_offer_highest_bid, n=2))

    def format_time_of_completion(self) -> str:
        return self.time_of_completion.strftime("%d.%m.%Y")

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
class _BoolAttrValueModel(XMLModel):
    value: bool

    class Meta:
        case = Case.CAMEL
        attributes = ["value"]

    def format_value(self) -> str:
        return yes_no_bool(self.value)


@dataclass
class PromotionalOffer(_BoolAttrValueModel):
    class Meta(_BoolAttrValueModel.Meta):
        element_name = "PromotionalOffer"


@dataclass
class Rented(_BoolAttrValueModel):
    class Meta(_BoolAttrValueModel.Meta):
        element_name = "Rented"


@dataclass
class RentFixedTerm(_BoolAttrValueModel):
    class Meta(_BoolAttrValueModel.Meta):
        element_name = "RentFixedTerm"


@dataclass
class RentFurnished(_BoolAttrValueModel):
    class Meta(_BoolAttrValueModel.Meta):
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
    min: Optional[int] = None
    max: Optional[int] = None

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
    type: ApartmentType
    new_houses: bool
    key: str
    vendor_identifier: str
    mode_of_habitation: ModeOfHabitation
    street_address: str
    city: City

    action: Optional[ApartmentAction] = None
    new_apartment_reserved: Optional[bool] = None

    estate: Optional[Estate] = None
    mode_of_financing: Optional[str] = None
    apartment_city_plan_id: Optional[str] = None
    hide_building_data: Optional[bool] = None

    postal_code: Optional[str] = None
    other_post_code: Optional[str] = None
    post_office: Optional[str] = None
    region: Optional[str] = None
    country: Optional[str] = None
    latitude: Optional[float] = None
    longitude: Optional[float] = None

    oikotie_id: Optional[str] = None
    title: Optional[str] = None
    description: Optional[str] = None
    supplementary_information: Optional[str] = None
    direction: Optional[str] = None
    pictures: Optional[List[Picture]] = None
    picture_gallery_promotion: Optional[str] = None
    picture_gallery_promotion_url: Optional[str] = None
    picture_descriptions: Optional[List[PictureDescription]] = None
    city_plan_pictures: Optional[List[CityPlanPicture]] = None
    virtual_presentation_url: Optional[str] = None
    video_presentation_url: Optional[str] = None
    listing_background_image_url: Optional[str] = None
    listing_background_color_hex: Optional[str] = None

    floor_location: Optional[FloorLocation] = None
    number_of_rooms: Optional[int] = None
    room_types: Optional[str] = None
    other_space_description: Optional[str] = None
    balcony: Optional[str] = None
    has_terrace: Optional[bool] = None
    terrace: Optional[str] = None
    direction_of_windows: Optional[str] = None
    view: Optional[str] = None
    cellar: Optional[bool] = None

    living_area: Optional[LivingArea] = None
    living_area_type: Optional[LivingAreaType] = None
    total_area: Optional[TotalArea] = None
    floor_area: Optional[FloorArea] = None
    residental_apartment_area: Optional[float] = None
    office_area: Optional[float] = None
    estate_area: Optional[str] = None
    forest_amount: Optional[str] = None
    land_area: Optional[str] = None

    real_estate_id: Optional[str] = None
    real_estate_code: Optional[str] = None
    housing_company_name: Optional[str] = None
    housing_company_key: Optional[str] = None
    business_id: Optional[str] = None
    disponent: Optional[str] = None
    real_estate_management: Optional[str] = None
    number_of_apartments: Optional[str] = None
    lift: Optional[Lift] = None

    year_of_building: Optional[YearOfBuilding] = None
    year_start_of_use: Optional[int] = None
    basic_renovations: Optional[str] = None
    renovation_year_facade: Optional[str] = None
    renovation_year_roof: Optional[str] = None
    renovation_year_plumbing: Optional[str] = None
    renovation_year_bathrooms: Optional[str] = None
    future_renovations: Optional[str] = None
    future_renovation_year_facade: Optional[str] = None
    future_renovation_year_roof: Optional[str] = None
    future_renovation_year_plumbing: Optional[str] = None
    future_renovation_year_bathrooms: Optional[str] = None

    heating: Optional[str] = None
    roof_type: Optional[str] = None
    building_rights: Optional[str] = None
    building_rights_amount: Optional[BuildingRightsAmount] = None
    number_of_offices: Optional[int] = None

    sanitation: Optional[str] = None
    water_and_sewage: Optional[str] = None
    sewer_system: Optional[str] = None
    use_of_water: Optional[str] = None
    ventilation_system: Optional[str] = None
    other_buildings: Optional[str] = None
    more_estate_information: Optional[str] = None

    general_condition: Optional[str] = None
    condition_inspection: Optional[str] = None

    estate_name_and_number: Optional[str] = None
    site: Optional[Site] = None
    site_rent: Optional[str] = None
    site_rent_contract_end_date: Optional[date] = None
    site_area: Optional[SiteArea] = None
    area_description: Optional[str] = None
    shore: Optional[Shore] = None
    shores_description: Optional[str] = None
    shore_direction: Optional[str] = None
    shore_length: Optional[str] = None
    waters_description: Optional[str] = None
    building_plan_information: Optional[str] = None
    building_plan_situation: Optional[str] = None
    grounds: Optional[str] = None
    yard_description: Optional[str] = None
    yard_direction: Optional[str] = None

    heating_costs: Optional[HeatingCosts] = None
    sauna_charge: Optional[SaunaCharge] = None
    estate_tax: Optional[str] = None
    housing_company_fee: Optional[HousingCompanyFee] = None
    financing_fee: Optional[FinancingFee] = None
    maintenance_fee: Optional[MaintenanceFee] = None
    water_fee: Optional[WaterFee] = None
    water_fee_explanation: Optional[str] = None
    electricity_consumption: Optional[ElectricityConsumption] = None
    cable_tv_charge: Optional[CableTvCharge] = None
    road_costs: Optional[str] = None
    other_fees: Optional[str] = None
    share_of_debt_85: Optional[Decimal] = None
    share_of_debt_70: Optional[Decimal] = None
    charge_fee: Optional[ChargeFee] = None
    car_parking_charge: Optional[CarParkingCharge] = None

    building_material: Optional[str] = None
    foundation: Optional[str] = None
    wall_construction: Optional[str] = None
    roof_material: Optional[str] = None
    floor: Optional[str] = None
    bedroom_floor: Optional[str] = None
    kitchen_floor: Optional[str] = None
    living_room_floor: Optional[str] = None
    bathroom_floor: Optional[str] = None
    bedroom_wall: Optional[str] = None
    kitchen_wall: Optional[str] = None
    living_room_wall: Optional[str] = None
    bathroom_wall: Optional[str] = None
    other_rooms_materials: Optional[str] = None
    kitchen_appliances: Optional[str] = None
    bathroom_appliances: Optional[str] = None
    bedroom_appliances: Optional[str] = None
    living_room_appliances: Optional[str] = None
    non_included_appliances: Optional[str] = None
    other_included_appliances: Optional[str] = None
    sauna: Optional[Sauna] = None
    storage_space: Optional[str] = None
    parking_space: Optional[ParkingSpace] = None
    car_storage: Optional[str] = None
    common_areas: Optional[str] = None
    antenna_system: Optional[str] = None
    tv_appliances: Optional[str] = None
    internet_appliances: Optional[str] = None

    date_when_available: Optional[date] = None
    becomes_available: Optional[str] = None
    rent_fixed_term_start: Optional[date] = None
    rent_fixed_term_end: Optional[date] = None
    rent_min_length: Optional[str] = None
    extra_visibility_start_date_time: Optional[datetime] = None

    rented: Optional[Rented] = None
    rent_furnished: Optional[RentFurnished] = None
    municipal_development: Optional[str] = None
    honoring_clause: Optional[str] = None
    lease_holder: Optional[str] = None
    term_of_lease: Optional[str] = None
    encumbrances: Optional[str] = None
    mortgages: Optional[str] = None
    rent_increase: Optional[str] = None
    renting_terms: Optional[str] = None
    rent_fixed_term: Optional[RentFixedTerm] = None

    services: Optional[str] = None
    connections: Optional[str] = None
    driving_instructions: Optional[str] = None

    rent_per_month: Optional[RentPerMonth] = None
    rent_per_day: Optional[RentPerDay] = None
    rent_per_week: Optional[RentPerWeek] = None
    rent_per_year: Optional[RentPerYear] = None
    rent_per_week_end: Optional[RentPerWeekEnd] = None
    unencumbered_sales_price: Optional[UnencumberedSalesPrice] = None
    sales_price: Optional[SalesPrice] = None
    debt_payable: Optional[DebtPayable] = None
    redemption_price: Optional[RedemptionPrice] = None
    buyer_costs: Optional[str] = None
    apartment_rent_income: Optional[Decimal] = None
    rent_comission: Optional[RentComission] = None
    rent_security_deposit: Optional[str] = None
    rent_security_deposit2: Optional[RentSecurityDeposit2] = None
    financing_offer1: Optional[FinancingOffer1] = None
    financing_offer2: Optional[FinancingOffer2] = None
    site_repurchase_price: Optional[Decimal] = None
    site_condominium_fee: Optional[Decimal] = None

    magazine_identifier: Optional[str] = None
    print_media_text: Optional[str] = None

    estate_agent_contact_person: Optional[str] = None
    estate_agent_email: Optional[str] = None
    estate_agent_telephone: Optional[str] = None
    estate_agent_title: Optional[str] = None
    estate_agent_degrees: Optional[str] = None
    estate_agent_rating: Optional[EstateAgentRating] = None
    estate_agent_social_media: Optional[EstateAgentSocialMedia] = None
    estate_agent_contact_person_picture_url: Optional[str] = None

    inquiries: Optional[str] = None
    showing_date1: Optional[ShowingDate1] = None
    showing_start_time1: Optional[str] = None
    showing_end_time1: Optional[str] = None
    showing_date_explanation1: Optional[str] = None
    showing_date2: Optional[date] = None
    showing_start_time2: Optional[str] = None
    showing_end_time2: Optional[str] = None
    showing_date_explanation2: Optional[str] = None
    contact_request_email: Optional[str] = None
    electronic_brochure_request_email: Optional[str] = None
    electronic_brochure_request_url: Optional[str] = None
    application_url: Optional[str] = None
    show_lead_form: Optional[bool] = None

    more_info_url: Optional[str] = None
    attachments: Optional[Attachments] = None
    campaign_link: Optional[CampaignLink] = None
    banner_html: Optional[str] = None
    promotional_offer: Optional[PromotionalOffer] = None
    promotional_offer_title: Optional[str] = None
    promotional_offer_description: Optional[str] = None
    promotional_offer_url: Optional[str] = None
    promotional_offer_url_text: Optional[str] = None
    promotional_offer_logo: Optional[str] = None
    promotional_offer_color: Optional[str] = None
    online_offer: Optional[bool] = None
    online_offer_logo: Optional[str] = None
    online_offer_url: Optional[str] = None
    online_offer_highest_bid: Optional[Decimal] = None
    online_offer_label: Optional[OnlineOfferLabel] = None
    online_offer_search_logo: Optional[str] = None
    rc_energy_flag: Optional[str] = None
    rc_energyclass: Optional[str] = None
    rc_wastewater_flag: Optional[str] = None

    estate_division: Optional[str] = None

    new_development_status: Optional[NewDevelopmentStatus] = None
    time_of_completion: Optional[date] = None

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
        attributes = ["action", "type", "new_houses", "new_apartment_reserved"]

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

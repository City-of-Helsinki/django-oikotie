# ruff: noqa: E501

from datetime import date, datetime
from decimal import Decimal
from os import path

import pytest
from django.test import override_settings

from django_oikotie.oikotie import create_apartments

from .factories.apartment import (ApartmentFactory, AttachmentsFactory,
                                  BalconyFactory, BuildingRightsAmountFactory,
                                  CableTvChargeFactory, CampaignLinkFactory,
                                  CarParkingChargeFactory, ChargeFeeFactory,
                                  CityFactory, CityPlanPictureFactory,
                                  DebtPayableFactory,
                                  ElectricityConsumptionChargeFactory,
                                  EstateAgentRatingFactory,
                                  EstateAgentSocialMediaFactory, EstateFactory,
                                  FinancingFeeFactory, FinancingOffer1Factory,
                                  FinancingOffer2Factory, FloorAreaFactory,
                                  FloorLocationFactory,
                                  GeneralConditionFactory, HeatingCostsFactory,
                                  HousingCompanyFeeFactory, LiftFactory,
                                  LivingAreaFactory, MaintenanceFeeFactory,
                                  MinimalApartmentFactory,
                                  ModeOfHabitationFactory,
                                  NewDevelopmentStatusFactory,
                                  OnlineOfferLabelFactory, ParkingSpaceFactory,
                                  PictureDescriptionFactory, PictureFactory,
                                  PromotionalOfferFactory,
                                  RedemptionPriceFactory, RentComissionFactory,
                                  RentedFactory, RentFixedTermFactory,
                                  RentFurnishedFactory, RentPerDayFactory,
                                  RentPerMonthFactory, RentPerWeekEndFactory,
                                  RentPerWeekFactory, RentPerYearFactory,
                                  RentSecurityDeposit2Factory,
                                  SalesPriceFactory, SaunaChargeFactory,
                                  SaunaFactory, ShoreFactory,
                                  ShowingDate1Factory, SiteAreaFactory,
                                  SiteFactory, TotalAreaFactory,
                                  UnencumberedSalesPriceFactory,
                                  WaterFeeFactory, YearOfBuildingFactory)
from .utils import obj_to_xml_str


def test__apartment__xml_serialization_does_not_crash():
    obj = ApartmentFactory()
    xml = obj_to_xml_str(obj)
    assert "<Apartment" in xml
    assert "</Apartment>" in xml


@pytest.mark.parametrize(
    "factory,element_name",
    (
        (CableTvChargeFactory, "CableTvCharge"),
        (CarParkingChargeFactory, "CarParkingCharge"),
        (ChargeFeeFactory, "ChargeFee"),
        (ElectricityConsumptionChargeFactory, "ElectricityConsumptionCharge"),
        (FinancingFeeFactory, "FinancingFee"),
        (HeatingCostsFactory, "HeatingCosts"),
        (HousingCompanyFeeFactory, "HousingCompanyFee"),
        (MaintenanceFeeFactory, "MaintenanceFee"),
        (RentPerDayFactory, "RentPerDay"),
        (RentPerMonthFactory, "RentPerMonth"),
        (RentPerWeekFactory, "RentPerWeek"),
        (RentPerWeekEndFactory, "RentPerWeekEnd"),
        (RentPerYearFactory, "RentPerYear"),
        (SaunaChargeFactory, "SaunaCharge"),
        (WaterFeeFactory, "WaterFee"),
    ),
)
def test__cost_model__xml_serialization(factory, element_name):
    obj = factory(value=Decimal("1.2345"), unit="EUR/kk")
    xml = obj_to_xml_str(obj)
    assert xml == f'<{element_name} unit="EUR/kk">1.23</{element_name}>\n'


@pytest.mark.parametrize(
    "factory,element_name",
    (
        (RedemptionPriceFactory, "RedemptionPrice"),
        (RentComissionFactory, "RentComission"),
        (SalesPriceFactory, "SalesPrice"),
        (UnencumberedSalesPriceFactory, "UnencumberedSalesPrice"),
    ),
)
def test__price_model__xml_serialization(factory, element_name):
    obj = factory(value=Decimal("1.2345"), currency="EUR")
    xml = obj_to_xml_str(obj)
    assert xml == f'<{element_name} currency="EUR">1.23</{element_name}>\n'


def test__attachments__xml_serialization():
    obj = AttachmentsFactory()
    xml = obj_to_xml_str(obj)
    assert xml == f'<Attachments url="{obj.url}">{obj.link_text}</Attachments>\n'


def test__balcony__xml_serialization():
    obj = BalconyFactory(value=True)
    xml = obj_to_xml_str(obj)
    assert xml == f'<Balcony value="K">{obj.description}</Balcony>\n'


def test__building_rights_amount__xml_serialization():
    obj = BuildingRightsAmountFactory(amount=1.2345)
    xml = obj_to_xml_str(obj)
    assert xml == (
        f'<BuildingRightsAmount type="{obj.type.value}">1.23</BuildingRightsAmount>\n'
    )


def test__campaign_link__xml_serialization():
    obj = CampaignLinkFactory()
    xml = obj_to_xml_str(obj)
    assert xml == (
        f'<CampaignLink targetUrl="{obj.target_url}" pictureUrl="{obj.picture_url}"/>\n'
    )


def test__city__xml_serialization():
    obj = CityFactory()
    xml = obj_to_xml_str(obj)
    assert xml == f'<City id="{obj.id}">{obj.value}</City>\n'


def test__city_plan_picture__xml_serialization():
    obj = CityPlanPictureFactory(index=1)
    xml = obj_to_xml_str(obj)
    assert xml == f"<CityPlanPicture1>{obj.url}</CityPlanPicture1>\n"


def test__debt_payable__xml_serialization():
    obj = DebtPayableFactory(value=False)
    xml = obj_to_xml_str(obj)
    assert xml == '<DebtPayable value="E"/>\n'


def test__estate__xml_serialization():
    obj = EstateFactory()
    xml = obj_to_xml_str(obj)
    assert xml == f'<Estate type="{obj.type.value}"/>\n'


def test__estate_agent_rating__xml_serialization():
    obj = EstateAgentRatingFactory()
    xml = obj_to_xml_str(obj)
    assert xml == f'<EstateAgentRating value="{obj.value}"/>\n'


def test__estate_agent_social_media__xml_serialization():
    obj = EstateAgentSocialMediaFactory()
    xml = obj_to_xml_str(obj)
    assert xml == (
        f'<EstateAgentSocialMedia url="{obj.url}">{obj.description}</EstateAgentSocialMedia>\n'
    )


@pytest.mark.parametrize(
    "factory,element_name",
    (
        (FinancingOffer1Factory, "FinancingOffer1"),
        (FinancingOffer2Factory, "FinancingOffer2"),
    ),
)
def test__financing_offer__xml_serialization(factory, element_name):
    obj = factory()
    xml = obj_to_xml_str(obj)
    assert xml == (
        f'<{element_name} percentage="{obj.percentage}" price="{obj.price}" fee="{obj.fee}"/>\n'
    )


def test__floor_area__xml_serialization():
    obj = FloorAreaFactory(area=123.45678)
    xml = obj_to_xml_str(obj)
    assert xml == f'<FloorArea unit="{obj.unit}">123.45</FloorArea>\n'


def test__floor_location__xml_serialization():
    obj = FloorLocationFactory(high=True, low=False)
    xml = obj_to_xml_str(obj)
    assert xml == (
        f'<FloorLocation high="K" low="E" number="{obj.number}" count="{obj.count}">'
        f"{obj.description}"
        f"</FloorLocation>\n"
    )


def test__general_condition__xml_serialization():
    obj = GeneralConditionFactory()
    xml = obj_to_xml_str(obj)
    assert xml == (
        f'<GeneralCondition level="{obj.level.value}">{obj.description}</GeneralCondition>\n'
    )


def test__lift__xml_serialization():
    obj = LiftFactory(value=True)
    xml = obj_to_xml_str(obj)
    assert xml == f'<Lift value="K">{obj.description}</Lift>\n'


def test__living_area__xml_serialization():
    obj = LivingAreaFactory(area=123.4567)
    xml = obj_to_xml_str(obj)
    assert xml == f'<LivingArea unit="{obj.unit}">123.45</LivingArea>\n'


def test__mode_of_habitation__xml_serialization():
    obj = ModeOfHabitationFactory()
    xml = obj_to_xml_str(obj)
    assert xml == (
        f'<ModeOfHabitation type="{obj.type.value}" rentType="{obj.rent_type.value}"/>\n'
    )


def test__new_development_status__xml_serialization():
    obj = NewDevelopmentStatusFactory()
    xml = obj_to_xml_str(obj)
    assert xml == f'<NewDevelopmentStatus value="{obj.value.value}"/>\n'


def test__online_offer_label__xml_serialization():
    obj = OnlineOfferLabelFactory()
    xml = obj_to_xml_str(obj)
    assert xml == (
        f'<OnlineOfferLabel backgroundColor="{obj.background_color}" textColor="{obj.text_color}">'
        f"{obj.text_value}"
        f"</OnlineOfferLabel>\n"
    )


def test__parking_space__xml_serialization():
    obj = ParkingSpaceFactory(electricity_outlet=True)
    xml = obj_to_xml_str(obj)
    assert xml == (
        f'<ParkingSpace type="{obj.type.value}" heated="{obj.heated.value}" electricityOutlet="K">'
        f"{obj.text_value}"
        f"</ParkingSpace>\n"
    )


def test__picture__xml_serialization():
    obj = PictureFactory(is_floor_plan=True)
    xml = obj_to_xml_str(obj)
    assert xml == (
        f'<Picture{obj.index} isFloorPlan="K">{obj.url}</Picture{obj.index}>\n'
    )


def test__picture_description__xml_serialization():
    obj = PictureDescriptionFactory()
    xml = obj_to_xml_str(obj)
    assert xml == (
        f"<Picture{obj.index}Description>{obj.description}</Picture{obj.index}Description>\n"
    )


@pytest.mark.parametrize(
    "factory,element_name,value,expected_value",
    (
        (PromotionalOfferFactory, "PromotionalOffer", True, "K"),
        (PromotionalOfferFactory, "PromotionalOffer", False, "E"),
        (RentedFactory, "Rented", True, "K"),
        (RentedFactory, "Rented", False, "E"),
        (RentFixedTermFactory, "RentFixedTerm", True, "K"),
        (RentFixedTermFactory, "RentFixedTerm", False, "E"),
        (RentFurnishedFactory, "RentFurnished", True, "K"),
        (RentFurnishedFactory, "RentFurnished", False, "E"),
    ),
)
def test__value_attr_model__xml_serialization(
    factory, element_name, value, expected_value
):
    obj = factory(value=value)
    xml = obj_to_xml_str(obj)
    assert xml == f'<{element_name} value="{expected_value}"/>\n'


def test__rent_security_deposit_2__xml_serialization():
    obj = RentSecurityDeposit2Factory(value=123.4567)
    xml = obj_to_xml_str(obj)
    assert xml == (
        f'<RentSecurityDeposit2 currency="{obj.currency}">123.45</RentSecurityDeposit2>\n'
    )


def test__sauna__xml_serialisation():
    obj = SaunaFactory(own=True, common=False)
    xml = obj_to_xml_str(obj)
    assert xml == f'<Sauna own="K" common="E">{obj.description}</Sauna>\n'


def test__shore__xml_serialization():
    obj = ShoreFactory()
    xml = obj_to_xml_str(obj)
    assert xml == f'<Shore type="{obj.type.value}"/>\n'


def test__showing_date_1__xml_serialization():
    obj = ShowingDate1Factory(first_showing=True, value=date(2020, 1, 1))
    xml = obj_to_xml_str(obj)
    assert xml == '<ShowingDate1 firstShowing="K">01.01.2020</ShowingDate1>\n'


def test__site__xml_serialization():
    obj = SiteFactory()
    xml = obj_to_xml_str(obj)
    assert xml == f'<Site type="{obj.type.value}"/>\n'


def test__site_area__xml_serialization():
    obj = SiteAreaFactory(area=123.4567)
    xml = obj_to_xml_str(obj)
    assert xml == f'<SiteArea unit="{obj.unit}">123.45</SiteArea>\n'


def test__total_area__xml_serialization():
    obj = TotalAreaFactory(area=123.4567)
    xml = obj_to_xml_str(obj)
    assert xml == (
        f'<TotalArea unit="{obj.unit}" min="{obj.min}" max="{obj.max}">123.45</TotalArea>\n'
    )


def test__year_of_building__xml_serialization():
    obj = YearOfBuildingFactory()
    xml = obj_to_xml_str(obj)
    assert xml == (
        f'<YearOfBuilding original="{obj.original}">{obj.description}</YearOfBuilding>\n'
    )


def test__apartment__minimal_xml_serialization():
    moh = ModeOfHabitationFactory()
    obj = MinimalApartmentFactory(new_houses=False, mode_of_habitation=moh)
    xml = obj_to_xml_str(obj)
    assert xml == (
        f'<Apartment type="{obj.type.value}" newHouses="E">\n'
        f"  <Key>{obj.key}</Key>\n"
        f"  <VendorIdentifier>{obj.vendor_identifier}</VendorIdentifier>\n"
        f'  <ModeOfHabitation type="{moh.type.value}" rentType="{moh.rent_type.value}"/>\n'
        f"  <StreetAddress>{obj.street_address}</StreetAddress>\n"
        f'  <City id="{obj.city.id}">{obj.city.value}</City>\n'
        f"</Apartment>\n"
    )


def test__apartment__complete_xml_serialization():
    moh = ModeOfHabitationFactory()
    pic1 = PictureFactory(index=1, is_floor_plan=True)
    pic2 = PictureFactory(index=2, is_floor_plan=False)
    pd1 = PictureDescriptionFactory(index=1)
    pd2 = PictureDescriptionFactory(index=2)
    cpp1 = CityPlanPictureFactory(index=1)
    cpp2 = CityPlanPictureFactory(index=2)
    fl = FloorLocationFactory(low=False, high=False)
    bal = BalconyFactory(value=False)
    la = LivingAreaFactory(area=123.4567)
    ta = TotalAreaFactory(area=123.4567)
    fa = FloorAreaFactory(area=123.4567)
    lift = LiftFactory(value=True)
    yob = YearOfBuildingFactory()
    bra = BuildingRightsAmountFactory(amount=123.4567)
    gen = GeneralConditionFactory()
    sa = SiteAreaFactory(area=123.4567)
    hc = HeatingCostsFactory(value=123.4567)
    sc = SaunaChargeFactory(value=123.4567)
    hcf = HousingCompanyFeeFactory(value=123.4567)
    ff = FinancingFeeFactory(value=123.4567)
    mf = MaintenanceFeeFactory(value=123.4567)
    wf = WaterFeeFactory(value=123.4567)
    ec = ElectricityConsumptionChargeFactory(value=123.4567)
    ctc = CableTvChargeFactory(value=123.4567)
    cf = ChargeFeeFactory(value=123.4567)
    cpc = CarParkingChargeFactory(value=123.4567)
    sauna = SaunaFactory(own=True, common=False)
    ps = ParkingSpaceFactory(electricity_outlet=True)
    rented = RentedFactory(value=True)
    rf = RentFurnishedFactory(value=False)
    rft = RentFixedTermFactory(value=False)
    rpm = RentPerMonthFactory(value=123.4567)
    rpd = RentPerDayFactory(value=123.4567)
    rpw = RentPerWeekFactory(value=123.4567)
    rpy = RentPerYearFactory(value=123.4567)
    rpwe = RentPerWeekEndFactory(value=123.4567)
    usp = UnencumberedSalesPriceFactory(value=123.4567)
    sp = SalesPriceFactory(value=123.4567)
    dp = DebtPayableFactory(value=True)
    rp = RedemptionPriceFactory(value=123.4567)
    rc = RentComissionFactory(value=123.4567)
    rsd2 = RentSecurityDeposit2Factory(value=123.4567)
    fo1 = FinancingOffer1Factory()
    fo2 = FinancingOffer2Factory()
    ear = EstateAgentRatingFactory()
    easm = EstateAgentSocialMediaFactory()
    sd1 = ShowingDate1Factory(value=date(2020, 1, 1), first_showing=True)
    att = AttachmentsFactory()
    cl = CampaignLinkFactory()
    po = PromotionalOfferFactory(value=False)
    ool = OnlineOfferLabelFactory()
    nds = NewDevelopmentStatusFactory()

    obj = ApartmentFactory(
        new_houses=False,
        mode_of_habitation=moh,
        new_apartment_reserved=True,
        hide_building_data=False,
        latitude=60.1733244,
        longitude=24.9410248,
        pictures=[pic1, pic2],
        picture_descriptions=[pd1, pd2],
        city_plan_pictures=[cpp1, cpp2],
        floor_location=fl,
        balcony=bal,
        cellar=True,
        living_area=la,
        total_area=ta,
        floor_area=fa,
        residental_apartment_area=123.4567,
        office_area=123.4567,
        lift=lift,
        year_of_building=yob,
        building_rights_amount=bra,
        general_condition=gen,
        site_rent_contract_end_date=date(2020, 1, 1),
        site_area=sa,
        heating_costs=hc,
        sauna_charge=sc,
        housing_company_fee=hcf,
        financing_fee=ff,
        maintenance_fee=mf,
        water_fee=wf,
        electricity_consumption_charge=ec,
        cable_tv_charge=ctc,
        charge_fee=cf,
        car_parking_charge=cpc,
        share_of_debt_85=Decimal("123.4567"),
        share_of_debt_70=Decimal("123.4567"),
        sauna=sauna,
        parking_space=ps,
        date_when_available=date(2020, 1, 1),
        rent_fixed_term_start=date(2020, 1, 1),
        rent_fixed_term_end=date(2020, 1, 1),
        extra_visibility_start_date_time=datetime(2020, 1, 1, 12, 0, 0),
        rented=rented,
        rent_furnished=rf,
        rent_fixed_term=rft,
        rent_per_month=rpm,
        rent_per_day=rpd,
        rent_per_week=rpw,
        rent_per_year=rpy,
        rent_per_week_end=rpwe,
        unencumbered_sales_price=usp,
        sales_price=sp,
        debt_payable=dp,
        redemption_price=rp,
        rent_comission=rc,
        rent_security_deposit2=rsd2,
        financing_offer1=fo1,
        financing_offer2=fo2,
        estate_agent_rating=ear,
        estate_agent_social_media=easm,
        apartment_rent_income=123.4567,
        site_repurchase_price=Decimal("123.4567"),
        site_condominium_fee=Decimal("123.4567"),
        showing_date1=sd1,
        showing_date2=date(2020, 1, 1),
        show_lead_form=True,
        attachments=att,
        campaign_link=cl,
        promotional_offer=po,
        online_offer=True,
        online_offer_highest_bid=Decimal("123.4567"),
        online_offer_label=ool,
        new_development_status=nds,
        time_of_completion=date(2020, 1, 1),
    )
    xml = obj_to_xml_str(obj)
    assert xml == (
        f'<Apartment type="{obj.type.value}" newHouses="E" action="{obj.action.value}" newApartmentReserved="K">\n'
        f"  <Key>{obj.key}</Key>\n"
        f"  <VendorIdentifier>{obj.vendor_identifier}</VendorIdentifier>\n"
        f'  <ModeOfHabitation type="{moh.type.value}" rentType="{moh.rent_type.value}"/>\n'
        f"  <StreetAddress>{obj.street_address}</StreetAddress>\n"
        f'  <City id="{obj.city.id}">{obj.city.value}</City>\n'
        f'  <Estate type="{obj.estate.type.value}"/>\n'
        f"  <ModeOfFinancing>{obj.mode_of_financing}</ModeOfFinancing>\n"
        f"  <ApartmentCityPlanId>{obj.apartment_city_plan_id}</ApartmentCityPlanId>\n"
        f"  <HideBuildingData>E</HideBuildingData>\n"
        f"  <PostalCode>{obj.postal_code}</PostalCode>\n"
        f"  <OtherPostCode>{obj.other_post_code}</OtherPostCode>\n"
        f"  <PostOffice>{obj.post_office}</PostOffice>\n"
        f"  <Region>{obj.region}</Region>\n"
        f"  <Country>{obj.country}</Country>\n"
        f"  <Latitude>60.17332</Latitude>\n"
        f"  <Longitude>24.94102</Longitude>\n"
        f"  <OikotieID>{obj.oikotie_id}</OikotieID>\n"
        f"  <Title>{obj.title}</Title>\n"
        f"  <Description>{obj.description}</Description>\n"
        f"  <SupplementaryInformation>{obj.supplementary_information}</SupplementaryInformation>\n"
        f"  <Direction>{obj.direction}</Direction>\n"
        f'  <Picture1 isFloorPlan="K">{pic1.url}</Picture1>\n'
        f'  <Picture2 isFloorPlan="E">{pic2.url}</Picture2>\n'
        f"  <PictureGalleryPromotion>{obj.picture_gallery_promotion}</PictureGalleryPromotion>\n"
        f"  <PictureGalleryPromotionUrl>{obj.picture_gallery_promotion_url}</PictureGalleryPromotionUrl>\n"
        f"  <Picture1Description>{pd1.description}</Picture1Description>\n"
        f"  <Picture2Description>{pd2.description}</Picture2Description>\n"
        f"  <CityPlanPicture1>{cpp1.url}</CityPlanPicture1>\n"
        f"  <CityPlanPicture2>{cpp2.url}</CityPlanPicture2>\n"
        f"  <VirtualPresentation>{obj.virtual_presentation}</VirtualPresentation>\n"
        f"  <VideoPresentationUrl>{obj.video_presentation_url}</VideoPresentationUrl>\n"
        f"  <ListingBackgroundImage>{obj.listing_background_image}</ListingBackgroundImage>\n"
        f"  <ListingBackgroundColor>{obj.listing_background_color}</ListingBackgroundColor>\n"
        f'  <FloorLocation high="E" low="E" number="{fl.number}" count="{fl.count}">{fl.description}</FloorLocation>\n'
        f"  <NumberOfRooms>{obj.number_of_rooms}</NumberOfRooms>\n"
        f"  <RoomTypes>{obj.room_types}</RoomTypes>\n"
        f"  <OtherSpaceDescription>{obj.other_space_description}</OtherSpaceDescription>\n"
        f'  <Balcony value="E">{bal.description}</Balcony>\n'
        f"  <Terrace>{obj.terrace}</Terrace>\n"
        f"  <DirectionOfWindows>{obj.direction_of_windows}</DirectionOfWindows>\n"
        f"  <View>{obj.view}</View>\n"
        f"  <Cellar>K</Cellar>\n"
        f'  <LivingArea unit="{la.unit}">123.45</LivingArea>\n'
        f"  <LivingAreaType>{obj.living_area_type.value}</LivingAreaType>\n"
        f'  <TotalArea unit="{ta.unit}" min="{ta.min}" max="{ta.max}">123.45</TotalArea>\n'
        f'  <FloorArea unit="{fa.unit}">123.45</FloorArea>\n'
        f"  <ResidentalApartmentArea>123.45</ResidentalApartmentArea>\n"
        f"  <OfficeArea>123.45</OfficeArea>\n"
        f"  <EstateArea>{obj.estate_area}</EstateArea>\n"
        f"  <ForestAmount>{obj.forest_amount}</ForestAmount>\n"
        f"  <LandArea>{obj.land_area}</LandArea>\n"
        f"  <RealEstateID>{obj.real_estate_id}</RealEstateID>\n"
        f"  <RealEstateCode>{obj.real_estate_code}</RealEstateCode>\n"
        f"  <HousingCompanyName>{obj.housing_company_name}</HousingCompanyName>\n"
        f"  <HousingCompanyKey>{obj.housing_company_key}</HousingCompanyKey>\n"
        f"  <BusinessId>{obj.business_id}</BusinessId>\n"
        f"  <Disponent>{obj.disponent}</Disponent>\n"
        f"  <RealEstateManagement>{obj.real_estate_management}</RealEstateManagement>\n"
        f"  <NumberOfApartments>{obj.number_of_apartments}</NumberOfApartments>\n"
        f'  <Lift value="K">{lift.description}</Lift>\n'
        f'  <YearOfBuilding original="{yob.original}">{yob.description}</YearOfBuilding>\n'
        f"  <YearStartOfUse>{obj.year_start_of_use}</YearStartOfUse>\n"
        f"  <BasicRenovations>{obj.basic_renovations}</BasicRenovations>\n"
        f"  <RenovationYearFacade>{obj.renovation_year_facade}</RenovationYearFacade>\n"
        f"  <RenovationYearRoof>{obj.renovation_year_roof}</RenovationYearRoof>\n"
        f"  <RenovationYearPlumbing>{obj.renovation_year_plumbing}</RenovationYearPlumbing>\n"
        f"  <RenovationYearBathrooms>{obj.renovation_year_bathrooms}</RenovationYearBathrooms>\n"
        f"  <FutureRenovations>{obj.future_renovations}</FutureRenovations>\n"
        f"  <FutureRenovationYearFacade>{obj.future_renovation_year_facade}</FutureRenovationYearFacade>\n"
        f"  <FutureRenovationYearRoof>{obj.future_renovation_year_roof}</FutureRenovationYearRoof>\n"
        f"  <FutureRenovationYearPlumbing>{obj.future_renovation_year_plumbing}</FutureRenovationYearPlumbing>\n"
        f"  <FutureRenovationYearBathrooms>{obj.future_renovation_year_bathrooms}</FutureRenovationYearBathrooms>\n"
        f"  <Heating>{obj.heating}</Heating>\n"
        f"  <RoofType>{obj.roof_type}</RoofType>\n"
        f"  <BuildingRights>{obj.building_rights}</BuildingRights>\n"
        f'  <BuildingRightsAmount type="{bra.type.value}">123.45</BuildingRightsAmount>\n'
        f"  <NumberOfOffices>{obj.number_of_offices}</NumberOfOffices>\n"
        f"  <Sanitation>{obj.sanitation}</Sanitation>\n"
        f"  <WaterAndSewage>{obj.water_and_sewage}</WaterAndSewage>\n"
        f"  <SewerSystem>{obj.sewer_system}</SewerSystem>\n"
        f"  <UseOfWater>{obj.use_of_water}</UseOfWater>\n"
        f"  <VentilationSystem>{obj.ventilation_system}</VentilationSystem>\n"
        f"  <OtherBuildings>{obj.other_buildings}</OtherBuildings>\n"
        f"  <MoreEstateInformation>{obj.more_estate_information}</MoreEstateInformation>\n"
        f'  <GeneralCondition level="{gen.level.value}">{gen.description}</GeneralCondition>\n'
        f"  <ConditionInspection>{obj.condition_inspection}</ConditionInspection>\n"
        f"  <EstateNameAndNumber>{obj.estate_name_and_number}</EstateNameAndNumber>\n"
        f'  <Site type="{obj.site.type.value}"/>\n'
        f"  <SiteRent>{obj.site_rent}</SiteRent>\n"
        f"  <SiteRentContractEndDate>01.01.2020</SiteRentContractEndDate>\n"
        f'  <SiteArea unit="{sa.unit}">123.45</SiteArea>\n'
        f"  <AreaDescription>{obj.area_description}</AreaDescription>\n"
        f'  <Shore type="{obj.shore.type.value}"/>\n'
        f"  <ShoresDescription>{obj.shores_description}</ShoresDescription>\n"
        f"  <ShoreDirection>{obj.shore_direction}</ShoreDirection>\n"
        f"  <ShoreLength>{obj.shore_length}</ShoreLength>\n"
        f"  <WatersDescription>{obj.waters_description}</WatersDescription>\n"
        f"  <BuildingPlanInformation>{obj.building_plan_information}</BuildingPlanInformation>\n"
        f"  <BuildingPlanSituation>{obj.building_plan_situation}</BuildingPlanSituation>\n"
        f"  <Grounds>{obj.grounds}</Grounds>\n"
        f"  <YardDescription>{obj.yard_description}</YardDescription>\n"
        f"  <YardDirection>{obj.yard_direction}</YardDirection>\n"
        f'  <HeatingCosts unit="{hc.unit}">123.45</HeatingCosts>\n'
        f'  <SaunaCharge unit="{sc.unit}">123.45</SaunaCharge>\n'
        f"  <EstateTax>{obj.estate_tax}</EstateTax>\n"
        f'  <HousingCompanyFee unit="{hcf.unit}">123.45</HousingCompanyFee>\n'
        f'  <FinancingFee unit="{ff.unit}">123.45</FinancingFee>\n'
        f'  <MaintenanceFee unit="{mf.unit}">123.45</MaintenanceFee>\n'
        f'  <WaterFee unit="{wf.unit}">123.45</WaterFee>\n'
        f"  <WaterFeeExplanation>{obj.water_fee_explanation}</WaterFeeExplanation>\n"
        f"  <ElectricityConsumption>{obj.electricity_consumption}</ElectricityConsumption>\n"
        f'  <ElectricityConsumptionCharge unit="{ec.unit}">123.45</ElectricityConsumptionCharge>\n'
        f'  <CableTvCharge unit="{ctc.unit}">123.45</CableTvCharge>\n'
        f"  <RoadCosts>{obj.road_costs}</RoadCosts>\n"
        f"  <OtherFees>{obj.other_fees}</OtherFees>\n"
        f"  <ShareOfDebt85>123.45</ShareOfDebt85>\n"
        f"  <ShareOfDebt70>123.45</ShareOfDebt70>\n"
        f'  <ChargeFee unit="{cf.unit}">123.45</ChargeFee>\n'
        f'  <CarParkingCharge unit="{cpc.unit}">123.45</CarParkingCharge>\n'
        f"  <BuildingMaterial>{obj.building_material}</BuildingMaterial>\n"
        f"  <Foundation>{obj.foundation}</Foundation>\n"
        f"  <WallConstruction>{obj.wall_construction}</WallConstruction>\n"
        f"  <RoofMaterial>{obj.roof_material}</RoofMaterial>\n"
        f"  <Floor>{obj.floor}</Floor>\n"
        f"  <BedroomFloor>{obj.bedroom_floor}</BedroomFloor>\n"
        f"  <KitchenFloor>{obj.kitchen_floor}</KitchenFloor>\n"
        f"  <LivingRoomFloor>{obj.living_room_floor}</LivingRoomFloor>\n"
        f"  <BathroomFloor>{obj.bathroom_floor}</BathroomFloor>\n"
        f"  <BedroomWall>{obj.bedroom_wall}</BedroomWall>\n"
        f"  <KitchenWall>{obj.kitchen_wall}</KitchenWall>\n"
        f"  <LivingRoomWall>{obj.living_room_wall}</LivingRoomWall>\n"
        f"  <BathroomWall>{obj.bathroom_wall}</BathroomWall>\n"
        f"  <OtherRoomsMaterials>{obj.other_rooms_materials}</OtherRoomsMaterials>\n"
        f"  <KitchenAppliances>{obj.kitchen_appliances}</KitchenAppliances>\n"
        f"  <BathroomAppliances>{obj.bathroom_appliances}</BathroomAppliances>\n"
        f"  <BedroomAppliances>{obj.bedroom_appliances}</BedroomAppliances>\n"
        f"  <LivingRoomAppliances>{obj.living_room_appliances}</LivingRoomAppliances>\n"
        f"  <NonIncludedAppliances>{obj.non_included_appliances}</NonIncludedAppliances>\n"
        f"  <OtherIncludedAppliances>{obj.other_included_appliances}</OtherIncludedAppliances>\n"
        f'  <Sauna own="K" common="E">{sauna.description}</Sauna>\n'
        f"  <StorageSpace>{obj.storage_space}</StorageSpace>\n"
        f'  <ParkingSpace type="{ps.type.value}" heated="{ps.heated.value}" electricityOutlet="K">{ps.text_value}</ParkingSpace>\n'
        f"  <CarStorage>{obj.car_storage}</CarStorage>\n"
        f"  <CommonAreas>{obj.common_areas}</CommonAreas>\n"
        f"  <AntennaSystem>{obj.antenna_system}</AntennaSystem>\n"
        f"  <TvAppliances>{obj.tv_appliances}</TvAppliances>\n"
        f"  <InternetAppliances>{obj.internet_appliances}</InternetAppliances>\n"
        f"  <DateWhenAvailable>01.01.2020</DateWhenAvailable>\n"
        f"  <BecomesAvailable>{obj.becomes_available}</BecomesAvailable>\n"
        f"  <RentFixedTermStart>01.01.2020</RentFixedTermStart>\n"
        f"  <RentFixedTermEnd>01.01.2020</RentFixedTermEnd>\n"
        f"  <RentMinLength>{obj.rent_min_length}</RentMinLength>\n"
        f"  <ExtraVisibilityStartDateTime>2020-01-01T12:00:00</ExtraVisibilityStartDateTime>\n"
        f'  <Rented value="K"/>\n'
        f'  <RentFurnished value="E"/>\n'
        f"  <MunicipalDevelopment>{obj.municipal_development}</MunicipalDevelopment>\n"
        f"  <HonoringClause>{obj.honoring_clause}</HonoringClause>\n"
        f"  <LeaseHolder>{obj.lease_holder}</LeaseHolder>\n"
        f"  <TermOfLease>{obj.term_of_lease}</TermOfLease>\n"
        f"  <Encumbrances>{obj.encumbrances}</Encumbrances>\n"
        f"  <Mortgages>{obj.mortgages}</Mortgages>\n"
        f"  <RentIncrease>{obj.rent_increase}</RentIncrease>\n"
        f"  <RentingTerms>{obj.renting_terms}</RentingTerms>\n"
        f'  <RentFixedTerm value="E"/>\n'
        f"  <Services>{obj.services}</Services>\n"
        f"  <Connections>{obj.connections}</Connections>\n"
        f"  <DrivingInstructions>{obj.driving_instructions}</DrivingInstructions>\n"
        f'  <RentPerMonth unit="{rpm.unit}">123.45</RentPerMonth>\n'
        f'  <RentPerDay unit="{rpd.unit}">123.45</RentPerDay>\n'
        f'  <RentPerWeek unit="{rpw.unit}">123.45</RentPerWeek>\n'
        f'  <RentPerYear unit="{rpy.unit}">123.45</RentPerYear>\n'
        f'  <RentPerWeekEnd unit="{rpwe.unit}">123.45</RentPerWeekEnd>\n'
        f'  <UnencumberedSalesPrice currency="{usp.currency}">123.45</UnencumberedSalesPrice>\n'
        f'  <SalesPrice currency="{sp.currency}">123.45</SalesPrice>\n'
        f'  <DebtPayable value="K"/>\n'
        f'  <RedemptionPrice currency="{rp.currency}">123.45</RedemptionPrice>\n'
        f"  <BuyerCosts>{obj.buyer_costs}</BuyerCosts>\n"
        f"  <ApartmentRentIncome>123.45</ApartmentRentIncome>\n"
        f'  <RentComission currency="{rc.currency}">123.45</RentComission>\n'
        f"  <RentSecurityDeposit>{obj.rent_security_deposit}</RentSecurityDeposit>\n"
        f'  <RentSecurityDeposit2 currency="{rsd2.currency}">123.45</RentSecurityDeposit2>\n'
        f'  <FinancingOffer1 percentage="{fo1.percentage}" price="{fo1.price}" fee="{fo1.fee}"/>\n'
        f'  <FinancingOffer2 percentage="{fo2.percentage}" price="{fo2.price}" fee="{fo2.fee}"/>\n'
        f"  <SiteRepurchasePrice>123.45</SiteRepurchasePrice>\n"
        f"  <SiteCondominiumFee>123.45</SiteCondominiumFee>\n"
        f"  <MagazineIdentifier>{obj.magazine_identifier}</MagazineIdentifier>\n"
        f"  <PrintMediaText>{obj.print_media_text}</PrintMediaText>\n"
        f"  <EstateAgentContactPerson>{obj.estate_agent_contact_person}</EstateAgentContactPerson>\n"
        f"  <EstateAgentEmail>{obj.estate_agent_email}</EstateAgentEmail>\n"
        f"  <EstateAgentTelephone>{obj.estate_agent_telephone}</EstateAgentTelephone>\n"
        f"  <EstateAgentTitle>{obj.estate_agent_title}</EstateAgentTitle>\n"
        f"  <EstateAgentDegrees>{obj.estate_agent_degrees}</EstateAgentDegrees>\n"
        f'  <EstateAgentRating value="{ear.value}"/>\n'
        f'  <EstateAgentSocialMedia url="{easm.url}">{easm.description}</EstateAgentSocialMedia>\n'
        f"  <EstateAgentContactPersonPictureUrl>{obj.estate_agent_contact_person_picture_url}</EstateAgentContactPersonPictureUrl>\n"
        f"  <Inquiries>{obj.inquiries}</Inquiries>\n"
        f'  <ShowingDate1 firstShowing="K">01.01.2020</ShowingDate1>\n'
        f"  <ShowingStartTime1>{obj.showing_start_time1}</ShowingStartTime1>\n"
        f"  <ShowingEndTime1>{obj.showing_end_time1}</ShowingEndTime1>\n"
        f"  <ShowingDateExplanation1>{obj.showing_date_explanation1}</ShowingDateExplanation1>\n"
        f"  <ShowingDate2>01.01.2020</ShowingDate2>\n"
        f"  <ShowingStartTime2>{obj.showing_start_time2}</ShowingStartTime2>\n"
        f"  <ShowingEndTime2>{obj.showing_end_time2}</ShowingEndTime2>\n"
        f"  <ShowingDateExplanation2>{obj.showing_date_explanation2}</ShowingDateExplanation2>\n"
        f"  <ContactRequestEmail>{obj.contact_request_email}</ContactRequestEmail>\n"
        f"  <ElectronicBrochureRequestEmail>{obj.electronic_brochure_request_email}</ElectronicBrochureRequestEmail>\n"
        f"  <ElectronicBrochureRequestUrl>{obj.electronic_brochure_request_url}</ElectronicBrochureRequestUrl>\n"
        f"  <ApplicationUrl>{obj.application_url}</ApplicationUrl>\n"
        f"  <ShowLeadForm>K</ShowLeadForm>\n"
        f"  <MoreInfoUrl>{obj.more_info_url}</MoreInfoUrl>\n"
        f'  <Attachments url="{att.url}">{att.link_text}</Attachments>\n'
        f'  <CampaignLink targetUrl="{cl.target_url}" pictureUrl="{cl.picture_url}"/>\n'
        f"  <BannerHtml>{obj.banner_html}</BannerHtml>\n"
        f'  <PromotionalOffer value="E"/>\n'
        f"  <PromotionalOfferTitle>{obj.promotional_offer_title}</PromotionalOfferTitle>\n"
        f"  <PromotionalOfferDescription>{obj.promotional_offer_description}</PromotionalOfferDescription>\n"
        f"  <PromotionalOfferUrl>{obj.promotional_offer_url}</PromotionalOfferUrl>\n"
        f"  <PromotionalOfferUrlText>{obj.promotional_offer_url_text}</PromotionalOfferUrlText>\n"
        f"  <PromotionalOfferLogo>{obj.promotional_offer_logo}</PromotionalOfferLogo>\n"
        f"  <PromotionalOfferColor>{obj.promotional_offer_color}</PromotionalOfferColor>\n"
        f"  <OnlineOffer>K</OnlineOffer>\n"
        f"  <OnlineOfferLogo>{obj.online_offer_logo}</OnlineOfferLogo>\n"
        f"  <OnlineOfferUrl>{obj.online_offer_url}</OnlineOfferUrl>\n"
        f"  <OnlineOfferHighestBid>123.45</OnlineOfferHighestBid>\n"
        f'  <OnlineOfferLabel backgroundColor="{ool.background_color}" textColor="{ool.text_color}">{ool.text_value}</OnlineOfferLabel>\n'
        f"  <OnlineOfferSearchLogo>{obj.online_offer_search_logo}</OnlineOfferSearchLogo>\n"
        f"  <rc-energy-flag>{obj.rc_energy_flag}</rc-energy-flag>\n"
        f"  <rc-energyclass>{obj.rc_energyclass}</rc-energyclass>\n"
        f"  <rc-wastewater-flag>{obj.rc_wastewater_flag}</rc-wastewater-flag>\n"
        f"  <EstateDivision>{obj.estate_division}</EstateDivision>\n"
        f'  <NewDevelopmentStatus value="{nds.value.value}"/>\n'
        f"  <TimeOfCompletion>01.01.2020</TimeOfCompletion>\n"
        f"</Apartment>\n"
    )


@override_settings(
    OIKOTIE_TRANSFER_ID="test", OIKOTIE_COMPANY_NAME="ATT", OIKOTIE_ENTRYPOINT="test"
)
def test_appartment_xml_created(test_folder):
    apartment = MinimalApartmentFactory.create_batch(1)
    test_file = create_apartments(apartment, test_folder)
    test_xml = open(path.join(test_folder, test_file), "r")
    test_xml = test_xml.read()

    expected = [
        "<?xml version='1.0' encoding='utf-8'?>",
        "<Apartment type",
        "newHouses",
        "<Key>",
        "<VendorIdentifier>",
    ]

    assert all(item in test_xml for item in expected)

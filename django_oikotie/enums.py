from enum import Enum


class Case(Enum):
    PASCAL = 1
    KEBAB = 2
    CAMEL = 3


class ApartmentAction(Enum):
    UPDATE = "update"
    REMOVE = "remove"


class Availability(Enum):
    PRE_MARKETING = "ennakkomarkkinoinnissa"
    FOR_SALE = "myynnissä"


class ApartmentType(Enum):
    BLOCK_OF_FLATS = "KT"  # Kerrostalo
    HOUSE = "OT"  # Omakotitalo
    ROW_HOUSE = "RT"  # Rivitalo
    DUPLEX = "PT"  # Paritalo
    DETACHED_HOUSE = "ET"  # Erillistalo
    COTTAGE_OR_VILLA = "MO"  # Mökki tai huvila
    VACATION_APARTMENT = "LH"  # Lomahuoneisto
    VACATION_APARTMENT_ABROAD = "UL"  # Loma-asunto ulkomailla
    TIME_SHARE = "LO"  # Lomaosake
    RESIDENTIAL_PLOT = "OKTT"  # Omakotitalotontti
    LEISURE_PLOT = "VT"  # Vapaa-ajan tontti
    ROW_HOUSE_PLOT = "RTT"  # Rivitalotontti
    PLOT = "TO"  # Tontti
    PARKING_SPACE = "AP"  # Autopaikka
    GARAGE = "AT"  # Autotalli
    FARM = "MAT"  # Maatila
    FOREST_PROPERTY = "MET"  # Metsätila
    OFFICE_PREMISES = "TOT"  # Toimistotila
    BUSINESS_PREMISES = "LT"  # Liiketila
    STORAGE_SPACE = "VART"  # Varastotila
    RESTAURANT_PREMISES = "RAV"  # Ravintolatila
    EXHIBITION_PREMISES = "NAY"  # Näyttelytila
    HOBBY_PREMISES = "HAR"  # Harrastetila
    HUB_PREMISES = "HUB"  # Hub-tila
    OTHER_OFFICE_PREMISES = "TMUU"  # Muu toimistotila
    PRODUCTION_PREMISES = "TUT"  # Tuotantotila
    WOODEN_HOUSE_DEPARTMENT = "PUUT"  # Puutalo-osake
    BALCONY_ACCESS_HOUSE = "LUHT"  # Luhtitalo

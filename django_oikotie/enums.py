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


class BuildingRightAmountType(Enum):
    DENSITY_RATE = "e"
    SQUARE_METERS = "m2"


class EstateType(Enum):
    REAL_ESTATE = "K"
    CONDOMINIUM = "E"


class LivingAreaType(Enum):
    CONTROL = "CONTROL"
    OFFICIAL = "OFFICIAL"
    CERTIFIED = "CERTIFIED"
    OTHER = "OTHER"


class GeneralConditionLevel(Enum):
    HIDDEN = 0
    NEW = 1
    EXCELLENT = 2
    GOOD = 3
    SATISFACTORY = 4
    PASSABLE = 5
    BAD = 6
    UNKNOWN = 9


class ModeOfHabitationType(Enum):
    OWNED = "OM"
    OWNERSHIP = "OO"
    RIGHT_OF_OCCUPANCY = "AO"
    TENANCY = "VU"


class ModeOfHabitationRentType(Enum):
    MAIN = "MAIN"
    SUB = "SUB"


class NewDevelopmentStatusChoices(Enum):
    NONE_OR_HIDDEN = 0
    UNDER_PLANNING = 1
    PRE_MARKETING = 2
    UNDER_CONSTRUCTION = 3
    READY_TO_MOVE = 4


class ParkingSpaceHeatingType(Enum):
    NOT_DISPLAYED = 0
    COLD = 1
    WARM = 2


class ParkingSpaceType(Enum):
    NOT_DISPLAYED = 0
    NONE = 1
    PARKING_SPACE = 2
    CARPORT = 3
    GARAGE = 4
    PARKING_GARAGE = 5


class ShoreType(Enum):
    OWN_SHORE = "OR"
    WATER_RIGHTS = "OV"
    SHORE_RIGHTS = "RO"
    NO_SHORE = "ER"
    UNKNOWN = "ET"
    OTHER = "MUU"


class SiteType(Enum):
    OWNED = "O"
    RENT = "V"

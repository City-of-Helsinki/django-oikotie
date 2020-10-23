from enum import Enum


class Case(Enum):
    PASCAL = 1
    KEBAB = 2
    CAMEL = 3


class ApartmentAction(Enum):
    UPDATE = "update"
    REMOVE = "remove"


class ApartmentType(Enum):
    KT = "Kerrostalo"
    OT = "Omakotitalo"
    RT = "Rivitalo"
    PT = "Paritalo"
    ET = "Erillistalo"
    MO = "Mökki tai huvila"
    LH = "Lomahuoneisto"
    UL = "Loma-asunto ulkomailla"
    LO = "Lomaosake"
    OKTT = "Omakotitalotontti"
    VT = "Vapaa-ajan tontti"
    RTT = "Rivitalotontti"
    TO = "Tontti"
    AP = "Autopaikka"
    AT = "Autotalli"
    MAT = "Maatila"
    MET = "Metsätila"
    TOT = "Toimistotila"
    LT = "Liiketila"
    VART = "Varastotila"
    RAV = "Ravintolatila"
    NAY = "Näyttelytila"
    HAR = "Harrastetila"
    HUB = "Hub-tila"
    TMUU = "Muu toimistotila"
    TUT = "Tuotantotila"
    PUUT = "Puutalo-osake"
    LUHT = "Luhtitalo"

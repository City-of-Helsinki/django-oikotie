import math
from decimal import Decimal
from typing import TYPE_CHECKING, Union

from lxml import etree

from .enums import Case

if TYPE_CHECKING:
    from .xml_models import XMLModel


def object_to_xml_string(obj: "XMLModel", encoding: str = "utf-8"):
    root = obj.to_etree()

    return etree.tostring(
        root, encoding=encoding, xml_declaration=True, pretty_print=True
    )


def transform_name(name: str, case: Case) -> str:
    # Name is snake_case by default
    if case == Case.KEBAB:
        return name.replace("_", "-")
    elif case == Case.CAMEL:
        parts = name.split("_")
        return parts[0] + "".join([p.title() for p in parts[1:]])
    else:  # PascalCase
        return name.title().replace("_", "")


def truncate_to_n_decimal_places(value: Union[float, Decimal], n: int) -> float:
    """
    Truncate float or Decimal to n decimal places.
    """
    return math.floor(value * 10**n) / 10**n


def yes_no_bool(value: bool) -> str:
    return "K" if value else "E"

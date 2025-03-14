import math
import os
from decimal import Decimal
from typing import TYPE_CHECKING, Union

from django.conf import settings
from lxml import etree

from .enums import Case

if TYPE_CHECKING:
    from .xml_models import XMLModel

import logging

_logger = logging.getLogger(__name__)


def get_schemas() -> dict:  # TODO: add return type
    """
    Fetches relaxNG validation schemas from external storage\
    or from local files (dev env).
    """
    schema_dir = settings.OIKOTIE_SCHEMA_DIR
    _logger.info(f"schema_dir {schema_dir}")

    # TODO: parameterize
    filenames = (
        settings.OIKOTIE_APARTMENTS_BATCH_SCHEMA,
        settings.OIKOTIE_APARTMENTS_UPDATE_SCHEMA,
        settings.OIKOTIE_HOUSINGCOMPANIES_BATCH_SCHEMA,
    )
    schemas = {}
    _logger.info(f"get schemas from {schema_dir}")

    for filename in filenames:

        schema: etree.RelaxNG = etree.RelaxNG(
            etree.parse(os.path.join(schema_dir, filename))
        )
        schemas[filename] = schema

    return schemas


def validate_against_schema(schema_filename: str, xml_path: str) -> bool:
    schema = get_schemas()[schema_filename]

    _logger.info(
        f"Validating file {xml_path} against schema {os.path.join(settings.OIKOTIE_SCHEMA_DIR, schema_filename)}"  # noqa: E501
    )  # noqa: E501
    with open(xml_path, "rb") as f:
        file_content = f.read()
        xml_file = etree.fromstring(file_content)
        valid = schema.validate(xml_file)
        if not valid:
            _logger.error(schema.error_log)
        else:
            _logger.info(f"File {xml_path} is valid")

        return valid
    pass


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


def truncate_to_n_decimal_places(
    value: Union[float, Decimal], n: int
) -> float:  # noqa: E501
    """
    Truncate float or Decimal to n decimal places.
    """
    return math.floor(value * 10**n) / 10**n


def yes_no_bool(value: bool) -> str:
    return "K" if value else "E"

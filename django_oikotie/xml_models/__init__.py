import types
from enum import Enum
from typing import Union

from lxml import etree

from ..utils import transform_name, yes_no_bool


class XMLModel:
    """
    Baseclass for dataclasses that are representation of a XML element

    Example::

        >>> from dataclasses import dataclass
        >>> from django_oikotie.enums import Case
        >>> from django_oikotie.xml_models import XMLModel
        >>>
        >>> @dataclass
        >>> class Address(XMLModel):
        >>>     street: str
        >>>     postal_code: str
        >>>     city: str
        >>>
        >>>     class Meta:
        >>>         element_name = "address"
        >>>         case = Case.KEBAB

    Above example would be serialized into following XML:

        <address>
          <street>Somestreet 1</street>
          <postal-code>12345</postal-code>
          <city>Test City</city>
        </address>
    """

    class Meta:
        element_name = None
        case = None
        attributes = []

    def __init__(self, *args, **kwargs):
        self._validate_meta()
        super().__init__(*args, **kwargs)

    def _validate_meta(self):
        case = self.Meta.case
        element_name = self.Meta.element_name

        if not element_name:
            err = f"{self.__class__.__name__}.Meta.element_name is not defined"
            raise ValueError(err)
        if not case:
            err = f"{self.__class__.__name__}.Meta.case is not defined"
            raise ValueError(err)

    def get_formatted_value(
        self, key: str
    ) -> Union[str, list, "XMLModel", etree._Element]:
        format_function = getattr(self, f"format_{key}", None)
        if format_function and callable(format_function):
            # Class has format_<key> method which is expected to return
            # correctly formatted value. Return that value as is.
            return format_function()

        value = getattr(self, key)

        if isinstance(value, (list, XMLModel)):
            return value
        if isinstance(value, bool):
            return yes_no_bool(value)
        if isinstance(value, Enum):
            return str(value.value)
        else:
            return str(value)

    def get_element_name(self, key: str) -> str:
        if key in getattr(self.Meta, "element_name_overrides", {}):
            return self.Meta.element_name_overrides[key]

        case_overrides = getattr(self.Meta, "case_overrides", {})
        case = case_overrides.get(key, self.Meta.case)

        return transform_name(key, case)

    def to_etree(self) -> etree._Element:
        root = etree.Element(self.Meta.element_name)

        for key, value in self.__dict__.items():
            if value is None:
                continue

            # Format key and value before anything is added to the root element.
            value = self.get_formatted_value(key)
            element_name = self.get_element_name(key)

            if etree.iselement(value):
                # The value is an lxml element. Append it to the root element as is.
                root.append(value)
            elif isinstance(value, types.GeneratorType):
                # The value is a generator object that is a result of yielding
                # XMLModel.to_etree() in format_<key> function. Yielded lxml Elements
                # are added directly to root element instead of nesting them within
                # separate child element
                for child_element in value:
                    root.append(child_element)
            elif isinstance(value, XMLModel):
                # The value is an XMLModel object. Serialize it to a lxml element and
                # append it to the root element.
                element = value.to_etree()
                root.append(element)
            elif isinstance(value, list):
                # The value is a list of XMLModel objects. Serialize them to lxml
                # elements and append them to the root element.
                element = etree.Element(element_name)
                for child in value:
                    element.append(child.to_etree())
                root.append(element)
            elif key in getattr(self.Meta, "attributes", []):
                # The value is an attribute. Set the key-value pair as an attribute
                # to the root element instead of it being a regular child element.
                root.attrib[element_name] = value
            else:
                # Key-value pair is handled as a regular child element
                element = etree.Element(element_name)
                element.text = value
                root.append(element)
        return root

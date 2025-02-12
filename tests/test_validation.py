import os
from django.test import override_settings
from django.conf import settings

from django_oikotie.utils import validate_against_schema
from tests.utils import get_tests_base_path


class TestOikotieUtils:
    schema_dir = os.path.join(get_tests_base_path(), "schemas")
    test_xml_dir = os.path.join(get_tests_base_path(), "test_files")

    @override_settings(OIKOTIE_SCHEMA_DIR=schema_dir)
    def test_get_schemas(self):
        """Assert that fetching schemas works."""
        from django_oikotie.utils import get_schemas
        schemas = get_schemas()

        assert len(schemas.keys()) == 3
        assert schemas.get(settings.OIKOTIE_APARTMENTS_BATCH_SCHEMA) is not None
        assert schemas.get(settings.OIKOTIE_APARTMENTS_UPDATE_SCHEMA) is not None
        assert schemas.get(settings.OIKOTIE_HOUSINGCOMPANIES_BATCH_SCHEMA) is not None

    @override_settings(OIKOTIE_SCHEMA_DIR=schema_dir)
    def test_schema_validation_valid_file(self):
        """Assert that schema validation will return True for a valid file"""

        test_xml_path = os.path.join(
            self.test_xml_dir, "valid.xml"
        )
        valid = validate_against_schema(
            settings.OIKOTIE_APARTMENTS_BATCH_SCHEMA,
            test_xml_path
        )
        assert valid is True

    @override_settings(OIKOTIE_SCHEMA_DIR=schema_dir)
    def test_schema_validation_invalid_file(self):
        test_xml_path = os.path.join(
            self.test_xml_dir,"invalid.xml"
        )
        valid = validate_against_schema(
            settings.OIKOTIE_APARTMENTS_BATCH_SCHEMA,
            test_xml_path
        )
        assert valid is False

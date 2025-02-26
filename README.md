# django-oikotie
A Django wrapper around Oikotie API

## Validation schemas
The environment variables `OIKOTIE_APARTMENTS_BATCH_SCHEMA_URL`, `OIKOTIE_APARTMENTS_UPDATE_SCHEMA_URL`,
`OIKOTIE_HOUSINGCOMPANIES_BATCH_SCHEMA_URL` need to be set and pointed to the proper validation schemas provided by the Oikotie API customer service. The schemas will be added to the image at the directory defined by `OIKOTIE_SCHEMA_DIR` env variable.
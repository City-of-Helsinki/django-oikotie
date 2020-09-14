import time
from ftplib import FTP
from xml.etree.ElementTree import ElementTree

from django.conf import settings
from django.utils.text import slugify

from django_oikotie.utils import object_to_etree


def create_housing_companies(housing_companies):
    session = FTP(
        host=settings.OIKOTIE_FTP_HOST,
        user=settings.OIKOTIE_USER,
        passwd=settings.OIKOTIE_PASSWORD,
    )
    for housing_company in housing_companies:
        tree = ElementTree(object_to_etree(housing_company))
        filename = "HOUSINGCOMPANY{}.{}.neoff001.{}.xml".format(
            slugify(housing_company.name),
            settings.OIKOTIE_ENTRYPOINT,
            time.strftime("%Y%m%d%H%M%S"),
        )

        tree.write(filename, encoding="utf-8", xml_declaration=True)
        session.storbinary("STOR {}.temp".format(filename), open(filename, "rb"))
        session.rename("{}.temp".format(filename), filename)
    return session.retrlines("LIST")

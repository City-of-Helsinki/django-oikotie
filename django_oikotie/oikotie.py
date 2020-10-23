import time
from ftplib import FTP
from xml.etree.ElementTree import ElementTree

from django.conf import settings
from lxml.etree import Element

from django_oikotie.enums import ApartmentAction


def get_session():
    return FTP(
        host=settings.OIKOTIE_FTP_HOST,
        user=settings.OIKOTIE_USER,
        passwd=settings.OIKOTIE_PASSWORD,
    )


def get_filename(prefix):
    return "{}{}.{}.neoff001.{}.xml".format(
        prefix,
        settings.OIKOTIE_COMPANY_NAME,
        settings.OIKOTIE_ENTRYPOINT,
        time.strftime("%Y%m%d%H%M%S"),
    )


def write_file(filename, root):
    session = get_session()
    tree = ElementTree(root)
    tree.write(filename, encoding="utf-8", xml_declaration=True)
    session.storbinary("STOR {}.temp".format(filename), open(filename, "rb"))
    session.rename("{}.temp".format(filename), filename)
    session.quit()


def create_housing_companies(housing_companies):
    filename = get_filename("HOUSINGCOMPANY")
    root = Element("housing-companies")
    for housing_company in housing_companies:
        root.append(housing_company.to_etree())
    write_file(filename, root)


def create_apartments(apartments):
    filename = get_filename("APT")
    root = Element("Apartments")
    for apartment in apartments:
        root.append(apartment.to_etree())
    write_file(filename, root)


def update_apartments(apartments, action=ApartmentAction.UPDATE):
    filename = get_filename("UPDATEAPT")
    root = Element("Apartments")
    for apartment in apartments:
        apartment.action = action
        root.append(apartment.to_etree())
    write_file(filename, root)


def remove_apartments(apartments):
    update_apartments(apartments, ApartmentAction.REMOVE)

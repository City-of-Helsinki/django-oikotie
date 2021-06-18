import time
from ftplib import FTP
from os import path
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


def send_items(file_path, filename):
    session = get_session()
    with open(path.join(file_path, filename), "rb") as f:
        session.storbinary("STOR temp/{}.temp".format(filename), f)
        session.rename("temp/{}.temp".format(filename), "data/{}".format(filename))
        session.quit()


def create_housing_companies(housing_companies, file_path="."):
    filename = get_filename("HOUSINGCOMPANY")
    root = Element("housing-companies")
    for housing_company in housing_companies:
        root.append(housing_company.to_etree())
    tree = ElementTree(root)
    tree.write(path.join(file_path, filename), encoding="utf-8", xml_declaration=True)
    return filename


def create_apartments(apartments, file_path="."):
    filename = get_filename("APT")
    root = Element("Apartments")
    for apartment in apartments:
        root.append(apartment.to_etree())
    tree = ElementTree(root)
    tree.write(path.join(file_path, filename), encoding="utf-8", xml_declaration=True)
    return filename


def update_apartments(apartments, action=ApartmentAction.UPDATE, file_path="."):
    filename = get_filename("UPDATEAPT")
    root = Element("Apartments")
    for apartment in apartments:
        apartment.action = action
        root.append(apartment.to_etree())
    tree = ElementTree(root)
    tree.write(path.join(file_path, filename), encoding="utf-8", xml_declaration=True)
    return filename


def remove_apartments(apartments):
    return update_apartments(apartments, ApartmentAction.REMOVE)

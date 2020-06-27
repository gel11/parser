from xml.etree.ElementTree import Element, SubElement

import config


class XmlCreator:

    def create_persons_element(self):
        return Element(config.PEOPLE_TAG_NAME)

    def create_family_element(self, parent, columns):
        family_ele = SubElement(parent, config.FAMILY_TAG_NAME)
        self.create_elements(family_ele, columns, config.FAMILY_COLUMNS)
        return family_ele

    def create_person_element(self, parent, columns):
        person_ele = SubElement(parent, config.PERSON_TAG_NAME)
        self.create_elements(person_ele, columns, config.PERSON_COLUMNS)
        return person_ele

    def create_address_element(self, parent, columns):
        address_ele = SubElement(parent, config.ADDRESS_TAG_NAME)
        self.create_elements(address_ele, columns, config.ADDRESS_COLUMNS)
        return address_ele

    def create_phone_element(self, parent, columns):
        phone_ele = SubElement(parent, config.PHONE_TAG_NAME)
        self.create_elements(phone_ele, columns, config.PHONE_COLUMNS)
        return phone_ele

    def create_elements(self, parent, columns, columns_names):
        for column, column_name in zip(columns[1:], columns_names):
            ele = SubElement(parent, column_name)
            ele.text = column

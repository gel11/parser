import fileinput
from xml.etree.ElementTree import tostring

from xml.dom import minidom

import config
from validator import Validator, error
from xml_creator import XmlCreator


class Parser:

    def __init__(self):
        self.xmlCreator = XmlCreator()
        self.validator = Validator()
        self.root_element = None

    def parse_input_file(self, file_path):
        with fileinput.input(files=file_path) as f:
            self.root_element = self.xmlCreator.create_persons_element()
            column = self.validator.validate_first_row(f.readline(), f.lineno())
            self.__parse_line(f, column)

    def save_to_file(self, path):
        with open(path, "w") as f:
            f.write(self.__prettifyXML(self.root_element))

    def __parse_line(self, f, column):
        person_element = self.xmlCreator.create_person_element(self.root_element, column)
        line = self.__add_child_to_parent(person_element, f)

        if line is not None:
            column = self.validator.validate_columns(line, f.lineno())
            self.__parse_line(f, column)

    def __add_child_to_parent(self, person_element, f):
        parent = person_element
        for line in f:
            columns = self.validator.validate_columns(line, f.lineno())
            element_type = columns[0]

            if element_type == config.PHONE_TYPE:
                self.xmlCreator.create_phone_element(parent, columns)
            elif element_type == config.ADDRESS_TYPE:
                self.xmlCreator.create_address_element(parent, columns)
            elif element_type == config.FAMILY_TYPE:
                parent = self.xmlCreator.create_family_element(person_element, columns)
            elif element_type == config.PERSON_TYPE:
                return line
            else:
                error("Can not parse type {}".format(element_type), f.lineno())

        return None

    def __prettifyXML(self, elem):
        rough_string = tostring(elem, 'utf-8')
        re_parsed = minidom.parseString(rough_string)
        return re_parsed.toprettyxml(indent="  ")

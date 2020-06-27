import sys

import config


def error(msg, line):
    print("{}, error at line {}".format(msg, line))
    sys.exit(1)


class Validator:
    def validate_first_row(self, line, line_number):
        columns = self.validate_columns(line, line_number)
        if columns[0] != config.PERSON_TYPE:
            error("First row needs to be a person", line_number)
        return columns

    def validate_columns(self, line, line_number):
        columns = line.rstrip().split(config.DELIMITER)
        if len(columns) < 2:
            error("Each row needs to be equal or greater than two columns", line_number)
        return columns

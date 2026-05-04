######################################################################
# Authors: Artem Kurasov
# Username: kurasova
#
# Assignment: P01 - Final Project
#
# Purpose: Writing code for the Person class, which will
# store data about a person, including the following
# information: their name, date of birth, zodiac sign,
# element, and Kua number.
######################################################################
# No acknowledgements
######################################################################

from ZodiacSign import ZodiacSign
from Element import Element
from KuaNumber import KuaNumber


class Person:
    def __init__(self, name, birth_year, biological_sex, birth_month, birth_day):

        assert isinstance(name, str)
        self.name                       = name

        self.__zodiac_sign_object       = ZodiacSign(birth_year, birth_month, birth_day)
        self.__element_object           = Element(birth_year, birth_month, birth_day)
        self.__kua_number_object        = KuaNumber(birth_year, biological_sex, birth_month, birth_day)

        self.birth_year                 = birth_year
        self.biological_sex             = biological_sex
        self.birth_month                = birth_month
        self.birth_day                  = birth_day

        self.zodiac_sign                = self.__zodiac_sign_object.value
        self.element                    = self.__element_object.value
        self.kua_number                 = self.__kua_number_object.value

        self.zodiac_sign_description    = self.__zodiac_sign_object.description
        self.element_description        = self.__element_object.description
        self.kua_number_description     = self.__kua_number_object.description

        self.zodiac_sign_image          = self.__zodiac_sign_object.image
        self.element_image              = self.__element_object.image

        self.description                = self.combine_descriptions()

    def combine_descriptions(self):
        return str(self.zodiac_sign_description) + " " + str(self.element_description) + " " + str(self.kua_number_description)
#####################################################################
# Authors: Artem Kurasov
# Username: kurasova
#
# Assignment: P01 - Final Project
#
# Purpose: Writing code for the Compatibility class, which
# collects all the information about compatibility between two people
######################################################################
# No Acknowledgments
######################################################################

from ZodiacSignCompatibility import ZodiacSignCompatibility
from ElementCompatibility    import ElementCompatibility
from KuaNumberCompatibility  import KuaNumberCompatibility

class Compatibility:
    def __init__(self, person_1, person_2):
        self.zodiac_sign_compatibility_object       = ZodiacSignCompatibility(person_1, person_2)
        self.element_compatibility_object           = ElementCompatibility(person_1, person_2)
        self.kua_number_compatibility_object        = KuaNumberCompatibility(person_1, person_2)

        self.zodiac_sign_compatibility              = self.zodiac_sign_compatibility_object.value
        self.element_compatibility                  = self.element_compatibility_object.value
        self.kua_number_compatibility               = self.kua_number_compatibility_object.value

        self.zodiac_sign_compatibility_description  = self.zodiac_sign_compatibility_object.description
        self.element_compatibility_description      = self.element_compatibility_object.description
        self.kua_number_compatibility_description   = self.kua_number_compatibility_object.description

        self.description                            = self.combine_descriptions()

    def combine_descriptions(self):
        return str(self.zodiac_sign_compatibility_description) + str(self.element_compatibility_description) + str(self.kua_number_compatibility_description)
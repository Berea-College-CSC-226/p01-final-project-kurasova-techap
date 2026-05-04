######################################################################
# Authors: Artem Kurasov
# Username: kurasova
#
# Assignment: P01 - Final Project
#
# Purpose: Unit Testing Non-UI Elements of the Project
#
######################################################################
# No Acknowledgements
######################################################################

from ZodiacSign import ZodiacSign
from Element import Element
from KuaNumber import KuaNumber

from ZodiacSignCompatibility import ZodiacSignCompatibility
from ElementCompatibility import ElementCompatibility
from KuaNumberCompatibility import KuaNumberCompatibility

"""
Some of the unit tests are already prewritten in the AbstractClasses.py file, so 
this test will not go over extreme case scenarios, such as the wrong parameter type 
(because it is already tackled by that file)
"""

def zodiac_sign_test():
    """
    Tests the ZodiacSign Class.
    :return: None
    """

    assert ZodiacSign(2004,5, 25).value     == "Monkey"
    assert ZodiacSign(2005, 2, 9).value     == "Rooster"
    assert ZodiacSign(1931, 12, 31).value   == "Goat"

    # The next three dates of birth are before the Chinese New Year, so they
    # count as the previous year.
    assert ZodiacSign(2004, 1, 21).value    == "Goat"
    assert ZodiacSign(2005, 2, 8).value     == "Monkey"
    assert ZodiacSign(1931, 1, 30).value    == "Horse"



def element_test():
    """
    Tests the Element Class.
    :return: None
    """

    assert Element(2004, 5, 25).value   == "Wood"
    assert Element(2005, 2, 9).value    == "Wood"
    assert Element(1931, 12, 31).value  == "Metal"
    assert Element(1996, 3, 12).value   == "Fire"
    assert Element(1988, 3, 21).value   == "Earth"

    # The next three dates of birth are before the Chinese New Year, so they
    # count as the previous year.
    assert Element(2004, 1, 21).value   == "Water"
    assert Element(2005, 2, 8).value    == "Wood"
    assert Element(1931, 1, 30).value   == "Metal"



def kua_number_test():
    """
    Tests the KuaNumber Class.
    :return: None
    """

    assert KuaNumber(2004, "male",  5, 25).value    == 2
    # the Kua Number is 5, so for men it turns into 2

    assert KuaNumber(1936, "female", 5, 25).value   == 8
    # the Kua Number is 5, so for women it turns into 8

    assert KuaNumber(2005, "male", 2, 9).value      == 4
    assert KuaNumber(1931, "male", 12, 31).value    == 6
    assert KuaNumber(2005, "female", 2, 9).value    == 2
    assert KuaNumber(1931, "female", 12, 31).value  == 9

    # The next three dates of birth are before the Chinese New Year, so they
    # count as the previous year.
    assert KuaNumber(2004, "female", 1, 21).value   == 9
    assert KuaNumber(2005, "female", 2, 8).value    == 1
    assert KuaNumber(1931, "female", 1, 30).value   == 8

def compatibilities_test():
    """
    Tests the Person, the ZodiacSignCompatibility, the ElementCompatibility,
    the KuaNumberCompatibility Classes.
    :return: None
    """
    from Person import Person
    a = Person("John", 2005, "male",  5, 25)
    b = Person("Samantha", 2005, "female", 4, 21)
    c = Person("Kristen", 2004, "female", 2, 9)
    d = Person("Theodor", 1931, "male", 12, 31)

    from Compatibility import Compatibility
    c_d_compatibility = Compatibility(c, d)

    assert a.zodiac_sign    == "Rooster"
    assert a.element        == "Wood"
    assert a.kua_number     == 4

    assert b.zodiac_sign    == "Rooster"
    assert b.element        == "Wood"
    assert b.kua_number     == 2

    assert ZodiacSignCompatibility(a, b).value  == -3
    assert ZodiacSignCompatibility(a, c).value  == 0
    assert ZodiacSignCompatibility(b, c).value  == 0
    assert ZodiacSignCompatibility(a, d).value  == 0
    assert ZodiacSignCompatibility(b, d).value  == 0
    assert ZodiacSignCompatibility(c, d).value  == 0

    assert c_d_compatibility.zodiac_sign_compatibility  == 0

    assert ElementCompatibility(a, b).value     ==  1
    assert ElementCompatibility(a, c).value     ==  1
    assert ElementCompatibility(b, c).value     ==  1
    assert ElementCompatibility(a, d).value     == -1
    assert ElementCompatibility(b, d).value     == -1
    assert ElementCompatibility(c, d).value     == -1

    assert c_d_compatibility.element_compatibility      == -1

    assert KuaNumberCompatibility(a, b).value   == -2
    assert KuaNumberCompatibility(a, c).value   == -1
    assert KuaNumberCompatibility(b, c).value   == -2
    assert KuaNumberCompatibility(a, d).value   ==  2
    assert KuaNumberCompatibility(b, d).value   == -1
    assert KuaNumberCompatibility(c, d).value   ==  1

    assert c_d_compatibility.kua_number_compatibility   == 1


def main():
    zodiac_sign_test()
    element_test()
    kua_number_test()
    compatibilities_test()

if __name__ == "__main__":
    main()
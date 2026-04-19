######################################################################
# Authors: Artem Kurasov
# Username: kurasova
#
# Assignment: P01 - Final Project
#
# Purpose: Writing code for the KnowledgePiece class, which will
# be used as a parent class for the following classes:
# ZodiacSign, Element, KuaNumber, ZodiacSignCompatibility,
# ElementCompatibility, and KuaNumberCompatibility
######################################################################
# Acknowledgements:
#   Used the abc module: https://docs.python.org/3/library/abc.html
#   Article on how to create abstract classes: https://www.w3schools.com/python/ref_module_abc.asp
#   Chinese New Year Calendars:
#       - https://www.themalatree.com/chinese-new-year-dates-1930-to-2030/
#       - https://greenwichmeantime.com/chinese-new-year/1950/
#       - https://taiwan-database.net/PDFs/WTFpdf23.pdf
######################################################################

from abc import ABC, abstractmethod


class KnowledgePiece(ABC):
    """A class representing a piece of knowledge, whether it
    be a zodiac sign, an element, a Kua number, or any other
    piece of information."""

    description_dict = {}

    def __init__(self):
        self.value = self.evaluate()
        self.description = self.map_value()

    @abstractmethod
    def evaluate(self):
        """Finds self.value based on the attributes
        of the knowledge piece."""
        ...

    def map_value(self):
        """
        Maps the return value of the evaluate() method to
        a certain description.
        :return: a string from self.description_dict
        """
        return self.description_dict.get(self.evaluate(), -1)

"""
P.S.: The KnowledgePiece class allows you to write simpler classes,
following the pattern below (where ... represent pieces of code 
might need to be added): 


from AbstractClasses import KnowledgePiece

class ExampleClass(KnowledgePiece):

    description_dict = {value_1: "description_1", 
                        value_2: "description_2",
                        ...
                        }   
    ...

    def __init__(self, ...):
        ...                     # assign all the extra parameters to attributes here
        super().__init__()
        ...                     # anything that uses self.value

    def evaluate(self):
        ...

NOTE that self.value is created AFTER super().__init__(), so if any other 
function uses it, make sure to put them after super().__init__().
"""


chinese_new_years = {1900: (1, 31), 1901: (2, 19), 1902: (2,  8), 1903: (1, 29), 1904: (2, 16),
                     1905: (2,  4), 1906: (1, 25), 1907: (2, 13), 1908: (2,  2), 1909: (1, 22),
                     1910: (2, 10), 1911: (1, 30), 1912: (2, 18), 1913: (2,  6), 1914: (1, 26),
                     1915: (1, 14), 1916: (2,  4), 1917: (1, 23), 1918: (2, 11), 1919: (2,  1),
                     1920: (2, 20), 1921: (2,  8), 1922: (1, 28), 1923: (2, 16), 1924: (2,  5),
                     1925: (1, 24), 1926: (2, 13), 1927: (2,  2), 1928: (1, 23), 1929: (2, 10),
                     1930: (1, 30), 1931: (2, 17), 1932: (2,  6), 1933: (1, 26), 1934: (2, 14),
                     1935: (2,  4), 1936: (1, 24), 1937: (2, 11), 1938: (1, 31), 1939: (2, 19),
                     1940: (2,  8), 1941: (1, 27), 1942: (2, 15), 1943: (2,  4), 1944: (1, 25),
                     1945: (2, 13), 1946: (2,  1), 1947: (1, 22), 1948: (2, 10), 1949: (1, 29),
                     1950: (2, 17), 1951: (2,  6), 1952: (1, 27), 1953: (2, 14), 1954: (2,  3),
                     1955: (1, 24), 1956: (2, 12), 1957: (1, 31), 1958: (2, 18), 1959: (2,  8),
                     1960: (1, 28), 1961: (2, 15), 1962: (2,  5), 1963: (1, 25), 1964: (2, 13),
                     1965: (2,  2), 1966: (1, 21), 1967: (2,  9), 1968: (1, 30), 1969: (2, 17),
                     1970: (2,  6), 1971: (1, 27), 1972: (2, 15), 1973: (2,  3), 1974: (1, 23),
                     1975: (2, 11), 1976: (1, 31), 1977: (2, 18), 1978: (2,  7), 1979: (1, 28),
                     1980: (2, 16), 1981: (2,  5), 1982: (1, 25), 1983: (1, 13), 1984: (2,  2),
                     1985: (2, 20), 1986: (2,  9), 1987: (1, 29), 1988: (2, 17), 1989: (2,  6),
                     1990: (1, 27), 1991: (2, 15), 1992: (2,  4), 1993: (1, 23), 1994: (2, 10),
                     1995: (1, 31), 1996: (2, 19), 1997: (2,  7), 1998: (1, 28), 1999: (2, 16),
                     2000: (2,  5), 2001: (1, 24), 2002: (2, 12), 2003: (2,  1), 2004: (1, 22),
                     2005: (2,  9), 2006: (1, 29), 2007: (2, 18), 2008: (2,  7), 2009: (1, 26),
                     2010: (2, 14), 2011: (2,  3), 2012: (1, 23), 2013: (2, 10), 2014: (1, 31),
                     2015: (2, 19), 2016: (2,  8), 2017: (1, 28), 2018: (2, 16), 2019: (2,  5),
                     2020: (1, 25), 2021: (2, 12), 2022: (2,  1), 2023: (1, 22), 2024: (2, 10),
                     2025: (1, 29), 2026: (2, 17), 2027: (2,  6), 2028: (1, 26), 2029: (2, 13),
                     2030: (2,  3)
                     }


def is_int_in_range(value, lower_bound, upper_bound):
    """
    Checks if the given value is an integer that falls between the
    lower and the upper bounds.
    :param value: the checked value.
    :param lower_bound: an integer, representing the lower bound 
    (it's included in the range)
    :param upper_bound: an integer, representing the upper bound 
    (it's also included in the range)
    :return: None
    """
    assert isinstance(value, int)
    assert lower_bound <= value <= upper_bound

def check_birth_year(birth_year, birth_month, birth_day):
    """
    Checks if someone's birth was before the Chinese New Year or after.
    If it was before, decreases their birth year by 1, considering it
    as the previous year.
    :param birth_year: the year of someone's birth
    :param birth_month: the month of their birth (written as an integer)
    :param birth_day: the day of their birth
    :return: the person's birth year or the person's birth year minus 1.
    """
    is_int_in_range(birth_year, 1900, 2030)
    is_int_in_range(birth_month, 1, 12)
    is_int_in_range(birth_day, 1, 31)

    new_year_month = chinese_new_years[birth_year][0]
    new_year_day = chinese_new_years[birth_year][1]

    if birth_month < new_year_month:
        return birth_year - 1
    elif birth_month == new_year_month and birth_day < new_year_day:
        return birth_year - 1
    else:
        return birth_year


class DatedKP(KnowledgePiece, ABC):
    """A knowledge piece that includes someone's birthdate (year, month, day)
    as parameters."""
    def __init__(self, birth_year, birth_month, birth_day):
        self.birth_year = check_birth_year(birth_year, birth_month, birth_day)
        super().__init__()


class KPWithImages(DatedKP, ABC):
    """A knowledge piece that includes images."""
    images = {}

    def __init__(self, birth_year, birth_month, birth_day):
        super().__init__(birth_year, birth_month, birth_day)
        self.image = self.map_image()

    def map_image(self):
        return self.images.get(self.evaluate(), -1)


class GenderedKP(DatedKP, ABC):
    """A dated knowledge piece that includes someone's biological sex as
    one of the parameters."""
    def __init__(self, birth_year, biological_sex, birth_month, birth_day):
        self.biological_sex = biological_sex
        super().__init__(birth_year, birth_month, birth_day)

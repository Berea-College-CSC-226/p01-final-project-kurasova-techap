######################################################################
# Authors: Artem Kurasov
# Username: kurasova
#
# Assignment: P01 - Final Project
#
# Purpose: Writing code for the Zodiac Sign Compatibility class, which will
# evaluate the compatibility between two people based on their zodiac signs
######################################################################
# Acknowledgments:
#   Used Wikipedia for ZSC_table: https://en.wikipedia.org/wiki/Chinese_zodiac
#   (Accessed on April 19, 2026)
######################################################################

from AbstractClasses import CompatibilityKP

# The indices of rows and columns match the numbers in
# the zodiac_signs dictionary (which is right below).

zodiac_signs = {
        "Monkey":   0,
        "Rooster":  1,
        "Dog":      2,
        "Pig":      3,
        "Rat":      4,
        "Ox":       5,
        "Tiger":    6,
        "Rabbit":   7,
        "Dragon":   8,
        "Snake":    9,
        "Horse":    10,
        "Goat":     11
    }

# For example, the cell in column 0 and row 1 represents
# the relationship between a Monkey and a Rooster.

ZSC_table = (
    ( 0,  0,  0, -2,  2,  0, -1,  0,  2,  1,  0,  0),
    ( 0, -3, -2,  0,  0,  2,  0, -1,  1,  2,  0,  0),
    ( 0, -2,  0,  0,  0,  0,  2,  1, -1,  0,  2,  0),
    (-2,  0,  0, -3,  0,  0,  1,  2,  0, -1,  0,  2),
    ( 2,  0,  0,  0,  0,  1,  0, -3,  2,  0, -1, -2),
    ( 0,  2,  0,  0,  1,  0,  0, -3,  0,  2, -2, -1),
    (-1,  0,  2,  1,  0,  0,  0,  0,  0, -2,  2,  0),
    ( 0, -1,  1,  2, -2,  0,  0,  0, -2,  0,  0,  2),
    ( 2,  1, -1,  0,  2,  0,  0, -2, -3,  0,  0,  0),
    ( 1,  2,  0, -1,  0,  2, -2,  0,  0,  0,  0,  0),
    ( 0,  0,  2,  0, -1, -2,  2,  0,  0,  0,  0,  1),
    ( 0,  0,  0,  2, -2, -1,  0,  2,  0,  0,  1,  0),
)

class ZodiacSignCompatibility(CompatibilityKP):

    # In the ZodiacSignCompatibility class:
    # -3 represents Punishment Groups;   (THE WORST MATCHES!)
    # -2 represents Harming Groups;
    # -1 represents Offending Groups;
    #  0 represents Average Matches;     (NEUTRAL MATCHES)
    #  1 represents Six Harmonies;
    #  2 represents Four Trines.         (THE BEST MATCHES!)

    description_dict = {
        -3: "Regarding the person you have chosen as a companion, I have unfortunate news for you. Not only "
            "are you incompatible with them, but also you two are in the punishment group, which is worse than harming "
            "and offending. There is no way for you to be together!",
        -2: "When it comes to the person you have chosen as a companion, you are not compatible with them"
            "because you two are in a Harming Group.",
        -1: "Regarding the person you have chosen as a companion, you are not very compatible as you "
            "two are in an Offending Group.",
         0: "Regarding the person you have chosen as a companion, you are a Neutral match.",
         1: "Regarding the person you have chosen as a companion, you are highly compatible for intimate relationships (Six Harmonies).",
         2: "Regarding the person you have chosen as a companion, you are highly Compatible as a teammate or a business partner (Four Trines)."
    }

    def evaluate(self):
        self.value = ZSC_table[zodiac_signs[self.person_1.zodiac_sign]][zodiac_signs[self.person_2.zodiac_sign]]
        return self.value
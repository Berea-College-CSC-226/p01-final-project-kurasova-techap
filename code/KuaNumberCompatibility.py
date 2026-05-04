#####################################################################
# Authors: Artem Kurasov
# Username: kurasova
#
# Assignment: P01 - Final Project
#
# Purpose: Writing code for the Kua Number Compatibility class, which
# will compare two people based on their Kua numbers
######################################################################
# Acknowledgments:
#   More on Kua Number Compatibility: https://www.karmaweather.com/well-being/feng-shui/bagua-kua-number
######################################################################

from AbstractClasses import CompatibilityKP

# The indices of rows and columns match the Kua Numbers
# For example, the cell in column 1 and row 2 represents
# the relationship between Kua number 1 and Kua number 2.

# Because the same Kua numbers have the same directions,
# we can state that their connection can be considered love (2).

KNC_table = (
    ( 0,  0,  0,  0,  0,  0,  0,  0,  0,  0),
    ( 0,  2, -2, -1, -1,  0,  1,  1, -2,  2),
    ( 0, -2,  2, -2, -2,  0, -1,  1,  2, -1),
    ( 0, -1, -2,  2,  1,  0, -2,  2, -1,  1),
    ( 0, -1, -2,  1,  2,  0,  2, -2, -2,  1),
    ( 0,  0,  0,  0,  0,  0,  0,  0,  0,  0),
    ( 0,  1, -1, -2,  2,  0,  2,  1,  1, -2),
    ( 0,  1,  1,  2, -2,  0,  1,  2, -1, -2),
    ( 0, -2,  2, -1, -2,  0,  1, -1,  2,  2),
    ( 0,  2, -1,  1,  1,  0, -2, -2,  2,  2)
)


class KuaNumberCompatibility(CompatibilityKP):

    # In the KuaNumberCompatibility class:
    # -2 represents Incompatible Relationships;     (THE WORST MATCHES!)
    # -1 represents Neutral Relationships;
    #  0 represents... Nothing (it's for 0 and 5, which cannot be Kua numbers);
    #  1 represents Friendships;
    #  2 represents Love <3.                        (THE BEST MATCHES!)

    description_dict = {
         2: "Meanwhile, if we look at your partner's Kua Number, you are highly compatible with them for a romantic relationship"
            "if you put everything to the right your in your house.",
         1: "Meanwhile, if we look at your partner's Kua Number, you are highly compatible with them for a friendship"
            "if you follow the Feng Shui rules.",
        -1: "Meanwhile, if we look at your partner's Kua Number, you might have a very neutral relationship,",
        -2: "Meanwhile, if we look at your partner's Kua Number, you can't live with them in the same house: "
            " you two are incompatible.",
    }

    def evaluate(self):
        self.value = KNC_table[self.person_1.kua_number][self.person_2.kua_number]
        return self.value
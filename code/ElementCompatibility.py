######################################################################
# Authors: Pride Akana Techa
# Username: techap
#
# Assignment: P01 - Final Project
#
# Purpose: A class that returns your element from Chinese Metaphysics,
# the image representation, and a brief description of the characteristics
# of your element.
#
# Acknowledgements:
# Article on how to evaluate your element according to Chinese Metaphysics: https://www.yourtango.com/zodiac/chinese-zodiac-elements
#
#
######################################################################

from AbstractClasses import CompatibilityKP
class ElementCompatibility(CompatibilityKP):

# This table shows the element compatibility between two people based off the last digit of their birth year.
# -1 represents "Not Compatible: elements form part of the destructive cycle."
# 1 represents "Compatible: the same elements."
# 2 represents "Highly Compatible: elements form part of the constructive cycle."

    EC_table = (
    (1, 1, 2, 2, -1, -1, -1, -1, 2, 2),
    (1, 1, 2, 2, -1, -1, -1, -1, 2, 2),
    (2, 2, 1, 1, 2, 2, -1, -1, -1, -1),
    (2, 2, 1, 1, 2, 2, -1, -1, -1, -1),
    (-1, -1, 2, 2, 1, 1, 2, 2, -1, -1),
    (-1, -1, 2, 2, 1, 1, 2, 2, -1, -1),
    (-1, -1, -1, -1, 2, 2, 1, 1, 2, 2),
    (-1, -1, -1, -1, 2, 2, 1, 1, 2, 2),
    (2, 2, -1, -1, -1, -1, 2, 2, 1, 1),
    (2, 2, -1, -1, -1, -1, 2, 2, 1, 1)
    )

    description_dict = {
        2: "Looking at your elements, we can state that you guys are highly compatible (Part of the constructive cycle).",
        1: "Looking at your elements, we can say that you two are compatible/stable: it is what we call a mutual relationship (the same elements).",
        -1: "If we take a look at your elements, we can state that Not compatible, being part of the destructive cycle."
    }

    def evaluate(self):
        """
        Determines the element compatibility between two people.
        :return:
        """
        self.person_1.birth_year = str(self.person_1.birth_year )
        self.person_2.birth_year = str(self.person_2.birth_year)
        self.value = self.EC_table[int(self.person_1.birth_year[-1])][int(self.person_2.birth_year[-1])]
        return self.value



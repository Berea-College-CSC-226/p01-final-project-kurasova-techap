######################################################################
# Authors: Pride Akana Techa
# Username: techap
#
# Assignment: P01 - Final Project
#
# Purpose: A class that returns your Kua Number from Chinese Metaphysics,
# and a brief description of the characteristics of your Kua Number.
#
# Acknowledgements:
# Video and article on how to calculate Kua Number
# - https://www.youtube.com/shorts/cy6r7imx4Uo
# - https://wehomzfurn.com/blogs/decoration-ideas/how-to-calculate-your-kua-number-a-complete-guide-for-2026
#
######################################################################

from AbstractClasses import GenderedKP
class KuaNumber(GenderedKP):
    def evaluate(self):
        """
        Calculates the user's Kua Number
        :return: the Kua number
        """
        # Get the last two digits of the birth year and sum them up.
        kua_number = str(self.birth_year)
        kua_number = int(kua_number[-1]) + int(kua_number[-2])

        # Check whether the kua number contains two digits, and reduces to one digit if it does.
        while kua_number >= 10:
            kua_number = str(kua_number)
            kua_number = int(kua_number[0]) + int(kua_number[1])

        # Check the birth year and gender to determine the final kua number.
        if self.birth_year < 2000:
            if self.biological_sex == "male":
                kua_number = 10 - kua_number
            else:
                kua_number += 5
        else:
            if self.biological_sex == "male":
                kua_number = 9 - kua_number
            else:
                kua_number += 6

        # Reduce to a single digit again if the kua number has two digits
        while kua_number >= 10:
            kua_number = str(kua_number)
            kua_number = int(kua_number[0]) + int(kua_number[1])

        # Since 5 is not a kua number in Chinese Metaphysics, we convert it to the appropriate digits according to Feng Chui.
        if kua_number == 5:
            if self.biological_sex == "male":
                kua_number = 2
            else:
                kua_number = 8

        self.value = kua_number

def main():
    """
    Determines the user's zodiac sign and a brief description of it.
    :return: None
    """
    user1 = KuaNumber(2004,"male", 5, 25)
    print(user1.value)

if __name__ == "__main__":
    main()



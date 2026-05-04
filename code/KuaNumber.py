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

    description_dict = {
        1: "Based on your Kua number, your prosperity side is on the Southeast; your health side is on the east; your love is south; and your career is North. Meanwhile, the sides you should avoid "
           "include the West (Accidents), Northeast (Five Ghosts), Northwest (Six killings), and especially Southwest (Total Loss).",
        2: "Based on your Kua number, your prosperity side is on the Northeast; your health side is on the West; your love is Northwest; and your career is Southwest. Meanwhile, the sides you should avoid "
           "include the East (Accidents), Southeast (Five Ghosts), South (Six killings), and especially North (Total Loss).",
        3: "Based on your Kua number, your prosperity side is on the South; your health side is on the North; your love is Southeast; and your career is East. Meanwhile, the sides you should avoid "
           "include the Southwest (Accidents), Northwest (Five Ghosts), Northeast (Six killings), and especially West (Total Loss).",
        4: "Based on your Kua number, your prosperity side is on the North; your health side is on the South; your love is East; and your career is Southeast. Meanwhile, the sides you should avoid "
           "include the Northwest (Accidents), Southwest (Five Ghosts), West (Six killings), and especially Northeast (Total Loss).",
        6: "Based on your Kua number, your prosperity side is on the West; your health side is on the Northeast; your love is Southwest; and your career is Northwest. Meanwhile, the sides you should avoid "
           "include the Southeast (Accidents), East (Five Ghosts), North (Six killings), and especially South (Total Loss).",
        7: "Based on your Kua number, your prosperity side is on the Northwest; your health side is on the Southwest; your love is Northeast; and your career is West. Meanwhile, the sides you should avoid "
           "include the North (Accidents), South (Five Ghosts), Southeast (Six killings), and especially East (Total Loss).",
        8: "Based on your Kua number, your prosperity side is on the Southwest; your health side is on the Northwest; your love is West; and your career is Northeast. Meanwhile, the sides you should avoid "
           "include the South (Accidents), North (Five Ghosts), East (Six killings), and especially Southeast (Total Loss).",
        9: "Based on your Kua number, your prosperity side is on the East; your health side is on the  Southeast; your love is North; and your career is South. Meanwhile, the sides you should avoid "
           "include the Northeast (Accidents), West (Five Ghosts), Southwest (Six killings), and especially Northwest (Total Loss)."
    }

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
        return kua_number



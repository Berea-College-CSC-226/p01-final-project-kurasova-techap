#####################################################################
# Authors: Artem Kurasov
# Username: kurasova
#
# Assignment: P01 - Final Project
#
# Purpose: Writing code for the Report class, which
# will display the report of a specific person
######################################################################
# Acknowledgments:
#   Adding Images to TKInter: https://www.geeksforgeeks.org/python/how-to-add-an-image-in-tkinter/
#   CustomTKInter Documentation: https://customtkinter.tomschimansky.com/
######################################################################

import customtkinter as ctk
from PIL import Image

class Report:
    def __init__(self, screen):

        self.frame = ctk.CTkFrame(screen)

        self.name_label = None
        self.zodiac_sign_label = None
        self.element_label = None
        self.kua_number_label = None

        self.name = None
        self.zodiac_sign = None
        self.element = None
        self.kua_number = None

        self.zodiac_sign_image = None
        self.zsi_label = None
        self.element_image = None
        self.ei_label = None

        self.personal_description = None

    def update_report(self, screen, person):

        self.name_label = ctk.CTkLabel(screen, text = "Name: ", font = ("Arial", 15, "bold"))
        self.zodiac_sign_label = ctk.CTkLabel(screen, text = "Element: ", font = ("Arial", 15, "bold"))
        self.element_label = ctk.CTkLabel(screen, text = "Zodiac Sign: ", font = ("Arial", 15, "bold"))
        self.kua_number_label = ctk.CTkLabel(screen, text = "Kua Number: ", font = ("Arial", 15, "bold"))

        self.name = ctk.CTkLabel(screen, text = person.name, font = ("Arial", 15))
        self.zodiac_sign = ctk.CTkLabel(screen, text = person.zodiac_sign, font = ("Arial", 15))
        self.element = ctk.CTkLabel(screen, text = person.element, font = ("Arial", 15))
        self.kua_number = ctk.CTkLabel(screen, text = person.kua_number, font = ("Arial", 15))

        self.zodiac_sign_image = ctk.CTkImage(light_image = Image.open(person.zodiac_sign_image),
                                              size = (100, 100))
        self.zsi_label = ctk.CTkLabel(screen, image = self.zodiac_sign_image, text = "")

        self.element_image = ctk.CTkImage(light_image = Image.open(person.element_image),
                                              size = (100, 100))
        self.ei_label = ctk.CTkLabel(screen, image = self.element_image, text = "")

        self.personal_description = ctk.CTkLabel(screen, text = person.description)

        self.name_label.place(x = 600, y = 50)
        self.zodiac_sign_label.place(x = 600, y = 75)
        self.element_label.place(x = 600, y = 100)
        self.kua_number_label.place(x = 600, y = 125)

        self.name.place(x = 700, y = 50)
        self.zodiac_sign.place(x = 700, y = 75)
        self.element.place(x = 700, y = 100)
        self.kua_number.place(x = 700, y = 125)

        self.zsi_label.place(x = 750, y = 50)
        self.ei_label.place(x = 860, y = 50)

        self.personal_description.place(x = 500, y = 110)




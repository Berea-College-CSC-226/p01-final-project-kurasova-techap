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
from Compatibility import Compatibility


class Report:
    def __init__(self, screen):

        self.frame = ctk.CTkFrame(screen)

        self.name_label                 = None
        self.zodiac_sign_label          = None
        self.element_label              = None
        self.kua_number_label           = None

        self.name                       = None
        self.zodiac_sign                = None
        self.element                    = None
        self.kua_number                 = None

        self.zodiac_sign_image          = None
        self.zsi_label                  = None
        self.element_image              = None
        self.ei_label                   = None

        self.description                = None

    def update_report(self, screen, person):
        """
        Updates the report (No descriptions)
        :param screen: the window the update is in.
        :param person: the person whose stats we want to display
        :return: None
        """
        canvas = ctk.CTkCanvas(screen, width = 810, height = 500, bg = "white", highlightthickness = 0, borderwidth = 0)
        canvas.place(x = 990, y = 0)

        self.name_label = ctk.CTkLabel(screen, text = "Name: ", font = ("Arial", 15, "bold"))
        self.zodiac_sign_label = ctk.CTkLabel(screen, text = "Zodiac Sign: ", font = ("Arial", 15, "bold"))
        self.element_label = ctk.CTkLabel(screen, text = "Element: ", font = ("Arial", 15, "bold"))
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

        self.name_label.place(x = 700, y = 50)
        self.zodiac_sign_label.place(x = 700, y = 75)
        self.element_label.place(x = 700, y = 100)
        self.kua_number_label.place(x = 700, y = 125)

        self.name.place(x = 800, y = 50)
        self.zodiac_sign.place(x = 800, y = 75)
        self.element.place(x = 800, y = 100)
        self.kua_number.place(x = 800, y = 125)

        self.zsi_label.place(x = 950, y = 50)
        self.ei_label.place(x = 1060, y = 50)

    def update_personal_report(self, screen, person):
        """
        Updates the report with a personal description.
        :param screen: the window the update is in.
        :param person: the person whose stats we want to display
        :return: None
        """
        self.update_report(screen, person)
        self.description = ctk.CTkLabel(screen, text=person.description)
        self.description.place(x=500, y=110)

    def update_compatibility_report(self, screen, person1, person2):
        """
        Updates the report with a compatibility description.
        :param screen: the window the update is in.
        :param person1: the person whose stats we want to display.
        :param person2: the person we compare person1 to.
        :return: None
                """
        self.update_report(screen, person1)
        compatibility = Compatibility(person1, person2)
        self.description = ctk.CTkLabel(screen, text = str(person1.description) + str(compatibility.description), wraplength = 300)
        self.update_report(screen, person1)






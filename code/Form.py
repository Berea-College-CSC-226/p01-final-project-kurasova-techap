######################################################################
# Authors: Pride Akana Techa
# Username: techap
#
# Assignment: P01 - Final Project
#
# Purpose: A class that creates a form foe the user to fill in their information
# like year of birth, month of birth, birthday, and gender, and that of the
# other person they want to compare with.
#
# Acknowledgements:
#
#
#
######################################################################

import customtkinter as ctk

months = ["January", "February", "March", "April",
          "May", "June", "July", "August", "September",
          "October", "November", "December"]

years = []
for year in range(1900, 2031):
    years.append(str(year))

days = []
for day in range(1, 32):
    days.append(str(day))

class Form:
    def __init__(self, screen):
        """
        Creates a form for the user to enter their information and that of their beloved.
        :param screen: UI object - where the form will be displayed.
        """
        self.font = ctk.CTkFont(size = 15)
        self.frame = ctk.CTkFrame(screen)
        self.name = ctk.CTkLabel(screen, text = "Your Name:", font=("Arial", 15, "bold"))
        self.name.place(x = 50, y = 50)
        self.name_entry = ctk.CTkEntry(screen, width= 150, height = 20, font = self.font )
        self.name_entry.place(x = 50, y = 90)
        self.DOB_text = ctk.CTkLabel(screen, text = "Date of Birth:", font = ("Arial", 15, "bold")) # Label for date of birth.
        self.DOB_text.place(x = 50, y = 130)
        self.birth_month_combo_box = ctk.CTkComboBox(screen, values = months, width = 110)
        self.birth_month_combo_box.place(x = 50, y = 170)
        self.birth_day_combo_box = ctk.CTkComboBox(screen, values = days, width = 60)
        self.birth_day_combo_box.place(x = 170, y = 170)
        self.birth_year_combo_box = ctk.CTkComboBox(screen, values = years, width = 85)
        self.birth_year_combo_box.place(x = 240, y = 170)
        self.gender_text = ctk.CTkLabel(screen, text = "Biological Sex:", font = ("Arial", 15, "bold"))
        self.gender_text.place(x = 50, y = 210)

        self.radio_var = ctk.StringVar(value="male")
        self.male_gender_button = ctk.CTkRadioButton(screen, text = "male", variable = self.radio_var, value = "male" )
        self.male_gender_button.place(x=50, y=250)
        self.female_gender_button = ctk.CTkRadioButton(screen, text = "female",variable = self.radio_var, value = "female")
        self.female_gender_button.place(x=50, y=280)






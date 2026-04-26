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
from customtkinter import CTk, CTkLabel

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
        self.frame = ctk.CTkFrame(screen)
        self.name = ctk.CTkLabel(screen, text = "Your Name:")
        self.name.place(x = 50, y = 50)
        self.name_entry = ctk.CTkEntry(screen)
        self.name_entry.place(x= 50, y = 70)
        self.DOB_text = ctk.CTkLabel(screen, text = "Date of Birth:") # Label for date of birth.
        self.DOB_text.place(x=50, y=90)
        self.birth_year_combo_box = ctk.CTkComboBox(screen, values = years)
        self.birth_year_combo_box.place(x=70, y=110)
        self.birth_month_combo_box = ctk.CTkComboBox(screen, values=months)
        self.birth_month_combo_box.place(x=50, y=110)
        self.birth_day_combo_box = ctk.CTkComboBox(screen, values=days)
        self.birth_day_combo_box.place(x=60, y=110)
        self.gender_text = ctk.CTkLabel(screen, text = "Biological Sex:")
        self.gender_text.place(x=50, y=130)
        self.male_gender_button = ctk.CTkRadioButton(screen, text = "male", value = "male" )
        self.male_gender_button.place(x=50, y=150)
        self.female_gender_button = ctk.CTkRadioButton(screen, text = "female", value = "female")
        self.female_gender_button.place(x=50, y=160)
        self.submit_button = ctk.CTkButton(screen, text = "Submit")
        self.submit_button.place(x=50, y=190)
        self.add_more_button = ctk.CTkButton(screen, text = "Add more")
        self.add_more_button.place(x=50, y=190)

    def submit(self):
        pass




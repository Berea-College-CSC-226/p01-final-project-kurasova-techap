######################################################################
# Authors: Pride Akana Techa
# Username: techap
#
# Assignment: P01 - Final Project
#
# Purpose: A class that creates the user interface, and interacts with
# the form and report class, allowing the user to enter their information
# see their results displayed on the screen
#
# Acknowledgements:
#
#
#
######################################################################

import customtkinter as ctk
from Form import Form
from Report import Report

class UI(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("1000x500")
        self.title("Chinese Metaphysics")

        self.users_form = Form(self)

        self.users_report = Report()

        self.submit_button = ctk.CTkButton(self, text="Submit", command=self.submit)
        self.submit_button.place(x=50, y=320)
        self.add_more_button = ctk.CTkButton(self, text="Add more", command=self.add_more)
        self.add_more_button.place(x=200, y=320)
        # self.other_persons_form = Form()
        # self.users_report =

    def submit(self):
        name = self.users_form.name_entry.get()
        birth_year = self.users_form.birth_year_combo_box.get()
        birth_month = self.users_form.birth_month_combo_box.get()
        birth_day = self.users_form.birth_day_combo_box.get()
        biological_sex = self.users_form.radio_var.get()
        person = (name, birth_year, birth_month, birth_day, biological_sex)
        self.users_report.update(self, person)

    def add_more(self):
        pass

    def exit(self):
       self.quit()

UI_object = UI()
UI_object.mainloop()
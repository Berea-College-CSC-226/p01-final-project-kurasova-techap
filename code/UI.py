######################################################################
# Authors: Pride Akana Techa
# Username: techap
#
# Assignment: P01 - Final Project
#
# Purpose: A class that creates the user interface, and interacts with
# the form and report class, allowing the user to enter their information
# and see their results displayed on the screen.
#
# Acknowledgements:
# - Website on how to use custom tkinter:
#   https://customtkinter.tomschimansky.com/documentation/windows/window/
# - Changing the background image:
#   https://stackoverflow.com/questions/2744795/background-color-for-tk-in-python
# - Disabling resizability of the window:
#   https://www.tutorialspoint.com/article/how-can-i-prevent-a-window-from-being-resized-with-tkinter
######################################################################

import customtkinter as ctk
from Form import Form
from Report import Report
from Person import Person

class UI(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("1200x600")
        self.title("Chinese Metaphysics")
        self.configure(fg_color = "white")
        self.resizable(False, False)

        self.users_form = Form(self)
        self.users_report = Report(self)

        self.submit_button = ctk.CTkButton(self, text="Submit", command=self.submit)
        self.submit_button.place(x = 50, y = 320)
        self.add_more_button = ctk.CTkButton(self, text="Add more", command=self.add_more)
        self.add_more_button.place(x = 200, y = 320)

        self.other_persons_form = None
        self.submit_2_button = ctk.CTkButton(self, text="Submit", command=self.submit_2)

    month_value = {"January": 1, "February": 2, "March": 3, "April": 4, "May": 5, "June": 6,
                   "July": 7, "August": 8, "September": 9, "October": 10, "November": 11, "December": 12}

    def __get_data(self, form):
        try:
            name = form.name_entry.get()
            birth_year = int(form.birth_year_combo_box.get())
            birth_month = self.month_value[form.birth_month_combo_box.get()]
            birth_day = int(form.birth_day_combo_box.get())
            biological_sex = form.radio_var.get()
            return Person(name, birth_year, biological_sex, birth_month, birth_day)
        except ValueError:
            ...

    def submit(self):
        person = self.__get_data(self.users_form)
        try:
            self.users_report.update_personal_report(self, person)
        except AttributeError:
            ...

    def submit_2(self):
        person1 = self.__get_data(self.users_form)
        person2 = self.__get_data(self.other_persons_form)
        try:
            self.users_report.update_compatibility_report(self, person1, person2)
        except AssertionError:
            ...

    def add_more(self):
        self.other_persons_form = Form(self, x_shift = 330, nameLabel= "Your Partner's Name:")
        self.add_more_button.destroy()
        self.submit_button.destroy()
        self.submit_2_button.place(x=380, y=320)

    def exit(self):
       self.quit()

UI_object = UI()
UI_object.mainloop()
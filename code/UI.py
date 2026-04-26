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
class UI(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.geometry("1000x500")
        self.title("Chinese Metaphysics")

        self.users_form = Form(self)
        # self.other_persons_form = Form()
        # self.users_report =

    def exit(self):
       self.quit()

UI_object = UI()
UI_object.mainloop()
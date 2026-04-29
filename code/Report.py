# https://www.geeksforgeeks.org/python/how-to-add-an-image-in-tkinter/


import customtkinter as ctk

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
        self.element_image = None

        self.personal_description = None

    def update_report(self, screen, person):

        self.name_label = ctk.CTkLabel(screen, text = "Name: ")
        self.zodiac_sign_label = ctk.CTkLabel(screen, text = "Element: ")
        self.element_label = ctk.CTkLabel(screen, text = "Zodiac Sign: ")
        self.kua_number_label = ctk.CTkLabel(screen, text = "Kua Number: ")

        self.name = ctk.CTkLabel(screen, text = person.name)
        self.zodiac_sign = ctk.CTkLabel(screen, text = person.zodiac_sign)
        self.element = ctk.CTkLabel(screen, text = person.element)
        self.kua_number = ctk.CTkLabel(screen, text = person.kua_number)

        #self.zodiac_sign_image = ctk.CTkImage(screen)
        #self.element_image = ctk.CTkImage(screen)

        self.personal_description = ctk.CTkLabel(screen, text = person.description)

        self.name_label.place(x = 500, y = 10)
        self.zodiac_sign_label.place(x = 500, y = 20)
        self.element_label.place(x = 500, y = 30)
        self.kua_number_label.place(x = 500, y = 40)

        self.name.place(x = 500, y = 50)
        self.zodiac_sign.place(x = 500, y = 60)
        self.element.place(x = 500, y = 70)
        self.kua_number.place(x = 500, y = 80)

        #self.zodiac_sign_image.place(x = 500, y = 90)
        #self.element_image.place(x = 500, y = 100)

        self.personal_description.place(x = 500, y = 110)




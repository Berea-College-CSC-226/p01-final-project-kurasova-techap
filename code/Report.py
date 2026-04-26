import customtkinter as ctk

class Report:
    def __init__(self, screen):
        self.frame = ctk.CTkFrame(screen)

        self.name = None
        self.zodiac_sign = None
        self.element = None
        self.kua_number = None

        self.zodiac_sign_image = None
        self.element_image = None

        self.personal_description = None
        self.comparison_description = None

    def update_report(self, screen):
        self.name = ctk.CTkLabel(screen)
        self.zodiac_sign = ctk.CTkLabel(screen)
        self.element = ctk.CTkLabel(screen)
        self.kua_number = ctk.CTkLabel(screen)

        self.zodiac_sign_image = ctk.CTkImage(screen)
        self.element_image = ctk.CTkImage(screen)

        self.personal_description = ctk.CTkLabel(screen)
        self.comparison_description = ctk.CTkLabel(screen)


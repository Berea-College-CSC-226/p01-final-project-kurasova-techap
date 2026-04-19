from AbstractClasses import KPWithImages
class ZodiacSign(KPWithImages):
    zodiac_sign = {
        0: "Monkey",
        1: "Rooster",
        2: "Dog",
        3: "Pig",
        4: "Rat",
        5: "Ox",
        6: "Tiger",
        7: "Rabbit",
        8: "Dragon",
        9: "Snake",
        10: "Horse",
        11: "Goat"
    }
    description_dict = {
        "Monkey": "",
        "Rooster": "",
        "Dog": "",
        "Pig": "",
        "Rat": "",
        "Ox":"",
        "Tiger": "",
        "Rabbit": "",
        "Dragon": "",
        "Snake": "",
        "Horse": "",
        "Goat": ""

    }
    images = {
        "Monkey": "",
        "Rooster": "",
        "Dog": "",
        "Pig": "",
        "Rat": "",
        "Ox": "",
        "Tiger": "",
        "Rabbit": "",
        "Dragon": "",
        "Snake": "",
        "Horse": "",
        "Goat": ""
    }



    def evaluate(self):
        """
        Evaluates the zodiac sign of the user.
        :return: the user's zodiac sign and its description.
        """
        self.value = self.zodiac_sign[self.birth_year % 12]
        return self.value

def main():
    """
    Determines the user's zodiac sign and a brief description of it.
    :return: None
    """
    user1 = ZodiacSign(2004,5, 25)
    print(user1.value)

if __name__ == "__main__":
    main()

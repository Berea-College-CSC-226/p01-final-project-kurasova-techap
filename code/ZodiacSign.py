######################################################################
# Authors: Pride Akana Techa
# Username: techap
#
# Assignment: P01 - Final Project
#
# Purpose: A class that returns your Chinese Zodiac sign, the image
# representation, and a brief description of the characteristics
# of your sign.
#
# Acknowledgements:
# HW01: Breaking Bad
# Website for the meanings of the 12 animals in Chinese Zodiac Sign
# - https://migaku.com/blog/chinese/chinese-zodiac-animals-meanings#the-12-animals-in-chinese-calendar-and-what-they-actually-mean
#
######################################################################

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
        "Monkey": "The Entertaining Innovator: The monkey embodies intelligence and superior problem-solving skills. "
                  "People born in monkey years are considered to be witty, curious, and mischievous. Their curiosity drives"
                  "them to continuously learn new skills and keep life interesting. They are also known for their pranks. "
                  "Their lucky numbers are 1 and 8, and their lucky colors are white, blue, and gold.",

        "Rooster": "The Confident Perfectionist: Roosters are known for their brutal honesty, hard work, and observant"
                   "nature. They pay keen attention to details and they pride themselves in their freedom of speech. They"
                   "equally set high expectations for themselves and those around them. The lucky elements of the rooster"
                   "are the numbers 5, 7, and 8, and the colors gold, brown, and yellow.",

        "Dog": "The Loyal Friend: The dog represents loyalty, honesty, and justice. They are very protective of their love"
               "ones, and are also trustworthy, and straightforward. Their lucky numbers are 3, 4, and 9, and their lucky "
               "colors are red, green, and purple.",

        "Pig": "The Generous Optimist: Among the 12 animals in the Chinese zodiac, the pig symbolizes wealth, good fortune"
               "and honesty. People born in pig years are generous, optimistic, and genuine. They equally love to enjoy"
               "the pleasures of life. Their lucky elements are the numbers 2, 5, and 8 and the colors yellow, gray, brown,"
               "and gold.",

        "Rat": "The Clever Opportunist: According to Chinese culture, the rat won the zodiac race not because of its "
               "strength, but its intelligence. Therefore, the rat represents wisdom and wealth accumulation. People born "
               "in rat years turn to be charming and sociable. They are also good at noticing and taking advantage of "
               "opportunities others miss. The lucky elements of the rat are the numbers 2 and 3 and the colors blue, gold, and green.",

        "Ox":"The Dependable Worker: The ox is synonymous to diligence, strength, and reliability. Individuals born in "
             "ox years are known for their honesty and patience, they are people who are commited to their work and ensure "
             "that they complete whatever task they are working on, no matter how it difficult it is. The lucky elements "
             "of the ox are the numbers 1 and 9, with the colors white, yellow, and green.",

        "Tiger": "The Brave Leader: In Chinese culture, tigers are confident risktakers, competitive individuals, and "
                 "born leaders. They are known for their courage and power, hence they have a great affinity for tackling"
                 "challenging tasks and situations. Their lucky numbers are 1, 3, and 4, and their lucky colors are orange, "
                 "gray, and blue.",

        "Rabbit": "The Gentle Diplomat: Rabbits are highly known for their sensitivity, kindness, and elegance. They turn"
                  "to be compassionate and peaceful. This explains why they work well in diplomatic situations. The rabbit's "
                  "lucky elements are the numbers 3, 4, and 9, and the colors red, pink, purple, and blue.",

        "Dragon": "The Powerful Visionary: Dragons are considered to be the only mythical creatures in Chinese zodiac signs,"
                  "hence the luckiest animal. People born in dragon years are ambitious and highly confident to an extent"
                  "that portrays arrogance. The lucky elements for dragons are the numbers 1, 6, and 7 and the colors gold, "
                  "silver, and white.",

        "Snake": "The Wise Strategist: Snakes are clever, intuitive, and sophisticated. They work well in pressure intensive"
                 "environments while maintaining calmness. They monitor their environment before making any move, which"
                 "makes them very strategic in their thoughts and actions. the lucky colors for snakes are black, red, "
                 "and yellow, and their lucky numbers are 2, 8, and 9.",

        "Horse": "The Free Spirit: The Chinese zodiac horse is an epitome of energy. People born in horse years are associated "
                 "with independence, love and freedom. Their lucky elements are the colors yellow and green, with the"
                 "numbers 2, 3, and 7.",

        "Goat": "The Creative Soul: The goat embodies creativity, gentleness, and empathy, and they are sometimes referred to as "
                "sheep. Individuals born in goat years are good team players, supportive friends, artistic, and compassionate."
                "Their lucy elements are the numbers 2 and 7 and the colors brown, red, and purple."

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

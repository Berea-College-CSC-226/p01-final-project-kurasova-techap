######################################################################
# Authors: Pride Akana Techa
# Username: techap
#
# Assignment: P01 - Final Project
#
# Purpose: A class that returns your element from Chinese Metaphysics,
# the image representation, and a brief description of the characteristics
# of your element.
#
# Acknowledgements:
# Article on how to evaluate your element according to Chinese Metaphysics
# - https://shopceremonie.com/blog1/how-to-determine-your-elements
# Article on the meanings of the various elements
# - https://ohcomassagechairs.com/news-recognition/shiatsu-and-the-five-elements-theory/
######################################################################

from AbstractClasses import KPWithImages
class Element(KPWithImages):
    elements = {
        0: "Metal",
        1: "Metal",
        2: "Water",
        3: "Water",
        4: "Wood",
        5: "Wood",
        6: "Fire",
        7: "Fire",
        8: "Earth",
        9: "Earth"
    }
    description_dict = {
        "Metal": "Metal symbolizes clarity, strength, discipline, and precision. It goes hand in gloves with emotions of"
                 "grief and sadness, and its color is white.",
        "Water": "Water is an element that represents wisdom, fluidity, and adaptability. It is often associated with the"
                 "color blue, and emotions of fear and insecurity.",
        "Wood": "The wood element is a blend of two worlds, symbol of growth, creativity, alertness, and creativity."
                "Green comes up in the discussion of wood, as well as emotions of anger and frustration.",
        "Fire": "The fire element is synonymous to enthusiasm, warmth, passion, and flexibility. It is associated with the"
                "color red and emotions of joy and excitement.",
        "Earth": "Earth is a symbol of stability, nourishment, and grounding. Its color is yellow, and it is usually"
                 "associated with emotions of worry and overthinking."
    }

    images = {
        "Metal":    "../elements/metal.png",
        "Water":    "../elements/water.png",
        "Wood":     "../elements/wood.png",
        "Fire":     "../elements/fire.png",
        "Earth":    "../elements/earth.png"
    }

    def evaluate(self):
        """
        Evaluates the user's element.
        :return: the user's element and its description
        """
        self.birth_year = str(self.birth_year)
        self.value = self.elements[int(self.birth_year[-1])]
        return self.value


def main():
    """
    Determines the user's zodiac sign and a brief description of it.
    :return: None
    """
    user1 = Element(2004,5, 25)
    print(user1.value)

if __name__ == "__main__":
    main()
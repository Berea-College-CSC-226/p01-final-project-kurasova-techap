######################################################################
# Authors: Pride Akana Techa    TODO: Change this to your name
# Username: techap            TODO: Change this to your username
#
# Assignment: HW01: Breaking Bad
#
# Purpose: A program that returns your Chinese Zodiac animal given a
# birth year between (your birth year) and (your birth year + 11).
# Also prints your friend's animal, and your compatibility with that 
# friend's animal.
#
# Read the detailed notes about each task in the HW01 document.
######################################################################
# Acknowledgements:
#   Original Authors: Dr. Scott Heggen and Prof. Brian Schack
######################################################################

# (Required) Goal 1
# TODO Ask user for their birth year
birth_year = int(input("What year were you born in? "))
print(f"You were born in {birth_year}.")

# TODO Check the year using if conditionals, and print a witty message about the correct animal for that year.
# See the hw01_pets.py for examples

# Goals 1 needs to consider only the years between your birth year and the following 11 years.
# For example, Dr. Scott was born in 1982, so his submission of Goal 1 will consider the years 1982 to 1993.

######################################################################

if birth_year == 2004:
    print("You are a monkey!")
elif birth_year == 2005:
    print("You are a rooster!")
elif birth_year == 2006:
    print("You are a dog!")
elif birth_year == 2007:
    print("You are a pig!")
elif birth_year == 2008:
    print("You are a rat!")
elif birth_year == 2009:
    print("You are a an ox!")
elif birth_year == 2010:
    print("You are a tiger!")
elif birth_year == 2011:
    print("You are a rabbit!")
elif birth_year == 2012:
    print("You are a dragon!")
elif birth_year == 2013:
    print("You are a snake!")
elif birth_year == 2014:
    print("You are a horse!")
elif birth_year == 2015:
    print("You are a goat!")
else:
    print("Your birth year is not in the given range.")

# (Required) Goal 2
# TODO Ask the user for their friend's birth year

friend_birth_year = int(input("What year was your friend born in? "))
print(f"Your friend was born in {friend_birth_year}.")


# TODO Similar to above, check your friend's year using if conditionals,
#  and print a witty message the correct animal for that year


if friend_birth_year == 2004:
    print("Your friend is a monkey!")
elif friend_birth_year == 2005:
    print("Your friend is a rooster!")
elif friend_birth_year == 2006:
    print("Your friend is a dog!")
elif friend_birth_year == 2007:
    print("Your friend is a pig!")
elif friend_birth_year == 2008:
    print("Your friend is a rat!")
elif friend_birth_year == 2009:
    print("Your friend is an ox!")
elif friend_birth_year == 2010:
    print("Your friend is a tiger!")
elif friend_birth_year == 2011:
    print("Your friend is a rabbit!")
elif friend_birth_year == 2012:
    print("Your friend is a dragon!")
elif friend_birth_year == 2013:
    print("Your friend is a snake!")
elif friend_birth_year == 2014:
    print("Your friend is a horse!")
elif friend_birth_year == 2015:
    print("You friend is a goat!")
else:
    print("Your friend's birth year is not in the given range.")



######################################################################
# (Required) Goal 3
# TODO Check for compatibility between your birth year and your friend's birth year
# NOTE: You can always assume the first input is your birth year (i.e., 1982 for me).
# This way, you are not writing a ton of code to consider every possibility.
# In other words, only do one row of the sample compatibility table.

if friend_birth_year == 2007 or 2023:
    print("You guys are friends who don't see eye to eye. So are you guys really friends?:(")
elif friend_birth_year in [2012, 2008, 2013]:
    print("You guys are besties:)")
elif friend_birth_year in [2004, 2005, 2006, 2009, 2010, 2011, 2014, 2015]:
    print("You guys are just 'okay friends', nothing much.")


# TODO print a witty message if you are a Best match, Harmful match, or in between

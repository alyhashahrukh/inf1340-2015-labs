#!/usr/bin/env python3

""" Graded Lab #1 for Inf1340, Fall 2015 """

__author__ = 'Susan Sim'
__email__ = "ses@drsusansim.org"
__copyright__ = "2015 Susan Sim"
__license__ = "MIT License"


def vowels_and_consonants():
    letter = raw_input("Please enter a letter: ")

    if letter == "a":
        print ("Vowel")
    elif letter == "e":
        print ("Vowel")
    elif letter == "i":
        print ("Vowel")
    elif letter == "o":
        print ("Vowel")
    elif letter == "u":
        print ("Vowel")

    elif letter == "y":
        print ("Sometimes a vowel, sometimes a consonant.")

    else:
        print ("Consonant")

vowels_and_consonants()
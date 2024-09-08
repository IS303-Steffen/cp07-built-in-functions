# optional stuff that will clear the window each time you run it.
import os
import platform

def clear_screen():
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

clear_screen()

###########################
# START READING HERE
###########################


# See Chapter 9.3 for more examples.
# For time's sake, we'll only cover some of the
# more useful ones:

example_string = "  this is a sentence that Prof. Steffen wrote.  "

# upper()
# make example_string all upper case:


# lower()
# make example_string all lower case:


# strip()
# make example_string get rid of leading empty space:


# capitalize()
# make example_string's first chcaracter capitalized'
# hint, try combining with strip


# title()
# make example_string's first chcaracter capitalized'


# count()
# return number of times substring occurs in the string
example_string_2 = "Plumber Error Swimmer"
# how many times does "er" occur?


# can you do it to account for the capital "E"?



# find()
# find, returns the starting position of a substring:
# note this is a position, so it starts at 0
example_string_3 = "Let's get ready to rumble"


#split
# returns a list of strings based off of the character to split by
# return a list of words by splitting based on the underscores.
example_string_4 = "I_don't_want_the_underscores"


# replace
# replace every instance of "_" with " " in example_string_4



# len()
# how long is example_string_4


# using "in" with strings
example_string_5 = "nacho libre"
# if "ach" is in string_example_4, print "found it"


# if "chips" is not in string_example_4, print "not found"



# index of strings
# just like how lists can be accessed with an index
# you can access strings the same way:
example_string_6 = "Example of text"
# print only the 4th character of example_string_6


# print the 4th to the 10th character of example_string_6

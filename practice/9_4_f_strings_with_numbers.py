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

'''
When using f-strings, and you have an int or float inserted into the string,
You can use a colon : and then anything after the colon is instructions for
formatting the int/float. You can even round doing this.
'''

# Adding commas
# :,
# print "This is my formatted number {example_number}
# but make it have commas by adding :,
example_number = 100456.3257


# rounding (number of digits after decimal)
# :.2f
# print "This is my formatted number {example_number}
# but round it to the 2nd decimal
example_number = 100456.3257


#percents
# :% or #.2%, etc.
# print "This is my formatted number {example_number}
# but make it display as a percent
testNumber = .87


# more percents
# print "This is my formatted number {example_number}
# but make it display as a percent with two decimals
testNumber = .87465


# Spacing:
# align it in different ways with < for left > for right and ^ for center
testNumber = 12345
testStringLeft = f"{testNumber:<10}"
testStringRight = f"{testNumber:>10}"
testStringCenter = f"{testNumber:^10}"

# print("different alignments:", "\n")
# print(testStringRight)
# print(testStringLeft)
# print(testStringCenter)


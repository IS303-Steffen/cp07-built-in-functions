import os
import platform

def clear_screen():
    """
    Clears the terminal screen to make it easier to follow along with code.
    """
    if platform.system() == 'Windows':
        os.system('cls')
    else:
        os.system('clear')

clear_screen()

# ======================
# F STRINGS WITH NUMBERS
# ======================

'''
OVERVIEW
--------
You've alreaady seen f-strings.
These are just examples of using f-strings to round and format numbers

EXAMPLE
-------
example_number = 100456.3257
print(f"{example_number:,}") adds commas
print(f"{example_number:.2f}") rounds to second decimal
print(f"{example_number:,.2f}") rounds to second decimal and adds commas

'''
example_number = 100456.3257

# 1. ADDING COMMAS
# print "Formatted number: <example_number>"
# but make it have commas for digits in the thousands
'''
To add commas: {number:,}
'''


# 2. F-STRING ROUNDING
# print "Formatted number: <example_number>"
# but round it to the 2nd decimal
'''
To round: {number:.2f}
replace 2 with however many places you want after the decimal.
This uses traditional rounding, not banker's rounding.
'''



# 3. ROUND AND ADD COMMAS
# print "Formatted number: <example_number>"
# but round it to the 2nd decimal, and add commas for the thousands
'''
Commas & rounding: {number:,.2f}
commas come before the .
'''



# 4. PERCENTS
# print "Formatted number <example_percent>"
# but make it display as a percent
# try printing it with no decimals. Then try printing with 2 decimals
'''
To format as percent: {number:%}
To format as percent /w specific number of decimals: {number:.2%}
'''

example_percent = .87465



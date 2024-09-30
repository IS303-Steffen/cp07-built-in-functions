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

# ================
# NUMBER FUNCTIONS
# ================

'''
OVERVIEW
--------
These files go over built-in functions, as well as functions that use the 
python standard library.

There are many of these. You'll become familiar with many,
but for others you'll forget the exact syntax. Just google them when you
forget. That's what most people in the real world do.

math is part of the "standard library" of
python functions. It isn't automatically loaded, but it was downloaded when you
downloaded the python interpreter. You just need to add an "import" statement
to your python file.
Conventionally, you import everything you need at the top of the python file,
but to work, imports just need to come before the code that references them.
'''

# 1. ABSOLUTE VALUE
# Find the absolution value of -5.6 using abs()


# 2. MAX VALUE
# return the largest number in example_list using max()
example_list = [10, 4, 50, 10]


# 3. MIN VALUE min()
# return smallest number in example_list using min()
example_list = [10, 4, 50, 10]


# 4. SUM UP LIST
# add up a list using sum()
example_list = [10, 4, 50, 10]


# 5. ROUND
# round 5.6789 to the 2nd decimal using round()


'''
MATH LIBRARY
------------
Some more complex math functions come in the "math" library
Make sure to include "import math"


We won't focus much on these since we won't use math a whole lot in this class.
If you want even more math options, look into the "numpy" library.
'''



# 6. math.ceil()
# give the next highest integer value of 11.3:


# 7. math.floor()
# give the next lower integer value of 11.3:


# 8. math.factorial()
# give the factorial (4! or 4x3x2x1)


# 9. math.sqrt()
# find the square root of 16:


# 10. math.trunc()
# truncates anything past the decimal: 36.7





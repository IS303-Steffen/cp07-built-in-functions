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
# RANDOM FUNCTIONS
# ================

'''
OVERVIEW
--------
Occasionally, it is useful to generate random numbers, or randomly choose
something from a list. You'll use this on several of your assignments, so
make sure you at least know how to use randint()/randrange() and choice()

You must import random to get access to the random functions
'''

import random 

# 1. RANDOM SELECTION
# Use random.choice() to randomly choose an option from example_list
# print out your selection.
example_list = [1,2,3,4,5]


'''
GENERATING RANDOM INTEGERS
--------------------------
You have two choices:

    - randint(lower, upper)
    - randrange(lower, upper)

randint() is inclusive on the lower and upper range.

The makers of python decided that was inconsistent with how most other
functions in python work, so then the made randrange()

randrange() is inclusive on the lower end, but exclusive on the upper range

Just pick one and stick with it.
'''

# 2. randint() - GENERATE A RANDOM INTEGER BETWEEN 2 VALUES
# Using randint() Generate a random integer between 0 and 5


# 3. randrange() - GENERATE A RANDOM INTEGER BETWEEN 2 VALUES
# Using randrange() Generate a random integer between 0 and 5


# 4. randrange() - GENERATE A RANDOM INTEGER BETWEEN 2 VALUES
# Using randrange() Generate a random integer between 3 and 5


# 5. randrange() - GENERATE A RANDOM INTEGER BETWEEN 2 VALUES WITH INTERVALS
# Using randrange() Generate a random integer between 10 and 30, but only
# even numbers


'''
RANDOM FLOATS

    - uniform(lower, upper) is a float between any 2 floats, inclusive on
      both sides

    - random() is a float between 0 and 1, inclusive to 0, and exclusive to 1

'''

# 6. uniform() - GENERATE A RANDOM FLOAT BETWEEN 2 NUMBERS
# using uniform() generate a random float between 0 and 10


# 6. random() - GENERATE A RANDOM FLOAT BETWEEN 0 and 1
# using random() generate a random float between 0 and 1


'''
USING SEED() FOR REPRODUCABILITY OF OUTCOMES
--------------------------------------------
Sometime, you want to test your code with consistent outcomes.
In these scenarios, you can just use seed() and put any variable inside
as the starting point for the random number generator.

Afterwards, any random function will perform the same, no matter how many
times the code is run.

'''

# 7. USE SEED TO MAKE SELECTIONS CONSISTENT
# First, write a loop that prints out 5 random integers
# then, call random.seed() with any number at the beginning
# Then, repeat the loop that prints out 5 random integers again
# run your code multple times. Your second loop should always have the same
# numbers now.


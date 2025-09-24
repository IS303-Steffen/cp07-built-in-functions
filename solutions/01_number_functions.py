from helper_functions import clear_screen
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

# 1. MAX VALUE
# return the largest number in example_list using max()
example_list = [10, 4, 50, 10]
print("max: ", max(example_list))

# 2. MIN VALUE min()
# return smallest number in example_list using min()
example_list = [10, 4, 50, 10]
print("min: ", min(example_list))

# 3. SUM UP LIST
# add up a list using sum()
example_list = [10, 4, 50, 10]
print(f"sum: {sum(example_list)}")

# 4. ROUND
# round 5.6789 to the 2nd decimal using round()
print(f"round: {round(5.6789, 2)}")



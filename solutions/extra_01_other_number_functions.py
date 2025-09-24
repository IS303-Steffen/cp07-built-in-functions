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

# 1. ABSOLUTE VALUE
# Find the absolution value of -5.6 using abs()
print("absolute value:", abs(-5.6))



'''
MATH LIBRARY
------------
Some more complex math functions come in the "math" library
Make sure to include "import math"


We won't focus much on these since we won't use math a whole lot in this class.
If you want even more math options, look into the "numpy" library.
'''

import math

# 2. math.ceil()
# give the next highest integer value of 11.3:
print("ceil, next highest integer: ", math.ceil(11.3))

# 3. math.floor()
# give the next lower integer value of 11.3:
print("floor, next lowest integer: ", math.floor(11.3))

# 4. math.factorial()
# give the factorial (4! or 4x3x2x1)
print("factorial: ", math.factorial(4))

# 5. math.sqrt()
# find the square root of 16:
print("square root: ", math.sqrt(16))

# 6. math.trunc()
# truncates anything past the decimal: 36.7
print("truncated number: ", math.trunc(36.7))




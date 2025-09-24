from helper_functions import clear_screen
clear_screen()

# ==================
# DATETIME FUNCTIONS
# ==================

'''
OVERVIEW
--------
Python includes a lot of very useful ways to get the time and track
how much time has passed.
'''


from datetime import datetime
'''
datetime is part of the python standard library. 
importing it is confusing, because the module is called "datetime" but then
that module has a class (which we haven't learned about)
also called "datetime". So you are saying "from the module called datetime,
import the class datetime that has all those functions I want."
'''

# 1. GET CURRENT DATE/TIME
# datetime.now()
print("now() function: ", datetime.now())

# 2. ACCESSING SPECIFIC PARTS OF A DATETIME
# Using the date_time_example variable below,
# Try accessing whatever specific parts of the datetime you want. print them.

date_time_example = datetime.now()
'''
You can access any specfic part of a datetime object
    - .date()
    - .year
    - .month
    - .day
    - .hour
    - .minute
    - .second
    - .microsecond (millionth of a second)
'''
print("date:", date_time_example.date())
print("year", date_time_example.year)
print("month", date_time_example.month)
print("day", date_time_example.day)
print("hour", date_time_example.hour)
print("minute", date_time_example.minute)
print("second", date_time_example.second)
print("microsecond (millionths of seconds)", date_time_example.microsecond)

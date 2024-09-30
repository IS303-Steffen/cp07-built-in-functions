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

# ==================
# DATETIME FUNCTIONS
# ==================

'''
OVERVIEW
--------
We may just skip over these or briefly show off the reference file for time's
sake. Python includes a lot of very useful ways to get the time and track
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


# 3. CREATE YOUR OWN DATETIME OBJECT
# use datetime(year, month, day) to create a new datetime object
# of any date you want. print the date out.


# 4. FIND THE NUMBER OF DAYS BETWEEN NOW AND ANOTHER DATE
# Using the datetime you created in #3. subtract today's datetime
# from it and see how many days are between the 2 using .days


'''
Note, by default you can't get the number of years or months out of subtracting
dates, but if you want that functionality you can either write your own
logic for it, or import 3rd party libraries like dateutil.relativedelta
'''

'''
FORMATTING DATETIMES AS STRINGS
-------------------------------
When you have a datetime object, you can turn it into a string that is
formatted a specific way using strftime() or "string format time".

You need to provide formatting instructions. See below. We won't practice all
of these. Just look them up if you ever need them.

DATE:
•	%Y: Year with century (e.g., 2023).
•	%y: Year without century (last two digits, e.g., 23 for 2023).
•	%m: Month as a zero-padded decimal number (01–12).
•	%B: Full month name (e.g., September).
•	%b: Abbreviated month name (e.g., Sep).
•	%d: Day of the month as a zero-padded decimal number (01–31).
•	%A: Full weekday name (e.g., Monday).
•	%a: Abbreviated weekday name (e.g., Mon).
•	%w: Weekday as a decimal number (0 for Sunday, 6 for Saturday).
•	%j: Day of the year as a zero-padded decimal number (001–366).
•	%U: Week number of the year (Sunday as the first day of the week, 00–53).
•	%W: Week number of the year (Monday as the first day of the week, 00–53).

TIME:
•	%H: Hour (24-hour clock) as a zero-padded decimal number (00–23).
•	%I: Hour (12-hour clock) as a zero-padded decimal number (01–12).
•	%p: AM or PM (locale-specific).
•	%M: Minute as a zero-padded decimal number (00–59).
•	%S: Second as a zero-padded decimal number (00–59).
•	%f: Microsecond as a decimal number (000000–999999).
•	%z: UTC offset in the form +HHMM or -HHMM (if available).
•	%Z: Time zone name (if available).

'''

# 5. FORMATTING DATETIME AS STRINGS
# use strftime() to format date_time_example with the day of the week %A
# month %B and day %d


# 6. CREATE A DATETIME FROM A STRING
# Given date_string and format_string, create a datetime object using
# datetime.strptime()

date_string = "2023-09-26 14:45:08"
format_string = "%Y-%m-%d %H:%M:%S"
'''
strptime() or "string parse time" function.
when you want to create a datetime object from a string.
you need to give it a date as a string, and another string that tells how it is formatted.
'''


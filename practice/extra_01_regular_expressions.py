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

# ===========================
# REGULAR EXPRESSIONS (REGEX)
# ===========================

'''
OVERVIEW
--------
You are not required to learn this for the class. It is really useful, and
there is a whole chapter on it in the textbook, but with the limited time
we have, we currently dont' cover it. This file's purpose is just to show
how regular expressions are cool in case you want to go find out more on your
own.

Regular expressions let you define patterns, and then you can find matches of
those patterns in text.

See the textbook, or just look up online if you're curious about how you
define a pattern. Its like a whole mini-language that we won't cover.
'''

'''
To use regular expressions in python, you must import the "re" library:
'''
import re

# 1. EXTRACT ALL THE IP ADDRESSES FROM A LOG MESSAGE

ip_pattern = r"\b\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}\b"
'''
The above defines a regular expression pattern for an IP address:
    - r gets rid of the normal escape characters.
    - \b makes it so the pattern can only be matched if there is space
      at the start (and end) the pattern.
    - \d{1,3} a number that has at least 1 character and at most 3
    - \. just a dot (period)
'''

# Example of a log file with IP addresses
log_file = ("[INFO] - 2023-09-26 13:45:12 - User connected from 192.168.1.2 for 5th time on current date"
           "[ERROR] - 2023-09-26 13:46:14 - Connection timeout for 10.0.0.5 connection was lost"
           "[INFO] - 2023-09-26 13:47:05 - User connected from 172.16.0.3 for 1st time on current date")
    
# Find all IP addresses in the log_contents
ip_addresses = re.findall(ip_pattern, log_file)

# Print the extracted IP addresses
for ip in ip_addresses:
    print(ip)

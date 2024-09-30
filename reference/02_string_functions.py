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
# STRING FUNCTIONS
# ================

'''
OVERVIEW
--------
You've already seen most of these.

Remember that string functions don't change the string in-place.
Rather, they return a new string.
'''


'''
PRACTICE STRING
---------------
Notice the leading and trailing spaces, and the capitalization
of the string below:
'''
example_string = "  this is a sentence that Prof. Steffen wrote.  "

# 1. upper()
# make example_string all upper case:
print(f"upper: {example_string.upper()}")

# 2. lower()
# make example_string all lower case:
print(f"lower: {example_string.lower()}")

# 3. strip()
# make example_string get rid of leading empty space:
print(f"strip: {example_string.strip()}")

# 4. capitalize()
# make example_string's first character capitalized'
# HINT: try combining with strip
print(f"capitalize: {example_string.strip().capitalize()}")

# 5. title()
# Capitalize every word in exampmle_string
print(f"title: {example_string.title()}")

# 6. count()
# return number of times the substring "er" occurs in example_string_2
# BONUS: make it count whether "er" is capitalized or lowercase
example_string_2 = "Plumber Error Swimmer"
print(f'count of "er": {example_string_2.count("er")}')

# can you do it to account for the capital "E"?
print(f'count case insensitive: {example_string_2.lower().count("er")}')


#7. split()
# split example_string_3 by underscores, and get a list of the strings.
example_string_3 = "I_don't_want_the_underscores"
print("split:", example_string_3.split("_"))

# 8. replace()
# replace every instance of "_" with " " in example_string_3
print(f'replace: {example_string_3.replace("_", " ")}')

# 9. len()
# how long is example_string_3?
print(f"len: {len(example_string_3)}")

# 10. using "in" with strings
# if "ach" is in string_example_5, print "found it"
example_string_4 = "nacho libre"
if "ach" in example_string_4:
    print("in example:", "Found it")

# if "chips" is not in string_example_4, print "not found"
if "chips" not in example_string_4:
    print("not found")

'''
STRING INDEXING
---------------
just like how lists can be accessed with an [index]
you can access strings the same way:
'''
    
example_string_5 = "Example of text"
# 11. STRING INDEXING
# print only the 4th character of example_string_5
print("index example 1:", example_string_5[3])

# print the 4th to the 10th character of example_string_5
print("index example 2:", example_string_5[3:11])

# print the 4th to the end of example_string_5
print("index example 3:", example_string_5[3:])

# 12. find()
# find () returns the starting position of a substring.
# Given example_emails_list, use find() to find the start of the domain
# of each email address (the thing that starts with @)
# print out just the domain of the email address using string indexing.
example_emails_list = ["tom@gmail.com", "emily@yahoo.com",
                               "james@icloud.com"]

for email in example_emails_list:
    at_position = email.find("@")
    print(email[at_position:])

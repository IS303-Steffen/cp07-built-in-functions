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

# =========================
# RANDOM FUNCTIONS PRACTICE
# =========================


# 1. PRACTICE - GENERATING RANDOM NUMBERS AND SELECTING RANDOM CHOICES
# Generate a Random Number: Generate a random number between 1 and 100. This is your "number of the day".

# Choose a Random Color: pick a color from a predefined list of colors (e.g., ["Red", "Blue", "Green", "Yellow", "Purple"]).

# Determine Lucky Day:
# If the number is above 50 and the color is either Blue, Green, or Yellow, it's a "lucky day."
# Otherwise, it's a "normal day."

# Output: Print a message to inform the user whether it's a lucky day or a normal day based on the number and color.
# Include the number and color they generated


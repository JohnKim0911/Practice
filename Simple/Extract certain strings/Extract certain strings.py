with open("./Python Cheat Sheet.md") as file:
    content_list = file.readlines()

# print(content_list)

for text in content_list:
    if '###' in text:
        print(text.replace('###','').strip())

# ------------- Result --------------- #
# Print
# Input
# Comments
# Variables
# The += Operator
# Integers
# Floating Point Numbers
# Strings
# String Concatenation
# Escaping a String
# F-Strings
# Converting Data Types
# Checking Data Types
# Arithmetic Operators
# The += Operator
# The Modulo Operator
# Syntax Error
# Name Error
# Zero Division Error
# Creating Functions
# Calling Functions
# Functions with Inputs
# Functions with Outputs
# Variable Scope
# Keyword Arguments
# If
# Else
# Elif
# and
# or
# not
# comparison operators
# For Loop
# _ in a For Loop
# break
# continue
# Infinite Loops
# Adding Lists Together
# Adding an Item to a List
# List Index
# List Slicing
# Range
# Randomisation
# Round
# abs
# Importing
# Aliasing
# Importing from modules
# Importing Everything
# Creating a Python Class
# Creating an Object from a Class
# Class Methods
# Class Variables
# The __init__ method
# Class Properties
# Class Inheritance

# ------------------------------ Objective ---------------------------------- #
# [O] Calculate the input(string) from a user.
# [O] Keep Calculating on the top of the previous result if needed.
# [O] Cover weakness of 'eval' function.
# [O] Show the list of options.
# [O] Do not show the result as a floating point when it is actually an integer.
# [X] TODO: Make a Local GUI App
# [X] TODO: Make a Web App

# -------------------------------- Warning ---------------------------------- #
# Be careful when using "eval":
# https://stackoverflow.com/questions/9685946/math-operations-from-string

# -------------------------------- Code ------------------------------------- #
from introduction import Introduction
from calculation import Calculation


intro = Introduction()
cal = Calculation()

intro.print_intro()

is_on = True
while is_on:
    cal.get_input()

    if cal.should_turn_off():
        is_on = False
    elif not cal.is_input_suspicious() and not cal.is_input_empty():
        cal.calculate()

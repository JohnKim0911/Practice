# ------------------------------ Objective ---------------------------------- #
# [O] Calculate age by birthday.
# [O] Calculate age in South Korea.
# [O] Calculate time you have spent so far since you were born.
# [O] Calculate remaining days you have from now.
# [O] Show how many years left visually.
# [O] Calculate every 10 year from the birthday.


# --------------------------------- Code ------------------------------------ #
from calculator import Calculator

cal = Calculator()

cal.ask_birthday()
cal.ask_death_age()

cal.calculate_age()
cal.calculate_korean_age()
cal.calculate_remaining_time()

cal.print_text_result()
cal.print_life_chart()

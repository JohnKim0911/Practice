class Calculation:
    def __init__(self):
        self.result = 0
        self.user_input = ""

    def get_input(self):
        """Get input value from a user."""
        self.user_input = input("> ").lower()

    def is_input_empty(self):
        """Return True if the user input is empty. Otherwise, False."""
        if not self.user_input:
            print(self.result)
            return True
        else:
            return False

    def is_input_suspicious(self):
        """Return True if the user input is suspicious. Otherwise, False."""
        if "os.system" in self.user_input:  # Covers weakness of 'eval' function.
            print("It is not allowed.")
            return True
        else:
            return False

    def should_turn_off(self):
        """Return True if the user input includes "off". Otherwise, False."""
        if "off" in self.user_input:
            print("Turned off Successfully.")
            return True
        else:
            return False

    def should_calculate_on_top_of_pre_result(self):
        """Return True if the user input starts with math operators. Otherwise, False."""
        first_two_letters = self.user_input.strip()[:2]
        first_letter = self.user_input.strip()[0]
        if first_two_letters == "**" or first_two_letters == "//":
            return True
        elif first_letter == '+' or first_letter == '-' or first_letter == '*' or first_letter == '/' or first_letter == '%':
            return True
        else:
            return False

    def calculate(self):
        """Calculate and print the result. Print error message if needed."""
        try:
            if self.should_calculate_on_top_of_pre_result():
                self.result = eval(str(self.result) + self.user_input)
            else:
                self.result = eval(self.user_input)
        except (NameError, SyntaxError):
            print("Invalid input.")
        else:
            self.print_result()

    def is_result_integer(self):
        """Return True if the result is an integer. Otherwise, False."""
        temp = str(self.result).split(".")
        # Check if there is only "0" after dot.
        if len(temp) == 2 and temp[1] == "0":
            # e.g) 5.0 = > len: 2, temp[1] == "0" = > Integer
            return True
        else:
            return False

    def print_result(self):
        """Print result as an integer or floating number."""
        if not self.is_result_integer():
            # If it is a floating number, just print it out.
            print(self.result)
        else:
            # If it is an integer, change the form to an integer and print it out.
            self.result = int(self.result)
            print(self.result)

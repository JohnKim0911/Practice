class Introduction:

    def __init__(self):
        self.intro_msg = """Welcome to a Calculator.
- It can calculate mathematics like below:
  > 2 * (2 + 3) - 20/2 + 2**3
  8
  > + 2
  10
- To reset, simply type a new number
  without any math operator at the beginning:
  > 0
  0
- Type \"off\" to turn off the program.
- Refer to the available math operators below:\n"""

        self.math_operators_dict = {
            '+': ["Addition", "1 + 2 = 3"],
            '-': ["Subtraction", "2 - 1 = 1"],
            '*': ["Multiplication", "2 * 3 = 6"],
            '/': ["Division", "10 / 3 = 3.333333333"],
            '**': ["Exponentiation", "2 ** 3 = 8"],
            '//': ["Floor division", "10 // 3 = 3"],
            '%': ["Modulus", "10 % 2 = 0, 10 % 3 = 1"],
        }

    def print_math_operators(self):
        """Print math operators beautifully."""
        # Reference - How to print dictionary beautifully:
        # https://stackoverflow.com/questions/17330139/python-printing-a-dictionary-as-a-horizontal-table-with-headers
        print("{:<10} {:<18} {:<10}".format('Operator', 'Name', 'Example'))
        for key, value in self.math_operators_dict.items():
            label, num = value
            print("{:<10} {:<18} {:<10}".format(key, label, num))

    def print_intro(self):
        """Print introduction message."""
        line_break = "-----------------------------------------------------"
        print(line_break)
        print(self.intro_msg)
        self.print_math_operators()
        print("\nHave some fun!")
        print(line_break)

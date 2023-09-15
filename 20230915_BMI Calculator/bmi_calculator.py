# ------------------------------ Objective ---------------------------------- #
# [O] Calculate BMI with height and weight.
# [O] Calculate range of each category.
# [O] Visualize where you are within the range.


# --------------------------------- Code ------------------------------------ #
class BMICalculator:

    def __init__(self):
        self.your_height = 0
        self.your_weight = 0
        self.your_bmi = 0
        self.your_bmi_category = ""

        self.based_bmi_list = [18.5, 25, 30, 35]
        self.based_weight_list = []

        self.break_line = "-----------------------------------------------------------------------------"

    def print_introduction(self):
        print(self.break_line)
        print("Welcome to BMI Calculator!")
        print("* BMI(Body Mass Index) is a measure of body fat based on height and weight.")

    def ask_height_and_weight(self):
        self.your_height = float(input("- Your height in m? (e.g. 1.72): "))
        self.your_weight = float(input("- Your weight in kg? (e.g. 67.8): "))

        # # Use below for Test. (Instead of typing all the time)
        # self.your_height = 1.72
        # self.your_weight = 67.8
        # print(f"- Your height in m? (e.g. 1.72): {self.your_height}")
        # print(f"- Your weight in kg? (e.g. 67.8): {self.your_weight}")

    def calculate_bmi(self):
        # BMI = Weight / (Height**2)
        self.your_bmi = round(self.your_weight / self.your_height ** 2, 1)
        self.choose_bmi_category()

    def choose_bmi_category(self):
        if self.your_bmi < 18.5:
            self.your_bmi_category = "Underweight"
        elif self.your_bmi < 25:
            self.your_bmi_category = "Normal Weight"
        elif self.your_bmi < 30:
            self.your_bmi_category = "Slightly Overweight"
        elif self.your_bmi < 35:
            self.your_bmi_category = "Obese"
        else:  # 35 <= BMI
            self.your_bmi_category = "Clinically Obese"

    def calculate_weight_range_based_on_height(self):
        # BMI = Weight / (Height**2)
        # ----> Weight =  BMI * (Height**2)

        # Calculate weight from your_bmi based on the height.
        self.based_weight_list = []
        for bmi in self.based_bmi_list:
            # Weight =  BMI * (Height**2)
            weight = round(bmi * (self.your_height ** 2), 1)
            self.based_weight_list.append(weight)

    def format_weight_into_suitable_string(self, num_list):
        # Format numbers to the same length strings.

        # Check num_list to see if they are all 2 digits.
        are_all_2_digits = True
        for num in num_list:
            if num >= 100:
                are_all_2_digits = False
                break

        if are_all_2_digits:
            # All num are 2 digits, so no need to change.
            return num_list
        else:
            # Some are 3 digits, some are 2 digits. Need to format them to the same length string.
            formatted_list = []
            for num in num_list:
                if num > 100:
                    # 3 digits: no need to change.
                    formatted_list.append(str(num))
                else:
                    # 2 digits: add 1 white-space in front of it.
                    formatted_list.append(f" {str(num)}")
            return formatted_list

    def are_you_here(self, based_category, your_bmi_category):
        # To print where the user belongs to among the categories.
        if based_category == your_bmi_category:
            return "👈 You're here!"
        else:
            return ''

    def detail_range_result(self):
        # Format weight-numbers into suitable string format.
        formatted_list = self.format_weight_into_suitable_string(self.based_weight_list)

        # Name each category weight.
        normal_weight = f"{formatted_list[0]}kg"
        slightly_overweight = f"{formatted_list[1]}kg"
        obese = f"{formatted_list[2]}kg"
        clinically_obese = f"{formatted_list[3]}kg"

        detail_range_result = f"""(Based on height: {self.your_height}m, weight: {self.your_weight}kg)
1.         Underweight |         BMI < 18.5 |           Weight < {normal_weight} {self.are_you_here("Underweight", self.your_bmi_category)}
2.       Normal Weight | 18.5 <= BMI < 25.0 | {normal_weight} <= Weight < {slightly_overweight} {self.are_you_here("Normal Weight", self.your_bmi_category)}
3. Slightly Overweight | 25.0 <= BMI < 30.0 | {slightly_overweight} <= Weight < {obese} {self.are_you_here("Slightly Overweight", self.your_bmi_category)}
4.               Obese | 30.0 <= BMI < 35.0 | {obese} <= Weight < {clinically_obese} {self.are_you_here("Obese", self.your_bmi_category)}
5.    Clinically Obese | 35.0 <= BMI        | {clinically_obese} <= Weight {self.are_you_here("Clinically Obese", self.your_bmi_category)}
"""
        return detail_range_result

    def print_bmi_box_graph(self):
        box_list = []
        num_list = []
        blank_list = []

        for num in range(15, 41):
            if num == round(self.your_bmi):
                box_list.append("■ ")
                num_list.append(f"{str(num)}")
                blank_list.append("👆 Your BMI is here!")
            else:
                box_list.append("□ ")
                if num >= 100:
                    num_list.append(f"{str(num)[1:]}")
                else:
                    num_list.append(f"{str(num)}")
                blank_list.append("  ")

        you_are_here_line = ' '.join(blank_list)
        box_line = ' '.join(box_list)
        num_line = ' '.join(num_list)

        print("           |                 |   Slightly   |              |    Clinically  ")
        print("Underweight|  Normal Weight  |  Overweight  |     Obese    |      Obese     ")
        print("-----1---->|<-------2------->|<------3----->|<------4----->|<-------5-------")
        print(box_line)
        print(num_line)
        print(you_are_here_line)

    def print_weight_box_graph(self):
        round_your_weight = round(self.your_weight)

        rounded_based_weight_list = []
        for weight in self.based_weight_list:
            rounded_based_weight_list.append(round(weight))

        kg_clinically_obese = rounded_based_weight_list[3]
        kg_obese = rounded_based_weight_list[2]
        kg_slightly_overweight = rounded_based_weight_list[1]
        kg_normal_weight = rounded_based_weight_list[0]

        row_list = []
        for num in range(kg_clinically_obese+4, kg_normal_weight-6, -1):
            if num == round_your_weight:
                temp = f"■ {num} kg"
            else:
                temp = f"□ {num} kg"

            if num >= kg_clinically_obese:
                temp += " (Clinically Obese)"
            elif num >= kg_obese:
                temp += " (Obese)"
            elif num >= kg_slightly_overweight:
                temp += " (Slightly Overweight)"
            elif num >= kg_normal_weight:
                temp += " (Normal Weight)"
            else:
                temp += " (Underweight)"

            if num == round_your_weight:
                temp += " 👈 You're here!"

            row_list.append(temp)

        for row in row_list:
            print(row)

    def print_result(self):
        print(self.break_line)
        print("[Output]")
        print(f"👉 Your BMI: {self.your_bmi} ({self.your_bmi_category})")

        print("\n[Detail]")
        print(self.detail_range_result())

        print("[BMI Graph]")
        print(self.break_line)
        self.print_bmi_box_graph()
        print(self.break_line)

    def ask_for_weight_graph(self):
        answer = input("Would you like to check your weight graph too? (Type 'y' or 'n'): ").lower()

        if answer == 'y':
            print("\n[Weight Graph]")
            self.print_weight_box_graph()

        print(self.break_line)


cal = BMICalculator()

cal.print_introduction()
cal.ask_height_and_weight()
cal.calculate_bmi()
cal.calculate_weight_range_based_on_height()
cal.print_result()
cal.ask_for_weight_graph()

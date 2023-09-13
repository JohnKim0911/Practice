from datetime import datetime


class Calculator:

    def __init__(self):
        self.today_datetime = datetime.today()  # e.g. 2023-09-11 10:34:38.367519
        self.birthday_datetime = None  # e.g. 1992-10-29 00:00:00
        self.age = {
            'day': 0,  # e.g. 11274: Age converted into days
            'week': 0,  # e.g. 1564: Age converted into weeks
            'month': 0,  # e.g. 370: Age converted into months
            'year': 0,  # e.g. 30: Real Age
        }
        self.korean_age = 0
        self.death_age = 0
        self.death_datetime = None
        self.remaining_time = {
            'day': 0,  # : Remaining days
            'week': 0,  # : Remaining days Converted into weeks
            'month': 0,  # : Remaining days Converted into months
            'year': 0,  # : Remaining days Converted into years
        }

    def ask_birthday(self):
        """Ask birthday and store it in a suitable format."""
        birthday = input("Your birthday? (e.g. 1992-10-29): ").split('-')
        # birthday = "1992-10-29".split('-')  # Use this for test instead of typing it every time.
        # birthday = "1987-10-01".split('-')  # Use this for test instead of typing it every time.
        self.birthday_datetime = datetime(int(birthday[0]), int(birthday[1]), int(birthday[2]))

    def ask_death_age(self):
        """Ask expected death age and store it."""
        self.death_age = int(input("Expected death age? (e.g. 80): "))
        # self.death_age = 75  # Use this for test instead of typing it every time.
        # self.death_age = 94  # Use this for test instead of typing it every time.

    def cal_difference_and_convert(self, datetime1, datetime2, dict_to_save):
        """Calculate differences in days => (datetime1 - datetime2).days.
        Convert them into week, month, year and save them in a provided dictionary."""
        dict_to_save['day'] = (datetime1 - datetime2).days
        dict_to_save['week'] = int(dict_to_save['day'] / 7)
        dict_to_save['month'] = int(dict_to_save['day'] / 30.437)  # 30.437: Average days in a month
        dict_to_save['year'] = int(dict_to_save['day'] / 365.2422)  # 365.2422: Average days in a year

    def calculate_age(self):
        """Calculate age and save it in a suitable format."""
        self.cal_difference_and_convert(self.today_datetime, self.birthday_datetime, self.age)

    def calculate_korean_age(self):
        """Calculate Korean age and store it.\n
        In South Korea, you are already 1 year old when you are born.\n
        You get aged every 1st of January."""
        self.korean_age = 1 + self.today_datetime.year - self.birthday_datetime.year  # e.g. 1 + 2023 - 1992 = 32

    def calculate_remaining_time(self):
        """Calculate remaining days and save it in a suitable format."""
        expected_death_year = self.birthday_datetime.year + self.death_age
        self.death_datetime = datetime(expected_death_year, self.birthday_datetime.month, self.birthday_datetime.day)
        self.cal_difference_and_convert(self.death_datetime, self.today_datetime, self.remaining_time)

    def print_text_result(self):
        """Print all the text result in a nice format."""
        hr_line = "---------------------------------------------------------------------"
        print(hr_line)
        print(f"              Today: {self.today_datetime.strftime('%Y-%m-%d')} (Year-Month-Day)")
        print(f"      Your birthday: {self.birthday_datetime.strftime('%Y-%m-%d')} (Year-Month-Day)")
        print(f"           Your age: {self.age['year']}")
        print(f"    Your Korean age: {self.korean_age}")
        print(f" Expected death age: {self.death_age}")
        print(f"Expected death date: {self.death_datetime.strftime('%Y-%m-%d')} (Year-Month-Day)")
        print("")
        print(f"You have lived for {self.age['day']} days, {self.age['week']} weeks, "
              f"{self.age['month']} months, {self.age['year']} years.")
        print(f"          You have {self.remaining_time['day']} days, {self.remaining_time['week']} weeks, "
              f"{self.remaining_time['month']} months, {self.remaining_time['year']} years left.")
        print(hr_line)

    def get_proper_box(self, num):
        """For 'Life Chart'. Return '■' to show the age, '□' for remaining years."""
        if num <= self.age['year']:
            return '■'
        else:
            return '□'

    def cal_y_year_from_birthday(self, y_year):
        """Calculate 'y' year from the birthday.\n
        e.g. birthday: (1992-10-29),\n
        y_year=10: (2002-10-29),\n
        y_year=20: (2012-10-29)..."""
        return f"{self.birthday_datetime.year + y_year}-{self.birthday_datetime.strftime('%m')}-{self.birthday_datetime.strftime('%d')}"

    def white_space(self):
        """Calculate white space for the top line of life chart and return it."""
        num_of_last_boxes = self.death_age % 10
        white_space = (10 - num_of_last_boxes) * "  "
        return white_space

    def print_life_chart(self):
        """Print life chart in a beautiful format with informative graphic."""
        bottom_line_str = f"                      0 year.  ({self.birthday_datetime.strftime('%Y-%m-%d')})"
        outer_list = [bottom_line_str]  # The whole chart.
        inner_str = ""  # Each row
        y = 10  # For 10 years. 20 years. 30 years... at the end of each line.

        # Print boxes as many as age.
        for num in range(1, self.death_age + 1):
            if num % 10 != 0:
                # Every number except for 10, 20, 30...
                # Get proper box and store them in 'inner_str'.
                inner_str += (self.get_proper_box(num) + " ")
                if num == self.death_age:
                    # Top line
                    inner_str = f"{inner_str}{self.white_space()} {self.death_age} years. ({self.death_datetime.strftime('%Y-%m-%d')})\n"
                    outer_list.insert(0, inner_str)  # Insert 'inner_str' into 'outer_list' in a reverse order.
            else:
                # When it's 10th number each line:
                # At the end of each line, print '10 years'. '20 years'. '30 years'... and then change row.
                if y < 100:
                    # When it's 2 digits. e.g. 80 years.
                    inner_str += (self.get_proper_box(num) + f"  {y} years. ({self.cal_y_year_from_birthday(y)})\n")
                else:
                    # When it's 3 digits. e.g. 100 years.
                    inner_str += (self.get_proper_box(num) + f" {y} years. ({self.cal_y_year_from_birthday(y)})\n")
                outer_list.insert(0, inner_str)  # Insert 'inner_str' into 'outer_list' in a reverse order.
                inner_str = ""  # reset the inner str.
                y += 10  # 10 years. 20 years. 30 years...

        print("Here's your life chart:\n")
        result = "".join(outer_list)
        print(result)

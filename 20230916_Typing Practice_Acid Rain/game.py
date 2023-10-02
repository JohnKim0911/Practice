import random
from record import Record


class GameManager:

    def __init__(self):
        self.player_name = ""

        self.word_string_list = []
        self.rain_turtle_list = []

        self.rain_move_distance = 1.5
        self.rain_time_sleep_num = 0.06  # Control speed of generating each frame: The lower, the faster
        # self.rain_time_sleep_num = 0.005  # Control speed of generating each frame: The lower, the faster

        self.count_num = 0  # When 'count_num' reaches the number of 'timing_num': Create rain.
        self.timing_num = 20  # Change this to control the time between creating rain.

        self.rain_num = 0
        self.rain_max_num = 20

        self.special_num = 0
        self.special_word = ""
        self.special_effect_chosen = ""
        self.special_effect_temp_distance = 0

        self.score_for_whole_game = 0
        self.score_for_current_game = 0

        self.stage = 1

        self.ph_level = 4.0

        self.record = Record()

    def get_words_from_the_file(self):
        with open("./data/words.txt") as word_file:
            words = word_file.readlines()
        self.word_string_list = [word.strip() for word in words]

    def get_random_special_num(self):
        self.special_num = random.randrange(1, self.rain_max_num + 1)

    def time_to_create_rain(self):
        if self.count_num % self.timing_num == 0 and self.rain_num < self.rain_max_num and self.special_effect_chosen != "stop":
            return True
        else:
            return False

    def increase_score(self):
        self.score_for_whole_game += self.stage  # Score: Get more scores as stages go up
        self.score_for_current_game += 1

    def control_ph_level(self, symbol):
        if symbol == '+':
            self.ph_level += 0.5
        else:
            self.ph_level -= 0.5

    def is_next_stage(self):
        # Next stage when there isn't any rain left.
        if self.rain_num == self.rain_max_num and len(self.rain_turtle_list) == 0:
            return True
        else:
            return False

    def change_rain_speed(self, option):
        """This is only for special effect."""
        self.special_effect_temp_distance = self.rain_move_distance
        if option == "faster":
            self.special_effect_chosen = "faster"
            self.rain_move_distance *= 2
        elif option == "slower":
            self.special_effect_chosen = "slower"
            self.rain_move_distance /= 2  # Half speed of the current speed
        elif option == "stop":
            self.special_effect_chosen = "stop"
            self.rain_move_distance = 0

    def reset_special_effect(self):
        self.rain_move_distance = self.special_effect_temp_distance
        self.special_effect_chosen = ''

    def update_record(self):
        self.record.update_record(self.player_name, self.score_for_whole_game, self.stage)
        self.record.save_df_to_csv()
        self.record.update_df_dict()
        self.record.check_user_rank(self.player_name, self.score_for_whole_game, self.stage)
        return self.record.df_dict

    def increase_difficulty(self):
        if self.rain_time_sleep_num > 0.005:
            self.rain_time_sleep_num -= 0.005  # Control speed of generating each frame: The lower, the faster
        self.rain_move_distance += 0.3  # Make rain moves faster!
        if self.rain_max_num < 30:
            self.rain_max_num += 1  # Increase number of rain.

    def play_again(self):
        """Reset everything."""
        self.player_name = ""

        self.rain_turtle_list = []

        self.rain_move_distance = 1.5
        self.rain_time_sleep_num = 0.06  # Control speed of generating each frame: The lower, the faster
        # self.rain_time_sleep_num = 0.005  # Control speed of generating each frame: The lower, the faster

        self.count_num = 0  # When 'count_num' reaches the number of 'timing_num': Create rain.
        self.timing_num = 20  # Change this to control the time between creating rain.

        self.rain_num = 0
        self.rain_max_num = 20

        self.special_num = 0
        self.special_word = ""
        self.special_effect_chosen = ""
        self.special_effect_temp_distance = 0

        self.score_for_whole_game = 0
        self.score_for_current_game = 0

        self.stage = 1

        self.ph_level = 4.0

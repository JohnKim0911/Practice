import random


class GameManager:

    def __init__(self):
        self.player_name = ""

        self.word_string_list = []
        self.rain_turtle_list = []

        self.rain_move_distance = 1.5

        self.count_num = 0  # When 'count_num' reaches the number of 'timing_num': Create rain.
        self.timing_num = 15  # Change this to control the time between creating rain.

        self.rain_num = 0
        self.rain_max_num = 20
        # self.rain_max_num = 5  # For test

        self.special_num = 0
        self.special_word = ""
        self.special_effect_chosen = ""
        self.special_effect_distance = 1
        self.special_effect_temp_distance = 0

        self.score_for_whole_game = 0
        self.score_for_current_game = 0

        self.stage = 1

        self.ph_level = 4.0

    def get_words_from_the_file(self):
        with open("./data/words.txt") as word_file:
            words = word_file.readlines()
        self.word_string_list = [word.strip() for word in words]

    def get_random_special_num(self):
        self.special_num = random.randrange(1, self.rain_max_num + 1)
        print(self.special_num)

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
            self.ph_level += 0.3
        else:
            self.ph_level -= 0.3

    def is_next_stage(self):
        # Next stage when there isn't any rain left.
        if self.rain_num == self.rain_max_num and len(self.rain_turtle_list) == 0:
            return True
        else:
            return False

    def change_rain_speed(self, option):
        if option == "faster":
            self.special_effect_chosen = "faster"
            self.rain_move_distance += self.special_effect_distance
        elif option == "slower":
            self.special_effect_chosen = "slower"
            self.rain_move_distance -= self.special_effect_distance
        elif option == "stop":
            self.special_effect_chosen = "stop"
            self.special_effect_temp_distance = self.rain_move_distance
            self.rain_move_distance = 0

    def reset_special_effect(self):
        if self.special_effect_chosen == "faster":
            self.rain_move_distance -= self.special_effect_distance
        elif self.special_effect_chosen == "slower":
            self.rain_move_distance += self.special_effect_distance
        elif self.special_effect_chosen == "stop":
            self.rain_move_distance = self.special_effect_temp_distance
        self.special_effect_chosen = ''

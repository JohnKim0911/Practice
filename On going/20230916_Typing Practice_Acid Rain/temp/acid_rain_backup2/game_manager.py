from word_list import WordList
import random

class GameManager:

    def __init__(self):
        self.all_word_lists = WordList()
        self.current_stage_word_list = []
        self.stage = 1
        self.score = 0
        self.ph_level = 0

        self.rain_list = []
        self.rain_move_distance = 5

    def update_current_stage_word_list(self):
        self.current_stage_word_list = self.all_word_lists.word_lists_by_level[self.stage-1]

    def get_random_text(self):
        return random.choice(self.current_stage_word_list)

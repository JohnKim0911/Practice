from word_lists import ALL_LEVEL_WORDS_LIST
import random
from turtle import RawTurtle

SCREEN_LEFT = -400
SCREEN_RIGHT = 400
SCREEN_TOP = 300
SCREEN_BOTTOM = -300
SEA_LINE_Y_COORDINATE = -219

WORDS_STARTING_LINE_Y_COR = 250
WORDS_MOVING_DISTANCE = 5
WORDS_FONT = ("Arial", 15, "bold")
WORDS_MIN_Y_DISTANCE_BETWEEN = 30


class Word(RawTurtle):

    def __init__(self, screen):
        super().__init__()
        self.word = ""
        self.canvas = screen


class WordManager:

    def __init__(self, screen):
        super().__init__()
        self.level_list_index = 0
        self.all_words = []
        self.choose_words_for_this_level()
        self.word_index = 0
        self.all_turtles = []
        self.word_speed = WORDS_MOVING_DISTANCE
        self.screen = screen

    def choose_words_for_this_level(self):
        # Choose 30 words for this level
        while len(self.all_words) < 30:
            new_word = random.choice(ALL_LEVEL_WORDS_LIST[self.level_list_index])
            if new_word not in self.all_words:
                self.all_words.append(new_word)
        print(self.all_words)

    def can_create_another_word(self):
        t_ycor_list = []
        for t in self.all_turtles:
            t_ycor_list.append(t.ycor())
        for ycor in t_ycor_list:
            if ycor >= WORDS_STARTING_LINE_Y_COR - WORDS_MIN_Y_DISTANCE_BETWEEN:
                return False
        return True

    def create_word(self):
        t = Word(self.screen)
        t.hideturtle()
        t.penup()
        random_x = random.randint(SCREEN_LEFT + 50, SCREEN_RIGHT - 50)
        t.goto(random_x, WORDS_STARTING_LINE_Y_COR)
        t.setheading(270)
        t.word = self.all_words[self.word_index]
        t.write(t.word, font=WORDS_FONT)
        self.all_turtles.append(t)
        self.word_index += 1

    def create_word_controlling_timing(self):
        if len(self.all_turtles) == 0:
            self.create_word()
        else:
            if self.can_create_another_word():
                random_chance = random.randint(1, 6)
                if random_chance == 1:
                    self.create_word()

    def move_words(self):
        for t in self.all_turtles:
            t.clear()
            current_x = t.xcor()
            new_y = t.ycor() - self.word_speed
            t.goto(current_x, new_y)
            t.write(t.word, font=WORDS_FONT)

    def is_game_over(self):
        for t in self.all_turtles:
            if t.ycor() < SEA_LINE_Y_COORDINATE-20:
                return True

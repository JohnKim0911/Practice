from tkinter import *
from turtle import TurtleScreen, RawTurtle
import random
import time


class Word:

    def __init__(self, raw_turtle):
        self.raw_turtle = raw_turtle
        self.raw_turtle.hideturtle()
        self.raw_turtle.penup()
        self.word = random.choice(word_string_list)
        random_x = random.randrange(-250, 250)
        self.raw_turtle.goto(random_x, 150)
        self.raw_turtle.write(self.word, align="center", font=("Courier", 10, "normal"))


def get_words_from_the_file():
    with open("words.txt") as word_file:
        words = word_file.readlines()
    stripped_word_list = [word.strip() for word in words]
    return stripped_word_list

def create_rain():
    t = RawTurtle(screen)
    word_turtle_list.append(Word(t))

def move_rain():
    for rain in word_turtle_list:
        rain.raw_turtle.clear()
        current_x = rain.raw_turtle.xcor()
        new_y = rain.raw_turtle.ycor() - rain_move_distance
        rain.raw_turtle.goto(current_x, new_y)
        rain.raw_turtle.write(rain.word)


word_string_list = get_words_from_the_file()
word_turtle_list = []
rain_move_distance = 5


window = Tk()
window.title("Acid Rain")
window.config(padx=20, pady=20, bg="grey")

canvas = Canvas(width=600, height=400)
screen = TurtleScreen(canvas)
background_img = PhotoImage(file="background.png")
canvas.create_image(0, 0, image=background_img)
canvas.grid(row=0, column=0)

screen.tracer(0)

is_on = True
while is_on:
    time.sleep(0.5)
    screen.update()

    create_rain()
    move_rain()


window.mainloop()
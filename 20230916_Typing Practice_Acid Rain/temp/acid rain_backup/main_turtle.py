import turtle
import time
import tkinter as tk
from word_manager import WordManager
from scoreboard import Scoreboard


def enter(*event):
    print(entry.get())


# X coordinate => left: -400, X right: 400
# Y coordinate => top: 300, bottom: -300, sea line: -219

screen = turtle.Screen()
screen.setup(width=800, height=600)
screen.tracer(0)
screen.title("Typing Practice - Acid Rain")

image = "background.gif"
screen.addshape(image)
turtle.shape(image)

canvas = screen.getcanvas()
entry = tk.Entry(canvas.master)
canvas.bind('<Return>', enter)
entry.focus()
canvas.create_window(0, 255, window=entry)

word_manager = WordManager()
scoreboard = Scoreboard()

screen.listen()

game_is_on = True
while game_is_on:
    time.sleep(0.2)  # the higher, the slower the game is.
    screen.update()

    word_manager.create_word_controlling_timing()
    word_manager.move_words()

    if word_manager.is_game_over():
        # game_is_on = False
        scoreboard.increase_score()

turtle.mainloop()


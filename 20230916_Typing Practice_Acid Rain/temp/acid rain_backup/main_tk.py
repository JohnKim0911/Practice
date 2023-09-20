import tkinter as tk
import turtle
import time
from word_manager import WordManager
# from scoreboard import Scoreboard

FONT = "Arial"

window = tk.Tk()
window.title("Typing Practice")
window.config(padx=20, pady=20)

title_label = tk.Label(text="Acid Rain", font=(FONT, 18, "bold"))
title_label.grid(row=0, column=0, columnspan=2)

canvas = tk.Canvas(width=800, height=600)
background_img = tk.PhotoImage(file="background.gif")
canvas_background = canvas.create_image(400, 300, image=background_img)
canvas.grid(row=2, column=0, columnspan=2)

entry = tk.Entry(canvas.master, width=30)
entry.focus()
canvas.create_window(400, 570, window=entry)

level_and_score_label = tk.Label(text="Current Level: 1   Score: 0", font=(FONT, 13, "normal"))
level_and_score_label.grid(row=1, column=0, sticky='w')

highest_level_and_score_label = tk.Label(text="Highest Level: 1   Score: 1", font=(FONT, 13, "normal"))
highest_level_and_score_label.grid(row=1, column=1, sticky='e')

word_manager = WordManager()

game_is_on = True
while game_is_on:
    time.sleep(0.2)  # the higher, the slower the game is.
    # screen.update()

    word_manager.create_word_controlling_timing()
    word_manager.move_words()

    # if word_manager.is_game_over():
        # game_is_on = False
        # scoreboard.increase_score()

window.mainloop()



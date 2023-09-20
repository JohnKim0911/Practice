import turtle
from tkinter import *
import time
# from word_manager import WordManager

FONT = "Arial"


def enter(*event):
    print(user_input.get())
    user_input.delete(0, END)


window = Tk()
window.title("Typing Practice - Acid Rain")
window.config(padx=0, pady=20)
window.bind("<Return>", enter)

title_label = Label(text="Acid Rain", font=(FONT, 18, "bold"))
title_label.grid(row=0, column=0, columnspan=2)

current_label = Label(text="[ Current ]\nPlayer: someone   Level: 1   Score: 0", font=(FONT, 13, "normal"))
current_label.grid(row=1, column=0, sticky='w')

highest_label = Label(text="[ Highest ]\nPlayer: Someone    Level: 1   Score: 0", font=(FONT, 13, "normal"))
highest_label.grid(row=1, column=1, sticky='e')
#
# current_level_and_score_label = Label(text="Current Player   Level: 1   Score: 0", font=(FONT, 13, "normal"))
# current_level_and_score_label.grid(row=2, column=0, sticky='w')
#
# highest_level_and_score_label = Label(text="Someone    Level: 1   Score: 0", font=(FONT, 13, "normal"))
# highest_level_and_score_label.grid(row=2, column=1, sticky='e')

canvas = Canvas(width=800, height=600)
background_img = PhotoImage(file="background.gif")
canvas.create_image(400, 300, image=background_img)
canvas.grid(row=3, column=0, columnspan=2)


user_input = Entry(canvas.master, width=30)
user_input.focus()
canvas.create_window(400, 570, window=user_input)


window.mainloop()


# Background image:
# https://unsplash.com/photos/n5cj9tfftUk

# Emoji image:
# https://www.freepik.com/free-vector/businessman-vector-facial-expressions-icon-set-isolated-white-background_38003940.htm#query=different%20emotion%20old%20man&position=43&from_view=search&track=ais
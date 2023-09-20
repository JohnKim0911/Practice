from tkinter import *
import time
import random


# ----------------------------------------- Class ------------------------------------- #
class Word:

    def __init__(self, raw_turtle):
        self.raw_turtle = raw_turtle
        self.raw_turtle.hideturtle()
        self.raw_turtle.penup()
        self.word = random.choice(word_list)
        random_x = random.randrange(-450, 450)
        self.raw_turtle.goto(random_x, 150)
        self.raw_turtle.write(self.word, align="center", font=("Courier", 10, "normal"))


# ----------------------------------------- Functions ------------------------------------- #
def enter(event):
    print(entry.get())
    entry.delete(0, END)


def get_words_from_the_file():
    with open("./data/words.txt") as word_file:
        words = word_file.readlines()
    stripped_word_list = [word.strip() for word in words]
    return stripped_word_list


# def create_rain():
#     random_word = random.choice(word_list)
#     rain_label = Label(window, text=random_word)
#     random_x = random.randrange()



# ----------------------------------------- Variables ------------------------------------- #
DARK_BLUE = "#213555"
LIGHT_BLUE = "#4F709C"
BLACK = "black"
FONT_STYLE = "Arial"


# ----------------------------------------- UI ------------------------------------- #
window = Tk()
window.title("Typing Practice - Acid Rain")
window.minsize(width=1200, height=800)
window.config(padx=20, pady=20, bg=DARK_BLUE)

# Title
title_label = Label(text="Acid Rain", fg="white", bg=DARK_BLUE, font=(FONT_STYLE, 18, "bold"))
title_label.grid(column=0, row=0, columnspan=2)

# Light Blue Background Main Box
outer_canvas = Canvas(width=1170, height=727, bg=LIGHT_BLUE, highlightthickness=0)
outer_canvas.grid(column=0, row=1, columnspan=2, rowspan=7)

# Main Image
bg_canvas = Canvas(width=1000, height=667, highlightthickness=0)
background_img = PhotoImage(file="./images/background.png")
bg_canvas.create_image(500, 333, image=background_img)
bg_canvas.grid(column=0, row=1, rowspan=5, padx=(10, 10), pady=(10, 10))

# Entry inside the main image
entry = Entry(bg_canvas.master, width=15, font=(FONT_STYLE, 13, "normal"))
entry.bind("<Return>", enter)
entry.focus()
bg_canvas.create_window(500, 630, window=entry)  # turtle coordination used

# Side Box
# Player name with black background
player_canvas = Canvas(width=140, height=45, bg=BLACK, highlightthickness=0)
player_text = player_canvas.create_text(
    70,
    22,
    width=120,
    text="John",
    fill="white",
    font=(FONT_STYLE, 15, "normal")
)
player_canvas.grid(column=1, row=1, padx=(0, 10), pady=(10, 10))

# Profile Image
profile_canvas = Canvas(width=140, height=154, highlightthickness=0)
profile_img = PhotoImage(file="images/man_face_normal.png")
profile_canvas.create_image(70, 77, image=profile_img)
profile_canvas.grid(column=1, row=2, padx=(0, 10))

# Dark Blue Background Box
side_sub_canvas = Canvas(width=140, height=450, bg=DARK_BLUE, highlightthickness=0)
side_sub_canvas.grid(column=1, row=3, columnspan=3, rowspan=3, padx=(0, 10), pady=(10, 10))

# Stage
stage_label = Label(text="Stage: 1", fg="white", bg=DARK_BLUE, font=(FONT_STYLE, 14, "bold"))
stage_label.grid(column=1, row=3, sticky='s')

# Score with black background
score_canvas = Canvas(width=120, height=45, bg=BLACK, highlightthickness=0)
score_text = score_canvas.create_text(
    60,
    22,
    width=100,
    text="Score: 0",
    fill="white",
    font=(FONT_STYLE, 12, "normal")
)
score_canvas.grid(column=1, row=4, padx=(0, 10))

# pH Bar Image
ph_bar_canvas = Canvas(width=65, height=300, highlightthickness=0)
ph_bar_img = PhotoImage(file="images/pH_bar.png")
ph_bar_canvas.create_image(32, 150, image=ph_bar_img)
ph_bar_canvas.grid(column=1, row=5, padx=(10, 10), pady=(0, 10), sticky='w')

# Bottom Status Box
bottom_status_canvas = Canvas(width=1150, height=30, bg=BLACK, highlightthickness=0)
bottom_status_text = bottom_status_canvas.create_text(
    500,
    15,
    width=500,
    text="",
    fill="white",
    font=(FONT_STYLE, 12, "normal")
)
bottom_status_canvas.grid(column=0, row=6, columnspan=3, pady=(0, 10))

# ----------------------------------------- Main Game ------------------------------------- #

word_list = get_words_from_the_file
rain_list = []
rain_move_distance = 10

is_on = True
while is_on:
    time.sleep(1)
    window.update()


window.mainloop()  # Keep the window open

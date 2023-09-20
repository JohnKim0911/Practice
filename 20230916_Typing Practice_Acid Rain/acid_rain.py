from tkinter import *
from turtle import TurtleScreen, RawTurtle
import time
import random


# ----------------------------------------- Constant Variables ------------------------------------- #
DARK_BLUE = "#213555"
LIGHT_BLUE = "#4F709C"
FONT_STYLE = "Arial"

# ----------------------------------------- Variables ------------------------------------- #
word_string_list = []
rain_turtle_list = []
rain_move_distance = 3
# rain_move_distance = 30
num_for_timing_of_creating_rain = 0
rain_num = 0
rain_mux_num = 30
score = 0
stage = 1
ph_level = 5.0


# ----------------------------------------- Class ------------------------------------- #
class Rain:

    def __init__(self, raw_turtle):
        self.raw_turtle = raw_turtle
        self.raw_turtle.hideturtle()
        self.raw_turtle.penup()
        self.word = random.choice(word_string_list)
        random_x = random.randrange(-400, 400)
        self.raw_turtle.goto(random_x, 330)
        self.raw_turtle.write(self.word, align="center", font=("Courier", 10, "normal"))


# ----------------------------------------- Functions ------------------------------------- #
def enter(event):
    print(entry.get())

    # Check if the answer is right.
    for rain in rain_turtle_list:
        if entry.get() == rain.word:
            global score, score_canvas, ph_level
            # Add score
            score += 1
            # Update score
            score_canvas.itemconfig(score_text, text=f"Score: {score}")
            # Update ph_level
            if ph_level < 6.0:
                ph_level += 0.2
                ph_level = round(ph_level, 2)
                ph_level_turtle.clear()
                current_x = ph_level_turtle.xcor()
                new_y = ph_level_turtle.ycor() + 9.5
                ph_level_turtle.goto(current_x, new_y)
                ph_level_turtle.write(f"◀ pH {ph_level}", align="center", font=(FONT_STYLE, 10, "normal"))
                print(ph_level)
            # Remove rain
            rain.raw_turtle.clear()
            rain_turtle_list.remove(rain)
            break
    entry.delete(0, END)


def get_words_from_the_file():
    with open("./data/words.txt") as word_file:
        words = word_file.readlines()
    global word_string_list
    word_string_list = [word.strip() for word in words]


def create_rain():
    t = RawTurtle(turtle_screen)
    rain_turtle_list.append(Rain(t))


def move_rain():
    for rain in rain_turtle_list:
        rain.raw_turtle.clear()
        current_x = rain.raw_turtle.xcor()
        new_y = rain.raw_turtle.ycor() - rain_move_distance
        rain.raw_turtle.goto(current_x, new_y)
        rain.raw_turtle.write(rain.word, font=(FONT_STYLE, 15, "normal"))


def remove_rain_if_needed():
    for rain in rain_turtle_list:
        # When rain hits the ground.
        if rain.raw_turtle.ycor() <= -260:
            # Decrease pH level
            global ph_level
            if ph_level > 0:
                ph_level -= 0.2
                ph_level = round(ph_level, 2)
                ph_level_turtle.clear()
                current_x = ph_level_turtle.xcor()
                new_y = ph_level_turtle.ycor() - 9.5
                ph_level_turtle.goto(current_x, new_y)
                ph_level_turtle.write(f"◀ pH {ph_level}", align="center", font=(FONT_STYLE, 10, "normal"))
                print(ph_level)
            # Remove rain
            rain.raw_turtle.clear()
            rain_turtle_list.remove(rain)


def check_game_over():
    global is_on
    # when ph_level reaches 0, game over
    if ph_level == 0:
        is_on = False
        # Remove all the rains on the screen
        for rain in rain_turtle_list:
            rain.raw_turtle.clear()
        rain_turtle_list.clear()
        # Game Over Label
        game_over_label = Label(text="Game Over", fg="black", font=(FONT_STYLE, 30, "bold"))
        game_over_label.grid(column=0, row=1, rowspan=5)
        # Disable Entry
        entry.config(state="disabled")


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
turtle_screen = TurtleScreen(bg_canvas)
background_img = PhotoImage(file="images/background.png")  # Note: PhotoImage doesn't support '.jpg' format.
bg_canvas.create_image(0, -1, image=background_img)  # turtle coordination used
bg_canvas.grid(column=0, row=1, rowspan=5, padx=(10, 10), pady=(10, 10))

# Entry inside the main image
entry = Entry(bg_canvas.master, width=15, font=(FONT_STYLE, 13, "normal"))
entry.bind("<Return>", enter)
entry.focus()
bg_canvas.create_window(0, 300, window=entry)  # turtle coordination used

# Side Box
# Player name with black background
player_canvas = Canvas(width=140, height=45, bg="black", highlightthickness=0)
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
side_canvas = Canvas(width=140, height=450, highlightthickness=0)
side_canvas.grid(column=1, row=3, columnspan=3, rowspan=3, padx=(0, 10), pady=(10, 10))
side_turtle_screen = TurtleScreen(side_canvas)
side_turtle_screen.bgcolor(DARK_BLUE)

# Stage
stage_label = Label(text="Stage: 1", fg="white", bg=DARK_BLUE, font=(FONT_STYLE, 14, "bold"))
stage_label.grid(column=1, row=3, sticky='s')

# Score with black background
score_canvas = Canvas(width=120, height=45, bg="black", highlightthickness=0)
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

# pH Level Text
ph_level_turtle = RawTurtle(side_turtle_screen)
ph_level_turtle.hideturtle()
ph_level_turtle.penup()
ph_level_turtle.goto(35, 25)
ph_level_turtle.color("white")
ph_level_turtle.write("◀ pH 5.0", align="center", font=(FONT_STYLE, 10, "normal"))

# Bottom Status Box
bottom_status_canvas = Canvas(width=1150, height=30, bg="black", highlightthickness=0)
bottom_status_text = bottom_status_canvas.create_text(
    500,
    15,
    width=500,
    text="",
    fill="white",
    font=(FONT_STYLE, 12, "normal")
)
bottom_status_canvas.grid(column=0, row=6, columnspan=3, pady=(0, 10))

# ----------------------------------------- Animation ------------------------------------- #


get_words_from_the_file()
turtle_screen.tracer(0)  # Turn off animation of generating turtles -> Faster and natural

is_on = True
while is_on:
    time.sleep(0.08)  # Control speed of generating each frame
    # time.sleep(0.05)  # Control speed of generating each frame
    turtle_screen.update()

    # Create rain
    num_for_timing_of_creating_rain += 1
    if num_for_timing_of_creating_rain % 50 == 0 and rain_num < rain_mux_num:
        rain_num += 1
        create_rain()

    move_rain()

    remove_rain_if_needed()

    check_game_over()

window.mainloop()  # Keep the window open

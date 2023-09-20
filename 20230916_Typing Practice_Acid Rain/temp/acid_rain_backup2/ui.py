from tkinter import *
import turtle
import random
import time
from game_manager import GameManager


DARK_BLUE = "#213555"
LIGHT_BLUE = "#4F709C"
BLACK = "black"
FONT_STYLE = "Arial"


class UserInterface:

    def __init__(self):
        self.game = GameManager()

        # -------------------- Window ------------------------ #
        self.window = Tk()
        self.window.title("Typing Practice - Acid Rain")
        self.window.minsize(width=1200, height=800)
        self.window.config(padx=20, pady=20, bg=DARK_BLUE)

        # -------------------- Title ------------------------ #
        self.title_label = Label(text="Acid Rain", fg="white", bg=DARK_BLUE, font=(FONT_STYLE, 18, "bold"))
        self.title_label.grid(column=0, row=0, columnspan=2)

        # -------------------- Light Blue Main Box ------------------------ #
        self.outer_canvas = Canvas(width=1170, height=727, bg=LIGHT_BLUE, highlightthickness=0)
        self.outer_canvas.grid(column=0, row=1, columnspan=2, rowspan=7)

        # -------------------- Main Image ------------------------ #
        self.bg_canvas = Canvas(width=1000, height=667, highlightthickness=0)
        self.turtle_screen = turtle.TurtleScreen(self.bg_canvas)
        # Note: PhotoImage doesn't support '.jpg' format.
        background_img = PhotoImage(file="images/man_on_hill_with_cloud.png")
        self.bg_canvas.create_image(0, -1, image=background_img)  # turtle coordination used
        self.bg_canvas.grid(column=0, row=1, rowspan=5, padx=(10, 10), pady=(10, 10))
        # For turtle animation: Acid Rain

        # Entry inside the main image
        self.entry = Entry(self.bg_canvas.master, width=15, font=(FONT_STYLE, 13, "normal"))
        self.entry.bind("<Return>", self.enter)
        self.entry.focus()
        self.bg_canvas.create_window(0, 300, window=self.entry)  # turtle coordination used

        # -------------------- Side Box ------------------------ #
        # Player name with black background
        self.player_canvas = Canvas(width=140, height=45, bg=BLACK, highlightthickness=0)
        self.player_text = self.player_canvas.create_text(
            70,
            22,
            width=120,
            text="John",
            fill="white",
            font=(FONT_STYLE, 15, "normal")
        )
        self.player_canvas.grid(column=1, row=1, padx=(0, 10), pady=(10, 10))

        # Profile Image
        self.profile_canvas = Canvas(width=140, height=154, highlightthickness=0)
        profile_img = PhotoImage(file="images/man_face_normal.png")
        self.profile_canvas.create_image(70, 77, image=profile_img)
        self.profile_canvas.grid(column=1, row=2, padx=(0, 10))

        # Dark Blue Background Box
        self.side_sub_canvas = Canvas(width=140, height=450, bg=DARK_BLUE, highlightthickness=0)
        self.side_sub_canvas.grid(column=1, row=3, columnspan=3, rowspan=3, padx=(0, 10), pady=(10, 10))

        # Stage
        self.stage_label = Label(text="Stage: 1", fg="white", bg=DARK_BLUE, font=(FONT_STYLE, 14, "bold"))
        self.stage_label.grid(column=1, row=3, sticky='s')

        # Score with black background
        self.score_canvas = Canvas(width=120, height=45, bg=BLACK, highlightthickness=0)
        self.score_text = self.score_canvas.create_text(
            60,
            22,
            width=100,
            text="Score: 0",
            fill="white",
            font=(FONT_STYLE, 12, "normal")
        )
        self.score_canvas.grid(column=1, row=4, padx=(0, 10))

        # pH Bar Image
        self.ph_bar_canvas = Canvas(width=65, height=300, highlightthickness=0)
        ph_bar_img = PhotoImage(file="images/pH_bar.png")
        self.ph_bar_canvas.create_image(32, 150, image=ph_bar_img)
        self.ph_bar_canvas.grid(column=1, row=5, padx=(10, 10), pady=(0, 10), sticky='w')

        # -------------------- Bottom Status Box ------------------------ #
        self.bottom_status_canvas = Canvas(width=1150, height=30, bg=BLACK, highlightthickness=0)
        self.bottom_status_text = self.bottom_status_canvas.create_text(
            500,
            15,
            width=500,
            text="",
            fill="white",
            font=(FONT_STYLE, 12, "normal")
        )
        self.bottom_status_canvas.grid(column=0, row=6, columnspan=3, pady=(0, 10))

        # Keep the window open
        self.window.mainloop()

    def enter(self, event):
        print(self.entry.get())
        self.entry.delete(0, END)
    #
    # def play_game(self):
    #     self.game.update_current_stage_word_list()
    #
    #     is_game_on = True
    #     while is_game_on:
    #         time.sleep(0.2)
    #
    #         self.create_rain()
    #         self.move_rain()
    #
    #         self.window.update()
    #
    # def create_rain(self):
    #     rain_turtle = turtle.RawTurtle(self.turtle_screen)
    #     rain_turtle.hideturtle()
    #     rain_turtle.penup()
    #     # rain_text_label = Label(self.window, text=random_text, font=(FONT_STYLE, 12, "normal"))
    #     # pos_x = random.randrange(100, 900)
    #     x = random.randrange(-400, 400)
    #     y = 300
    #     rain_turtle.goto(x, y)
    #     rain_turtle.setheading(270)
    #     random_text = self.game.get_random_text()
    #     rain_turtle.write(random_text, font=("Arial", 15, "bold"))
    #     self.game.rain_list.append(rain_turtle)
    #
    # def move_rain(self):
    #     for rain_turtle in self.game.rain_list:
    #         rain_turtle.clear()
    #         current_x = rain_turtle.xcor()
    #         new_y = rain_turtle.ycor() - self.game.rain_move_distance
    #         rain_turtle.goto(current_x, new_y)
    #         rain_turtle.write(self.game.get_random_text(), font=("Arial", 15, "bold"))
    #         self.game.rain_list.append(rain_turtle)
    #
    # #         pos_x = int(rain.place_info()["x"])
    # #         pos_y_new = int(rain.place_info()["y"]) + self.game.rain_move_distance
    # #         rain.place(x=pos_x, y=pos_y_new)
    #
    # # def create_rain(self)

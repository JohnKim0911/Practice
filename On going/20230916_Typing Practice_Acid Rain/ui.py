from tkinter import *
from turtle import TurtleScreen, RawTurtle
from tkinter.simpledialog import askstring
from tkinter.messagebox import showinfo
import time
import random
from game import GameManager
from rain import Rain

# ----------------------------------------- Constants ------------------------------------- #
DARK_BLUE = "#213555"
LIGHT_BLUE = "#4F709C"
FONT_FAMILY = "Arial"
RAIN_FONT_STYLE = (FONT_FAMILY, 15, "bold")
# RAIN_FONT_STYLE = (FONT_FAMILY, 10, "normal")


# ----------------------------------------- Class ------------------------------------- #
class UserInterface:

    def __init__(self, game_manager: GameManager):
        self.game = game_manager

        # ----------------------------------------- UI ------------------------------------- #
        self.window = Tk()
        self.window.title("Typing Practice - Acid Rain")
        self.window.minsize(width=1200, height=800)
        self.window.config(padx=20, pady=20, bg=DARK_BLUE)
        # self.window.iconbitmap(r'C:\Users\Madhusudan\Downloads\favicon(2).ico')  # icon

        # Title
        # self.title_label = Label(text="Acid Rain", fg="white", bg=DARK_BLUE, font=(FONT_STYLE, 18, "bold"))
        self.title_label = Label(text="Test", fg="white", bg=DARK_BLUE, font=(FONT_FAMILY, 18, "bold"))
        self.title_label.grid(column=0, row=0, columnspan=2)

        # Light Blue Background Main Box
        self.outer_canvas = Canvas(width=1170, height=727, bg=LIGHT_BLUE, highlightthickness=0)
        self.outer_canvas.grid(column=0, row=1, columnspan=2, rowspan=7)

        # Main Image
        self.bg_canvas = Canvas(width=1000, height=667, highlightthickness=0)
        self.turtle_screen = TurtleScreen(self.bg_canvas)
        background_img = PhotoImage(file="images/background.png")  # Note: PhotoImage doesn't support '.jpg' format.
        self.bg_canvas.create_image(0, -1, image=background_img)
        self.bg_canvas.grid(column=0, row=1, rowspan=5, padx=(10, 10), pady=(10, 10))

        # Entry inside the main image
        self.entry = Entry(self.bg_canvas.master, width=15, font=(FONT_FAMILY, 13, "normal"))
        self.entry.bind("<Return>", self.enter)
        self.entry.focus()
        self.bg_canvas.create_window(0, 300, window=self.entry)

        # Side Box
        # Player name with black background
        self.player_canvas = Canvas(width=140, height=45, bg="black", highlightthickness=0)
        self.player_text = self.player_canvas.create_text(
            70,
            22,
            width=120,
            text="Name",
            fill="white",
            font=(FONT_FAMILY, 15, "normal")
        )
        self.player_canvas.grid(column=1, row=1, padx=(0, 10), pady=(10, 10))

        # Profile Image
        self.profile_canvas = Canvas(width=140, height=154, highlightthickness=0)
        profile_img = PhotoImage(file="images/man_face_normal.png")
        self.profile_canvas.create_image(70, 77, image=profile_img)
        self.profile_canvas.grid(column=1, row=2, padx=(0, 10))

        # Dark Blue Background Box
        self.side_canvas = Canvas(width=140, height=450, highlightthickness=0)
        self.side_canvas.grid(column=1, row=3, columnspan=3, rowspan=3, padx=(0, 10), pady=(10, 10))
        self.side_turtle_screen = TurtleScreen(self.side_canvas)
        self.side_turtle_screen.bgcolor(DARK_BLUE)

        # Stage
        self.stage_label = Label(text="Stage: 1", fg="white", bg=DARK_BLUE, font=(FONT_FAMILY, 14, "bold"))
        self.stage_label.grid(column=1, row=3, sticky='s')

        # Score with black background
        self.score_canvas = Canvas(width=120, height=45, bg="black", highlightthickness=0)
        self.score_text = self.score_canvas.create_text(
            60,
            22,
            width=100,
            text=f"Score: {self.game.score_for_whole_game}",
            fill="white",
            font=(FONT_FAMILY, 12, "normal")
        )
        self.score_canvas.grid(column=1, row=4, padx=(0, 10))

        # pH Bar Image
        self.ph_bar_canvas = Canvas(width=65, height=300, highlightthickness=0)
        ph_bar_img = PhotoImage(file="images/pH_bar.png")
        self.ph_bar_canvas.create_image(32, 150, image=ph_bar_img)
        self.ph_bar_canvas.grid(column=1, row=5, padx=(10, 10), pady=(0, 10), sticky='w')

        # pH Level Text
        self.ph_level_turtle = RawTurtle(self.side_turtle_screen)
        self.ph_level_turtle.hideturtle()
        self.ph_level_turtle.penup()
        self.ph_level_turtle.goto(35, -20)
        self.ph_level_turtle.color("white")
        self.ph_level_turtle.write(f"◀ pH {self.game.ph_level}", align="center", font=(FONT_FAMILY, 10, "normal"))

        # Bottom Status Box
        self.bottom_status_canvas = Canvas(width=1150, height=30, bg="black", highlightthickness=0)
        self.special_effect_description_text = self.bottom_status_canvas.create_text(
            50,
            15,
            width=500,
            text="",
            fill="white",
            font=(FONT_FAMILY, 10, "normal")
        )
        self.current_level_status_text = self.bottom_status_canvas.create_text(
            1080,
            15,
            width=200,
            text=f"Current Stage:  {self.game.rain_num} / {self.game.rain_max_num}",
            fill="white",
            font=(FONT_FAMILY, 10, "normal")
        )
        self.bottom_status_canvas.grid(column=0, row=6, columnspan=3, pady=(0, 10))

        # ----------------------------------------- Game ------------------------------------- #
        self.ask_player_name()  # Save name and display it on UI
        self.turtle_screen.tracer(0)  # Turn off animation of generating turtles -> Faster and natural

        # For Special effects
        # Get this random num for the first round. When going to the next stage, it gets another random number.
        self.game.get_random_special_num()
        self.count_timeout = False
        self.timeout = time.time() + 5  # It will be updated when a special effect is called.

        self.is_game_on = True
        while self.is_game_on:
            time.sleep(0.08)  # Control speed of generating each frame: The lower, the faster
            # time.sleep(0.05)  # Control speed of generating each frame: The lower, the faster
            # time.sleep(0.01)  # Control speed of generating each frame: The lower, the faster
            self.turtle_screen.update()

            # Create rain
            self.game.count_num += 1
            if self.game.time_to_create_rain():
                self.game.count_num = 0
                self.game.rain_num += 1
                self.create_rain()

            # Control rain
            self.move_rain()
            self.remove_rain_when_hitting_ground()

            # "Game over" or "Next stage"
            if self.game.ph_level <= 0:
                self.game_over()
            elif self.game.is_next_stage():  # Next stage when there isn't any rain left.
                self.next_stage()

            # Reset special effect after certain time if needed.
            if self.count_timeout and time.time() > self.timeout:
                self.reset_special_effect()

        self.window.mainloop()  # Keep the window open

    # ----------------------------------------- Functions ------------------------------------- #
    def enter(self, event):
        # When entering special word, activate special effect.
        if self.entry.get() == self.game.special_word:
            self.random_special_effect()
        # Loop through to check if the input is the right answer.
        for rain in self.game.rain_turtle_list:
            # When it's the right answer:
            if self.entry.get() == rain.word:
                if self.game.special_effect_chosen == "hide":
                    rain.raw_turtle.hideturtle()
                self.work_for_right_answer(rain)  # Update score, ph_level and remove rain.
                break
        self.entry.delete(0, END)

    def work_for_right_answer(self, rain):
        """Update score, ph_level and remove rain."""
        # Update score
        self.game.increase_score()
        self.score_canvas.itemconfig(self.score_text, text=f"Score: {self.game.score_for_whole_game}")
        self.bottom_status_canvas.itemconfig(self.current_level_status_text,
                                             text=f"Current Stage:  {self.game.score_for_current_game} / {self.game.rain_max_num}")
        # Update ph_level
        if self.game.ph_level < 6.0:
            self.control_ph_level('+')
        # Remove rain
        rain.raw_turtle.clear()
        self.game.rain_turtle_list.remove(rain)

    def ask_player_name(self):
        self.game.player_name = askstring('Name', 'What is your name?').title()
        self.player_canvas.itemconfig(self.player_text, text=f"{self.game.player_name}")

    def create_rain(self):
        t = RawTurtle(self.turtle_screen)
        rain = Rain(t)
        rain.raw_turtle.hideturtle()
        rain.raw_turtle.penup()
        random_x = random.randrange(-400, 400)
        rain.raw_turtle.goto(random_x, 330)
        rain.word = random.choice(self.game.word_string_list)
        # If it's a special number, set the text color to blue.
        if self.game.special_num == self.game.rain_num:
            rain.raw_turtle.color("blue")
            self.game.special_word = rain.word
        rain.raw_turtle.write(rain.word, font=RAIN_FONT_STYLE)
        self.game.rain_turtle_list.append(rain)

    def move_rain(self):
        for rain in self.game.rain_turtle_list:
            rain.raw_turtle.clear()
            current_x = rain.raw_turtle.xcor()
            new_y = rain.raw_turtle.ycor() - self.game.rain_move_distance
            rain.raw_turtle.goto(current_x, new_y)
            if self.game.special_effect_chosen == "hide":
                rain.raw_turtle.shape("square")
                rain.raw_turtle.shapesize(stretch_wid=1, stretch_len=5)
                rain.raw_turtle.showturtle()
            else:
                rain.raw_turtle.hideturtle()
                rain.raw_turtle.write(rain.word, font=RAIN_FONT_STYLE)

    def remove_rain_when_hitting_ground(self):
        for rain in self.game.rain_turtle_list:
            if rain.raw_turtle.ycor() <= -260:
                # Decrease pH level
                if self.game.ph_level > 0:
                    self.control_ph_level('-')
                # Remove rain
                rain.raw_turtle.clear()
                self.game.rain_turtle_list.remove(rain)

    def control_ph_level(self, symbol):
        if symbol == '+':
            self.game.control_ph_level('+')
            new_y = self.ph_level_turtle.ycor() + 9.8
        else:
            self.game.control_ph_level('-')
            new_y = self.ph_level_turtle.ycor() - 9.8
        two_digits_ph_level = round(self.game.ph_level, 2)
        self.ph_level_turtle.clear()
        current_x = self.ph_level_turtle.xcor()
        self.ph_level_turtle.goto(current_x, new_y)
        self.ph_level_turtle.write(f"◀ pH {two_digits_ph_level}", align="center", font=(FONT_FAMILY, 10, "normal"))

    def game_over(self):
        # Game over when ph_level reaches 0.
        self.is_game_on = False
        # Clear the screen: Remove all rain
        for rain in self.game.rain_turtle_list:
            rain.raw_turtle.clear()
        self.game.rain_turtle_list.clear()
        # Game Over Label
        game_over_label = Label(text="Game Over", fg="black", font=(FONT_FAMILY, 30, "bold"))
        game_over_label.grid(column=0, row=1, rowspan=5)
        # Disable Entry
        self.entry.config(state="disabled")

    def next_stage(self):
        self.game.rain_num = 0
        self.game.rain_move_distance += 1  # Make rain moves faster!
        # Pop-up Message
        showinfo(title=f"You've passed stage {self.game.stage}!", message="Press 'OK' to start the next level.")
        # Reset current stage score
        self.game.score_for_current_game = 0
        self.bottom_status_canvas.itemconfig(self.current_level_status_text,
                                             text=f"Current Stage:  {self.game.score_for_current_game} / {self.game.rain_max_num}")
        # Update stage number
        self.game.stage += 1
        self.stage_label.config(text=f"Stage: {self.game.stage}")
        # Reset Special effect
        self.game.get_random_special_num()
        self.game.reset_special_effect()
        self.bottom_status_canvas.itemconfig(self.special_effect_description_text, text="")
        self.count_timeout = False

    def random_special_effect(self):
        random_num = random.randint(0, 5)
        print(f"random_num: {random_num}")
        if random_num == 0:
            self.change_rain_speed("slower")
        elif random_num == 1:
            self.change_rain_speed("faster")
        elif random_num == 2:
            self.change_rain_speed("stop")
        elif random_num == 3:
            self.remove_all_rain_on_the_screen()
        else:
            self.hide_all_rain_text()

    def set_time_out(self):
        self.count_timeout = True
        self.timeout = time.time() + 5

    def remove_all_rain_on_the_screen(self):
        while len(self.game.rain_turtle_list) != 0:
            for rain in self.game.rain_turtle_list:
                self.work_for_right_answer(rain)
        self.bottom_status_canvas.itemconfig(self.special_effect_description_text, text="Remove all")
        self.set_time_out()

    def change_rain_speed(self, option):
        self.set_time_out()
        if option == "faster":
            self.bottom_status_canvas.itemconfig(self.special_effect_description_text, text="Faster")
        elif option == "slower":
            self.bottom_status_canvas.itemconfig(self.special_effect_description_text, text="Slower")
        elif option == "stop":
            self.bottom_status_canvas.itemconfig(self.special_effect_description_text, text="Stop")
        self.game.change_rain_speed(option)

    def hide_all_rain_text(self):
        self.set_time_out()
        self.game.special_effect_chosen = "hide"
        self.bottom_status_canvas.itemconfig(self.special_effect_description_text, text="Hide all")

    def reset_special_effect(self):
        self.count_timeout = False
        self.bottom_status_canvas.itemconfig(self.special_effect_description_text, text="")
        self.game.reset_special_effect()








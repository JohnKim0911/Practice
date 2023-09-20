from turtle import Screen, shape, Turtle, mainloop
from tkinter import *

window = Tk()
window.title("Yut-nori")
# window.config(padx=50, pady=50, bg="#B1DDC6")

canvas = Canvas(width=900, height=900)
board_img = PhotoImage(file="images/board.gif")
board_background = canvas.create_image(450, 450, image=board_img)
canvas.grid(row=0, column=0)

# screen = Screen()
# screen.setup(width=1100, height=900)
# screen.title("Yut-nori")
# image = "./images/board.gif"
# screen.addshape(image)
# shape(image)

# num_player = screen.textinput(title="How many players?", prompt="Enter the number of players.(2~4):")
colors = ["red", "orange", "green", "blue"]
x_positions = [280, 300, 320, 340]
all_turtles = []


for turtle_index in range(0, 16):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_index])
    new_turtle.goto(x=x_positions[turtle_index], y=-310)
    new_turtle.setheading(90)  # Looking North.
    all_turtles.append(new_turtle)

# print(num_player)

# mainloop()

window.mainloop()

import turtle

screen = turtle.Screen()
screen.setup(width=800, height=600)
image = "./background.gif"
screen.addshape(image)
turtle.shape(image)


def get_mouse_click_coor(x, y):
    print(x, y)


turtle.onscreenclick(get_mouse_click_coor)
turtle.mainloop()

# X coordinate
# left: -400
# right: 400

# Y coordinate
# top: 300
# bottom: -300
# sea line: -219

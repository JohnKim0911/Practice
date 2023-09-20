import turtle

screen = turtle.Screen()
screen.setup(width=900, height=900)
image = "board.gif"
screen.addshape(image)
turtle.shape(image)


def get_mouse_click_coor(x, y):
    print(x, y)


turtle.onscreenclick(get_mouse_click_coor)
turtle.mainloop()


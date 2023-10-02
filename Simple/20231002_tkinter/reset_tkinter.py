from tkinter import *

master = Tk()


def do_something_():
    print('do something')  # I added this so that i can run the code with no errors
    # *performing a function on widget*


def resetAll():
    canvas.destroy()  # destroys the canvas and therefore all of its child-widgets too


canvas = Canvas(master)
canvas.pack()
# creates the cnvas

DoThing = Button(canvas, text='Do Something', command=do_something_).pack(pady=10)
# its master widget is now the canvas

clearall = Button(canvas, text='reset', command=resetAll).pack(pady=10)
# its master widget is now the canvas

master.mainloop()

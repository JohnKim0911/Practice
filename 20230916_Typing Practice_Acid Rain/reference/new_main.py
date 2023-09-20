# https://www.youtube.com/watch?v=UHA0b1DhER0&list=RDCMUC-5Jyf13bHKGGDp2iApfDEw&start_radio=1&rv=UHA0b1DhER0&t=4071

from tkinter import *
from word_lists import ALL_LEVEL_WORDS_LIST
import random
import time
from PIL import Image, ImageTk  # pip install pillow


def enter(event):
    global lab_list
    if ent.get() == lucky_text:  # Causes Special Effect
        for lab in lab_list:
            lab.destroy()
        lab_list = []

    for lab in lab_list:
        if ent.get() == lab.cget("text"):  # Check if the input is the same as the Acid Rain
            lab.destroy()
            lab_list.remove(lab)
            break
    ent.delete(0, len(ent.get()))


win = Tk()
win.geometry("1000x1000+0+5")
win.option_add("*Font", "Arial 20")

# Background
cvs = Canvas(win)
cvs.config(width=1000, height=1000, bd=0, highlightthickness=0)
bg = Image.open("background.gif")
bg = bg.resize((1000, 950), Image.LANCZOS)
bg = ImageTk.PhotoImage(bg, master=win)
cvs.create_image(500, 525, image=bg)
cvs.pack()

voca_list = ALL_LEVEL_WORDS_LIST[0]

ent = Entry(win, width=15)
ent.bind("<Return>", enter)
ent.place(x=400, y=950)

# Display score
lab_point = Label(win, text="")
lab_point.place(x=0, y=0)

# win.mainloop()
win.update()

vel = 5
rain_max = 20
lucky_num = 9
k = 0
rain_num = 0
lab_list = []
damage = 0
lucky_text = ""
stage = 1

while True:
    k += 1
    vel = 1 + stage * 2

    # Create Acid Rain
    if k % 50 == 25 and rain_num < rain_max:
        lab_text = random.choice(voca_list)
        lab = Label(win, text=lab_text)
        if rain_num == lucky_num:  # Special Effect
            lab.config(fg="blue")
            lucky_text = lab_text
        pos_x = random.randrange(0, 900)
        pos_y = 100
        lab.place(x=pos_x, y=pos_y)
        rain_num += 1
        lab_list.append(lab)

    # Move Acid Rain
    for lab in lab_list:
        pos_x = int(lab.place_info()["x"])
        pos_y = int(lab.place_info()["y"])
        pos_y += vel
        lab.place(x=pos_x, y=pos_y)

    # Remove Acid Rain
    for lab in lab_list:
        pos_y = int(lab.place_info()["y"])
        if pos_y >= 900:
            lab.destroy()
            lab_list.remove(lab)
            damage += 1
            break

    # Game Over
    if damage >= 10:
        for wg in win.place_slaves():
            wg.destroy()
        lab = Label(win, text=f"Game Over! You've reached stage {stage}.")
        lab.place(x=300, y=450)
        break
    elif rain_num == rain_max and len(lab_list) == 0:
        lab_go = Label(win, text=f"Passed stage {stage}. The next stage will start in 5 second.")
        lab_go.place(x=200, y=450)
        win.update()
        time.sleep(5)
        lab_go.destroy()
        k = 0
        lucky_text = ""
        stage += 1
        rain_num = 0

    # Display score
    lab_point.config(text=f"Stage {stage}\t\t\t Life: {10-damage}")
    time.sleep(0.05)
    win.update()

win.mainloop()


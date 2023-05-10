from tkinter import *
from subprocess import call
import time

root = Tk()

height = 350
width = 600
x = (root.winfo_screenwidth() // 2) - (width // 2)
y = (root.winfo_screenheight() // 2) - (height // 2)
root.geometry('{}x{}+{}+{}'.format(width, height, x, y))
root.overrideredirect(1)


def quit_screen():
    root.destroy()


appFrame = Frame(
    root,
    width=600,
    height=350,
    bg='#156FA0'
)
appFrame.place(x=0, y=0)

# Image on the right
loading_image = PhotoImage(file="assets/loadingimg.png")
loading = Label(
    appFrame,
    image=loading_image,
    bg='#156FA0'
)
loading.place(x=140, y=-35)

title = Label(
    root,
    text='BlobMaths',
    font=("Loving Snow Trial", 48, "bold"),
    fg='white',
    bg='#156FA0'
)
title.place(x=40, y=90)

text = StringVar()
text.set('Configuring online classroom...')
status = Label(
    root,
    textvariable=text,
    font=("Calibri Light", 13),
    fg='white',
    bg='#156FA0'
)
status.place(x=10, y=315, width=220)

dot1 = PhotoImage(file='assets/dot1.png')
dot2 = PhotoImage(file='assets/dot2.png')

for i in range(5):
    if i == 1:
        text.set("Calibrating projector...")
    elif i == 2:
        text.set("Checking homework...")
    elif i == 3:
        text.set("Dotting i's...")
    elif i == 4:
        text.set("Three")

    l1 = Label(root, image=dot1, border=0, relief=SUNKEN).place(x=45, y=165)
    l2 = Label(root, image=dot2, border=0, relief=SUNKEN).place(x=85, y=165)
    l3 = Label(root, image=dot2, border=0, relief=SUNKEN).place(x=125, y=165)
    l4 = Label(root, image=dot2, border=0, relief=SUNKEN).place(x=165, y=165)
    root.update_idletasks()
    time.sleep(0.5)

    l1 = Label(root, image=dot2, border=0, relief=SUNKEN).place(x=45, y=165)
    l2 = Label(root, image=dot1, border=0, relief=SUNKEN).place(x=85, y=165)
    l3 = Label(root, image=dot2, border=0, relief=SUNKEN).place(x=125, y=165)
    l4 = Label(root, image=dot2, border=0, relief=SUNKEN).place(x=165, y=165)
    root.update_idletasks()
    time.sleep(0.5)

    if i == 1:
        text.set("Printing worksheets...")
    elif i == 2:
        text.set("Grading tests...")
    elif i == 3:
        text.set("Registering attendance...")
    elif i == 4:
        text.set("Two")

    l1 = Label(root, image=dot2, border=0, relief=SUNKEN).place(x=45, y=165)
    l2 = Label(root, image=dot2, border=0, relief=SUNKEN).place(x=85, y=165)
    l3 = Label(root, image=dot1, border=0, relief=SUNKEN).place(x=125, y=165)
    l4 = Label(root, image=dot2, border=0, relief=SUNKEN).place(x=165, y=165)
    root.update_idletasks()
    time.sleep(0.5)

    if i == 1:
        text.set("Unpacking games...")
    elif i == 2:
        text.set("Crossing t's...")

    l1 = Label(root, image=dot2, border=0, relief=SUNKEN).place(x=45, y=165)
    l2 = Label(root, image=dot2, border=0, relief=SUNKEN).place(x=85, y=165)
    l3 = Label(root, image=dot2, border=0, relief=SUNKEN).place(x=125, y=165)
    l4 = Label(root, image=dot1, border=0, relief=SUNKEN).place(x=165, y=165)

    if i == 4:
        time.sleep(0.5)
        text.set("One")

    root.update_idletasks()
    if i == 5:
        time.sleep(1)
    else:
        time.sleep(0.5)

quit_screen()
call(["python", "login.py"])

root.mainloop()

from tkinter import *
from customtkinter import CTkButton
import random

# BACKEND FUNCTIONS

# Function to provide random sums
def get_sum():
    sum1 = random.randint(25, 75)
    sum2 = random.randint(25, 75)
    equation = str(sum1) + " + " + str(sum2)
    final_solution = sum1 + sum2
    return equation, str(final_solution)


def button_text(final_solution):
    answer1 = final_solution - 20
    answer2 = final_solution + 20
    btn_text1 = str(random.randint(answer1, answer2))
    btn_text2 = str(random.randint(answer1, answer2))
    btn_text3 = str(random.randint(answer1, answer2))
    btn_text4 = str(random.randint(answer1, answer2))

    array = [btn_text1, btn_text2, btn_text3, btn_text4]
    while array.count(array[0]) != 1 or array.count(array[1]) != 1 or array.count(array[2]) != 1 or array.count(array[3]) != 1:
        btn_text1 = str(random.randint(answer1, answer2))
        btn_text2 = str(random.randint(answer1, answer2))
        btn_text3 = str(random.randint(answer1, answer2))
        btn_text4 = str(random.randint(answer1, answer2))

    key = random.randint(1, 4)
    if key == 1:
        btn_text1 = final_solution
    elif key == 2:
        btn_text2 = final_solution
    elif key == 3:
        btn_text3 = final_solution
    elif key == 4:
        btn_text4 = final_solution

    return btn_text1, btn_text2, btn_text3, btn_text4


def submit(btn, btntxt, final_solution):
    if int(btntxt) == int(final_solution):
        message.config(fg='#006400')
        tick_cross.config(fg='#069420')
        tick_cross.config(text="✔")
        if btn == 1:
            tick_cross.place(x=90, y=350, height=100, width=100)
        elif btn == 2:
            tick_cross.place(x=1070, y=350, height=100, width=100)
        elif btn == 3:
            tick_cross.place(x=90, y=520, height=100, width=100)
        elif btn == 4:
            tick_cross.place(x=1070, y=520, height=100, width=100)
        btn1.configure(state='disabled')
        btn2.configure(state='disabled')
        btn3.configure(state='disabled')
        btn4.configure(state='disabled')
        text.set("                                Well done!\n                                " + final_solution + " is the correct answer.")
    else:
        message.config(fg='#8B0000')
        tick_cross.config(fg='#bf372b')
        tick_cross.config(text="✘")
        if btn == 1:
            tick_cross.place(x=90, y=350, height=100, width=100)
        elif btn == 2:
            tick_cross.place(x=1070, y=350, height=100, width=100)
        elif btn == 3:
            tick_cross.place(x=90, y=520, height=100, width=100)
        elif btn == 4:
            tick_cross.place(x=1070, y=520, height=100, width=100)
        btn1.configure(state='disabled')
        btn2.configure(state='disabled')
        btn3.configure(state='disabled')
        btn4.configure(state='disabled')
        text.set("                                Not this time!\n                                " + final_solution + " is the correct answer.")


# END OF BACKEND

root = Tk()
root.geometry('1366x768')
root.title('Sum of the Day')
root.state('zoomed')
root.resizable(width=False, height=False)


# Image for the background
bg = PhotoImage(file="assets/gamebg.png")
label1 = Label(root, image=bg)
label1.place(x=0, y=0)


# Initialises and places the game window
appFrame = Frame(
    root,
    height=830,
    width=1260,
    bg='#dfe3ee'
)
appFrame.place(x=330, y=120)


# Brief game description
text1 = Label(
    appFrame,
    text="Choose the correct answer to the following sum:",
    bg='#dfe3ee',
    font=('yu gothic ui', 28, 'bold')
)
text1.place(x=200, y=60)


equation, final_solution = get_sum()

sumQuestion = Label(
    root,
    font=("Hack 20", 70),
    text=equation,
    bg='#dfe3ee'
)
sumQuestion.place(x=800, y=290)


btntxt1, btntxt2, btntxt3, btntxt4 = button_text(int(final_solution))

btn1 = CTkButton(
    master=appFrame,
    text=btntxt1,
    text_font=('yu gothic ui', 75, 'bold'),
    text_color='white',
    bg_color='#dfe3ee',
    fg_color='#5077bd',
    cursor='hand2',
    corner_radius=70,
    command=lambda : submit(1, btntxt1, final_solution)
)
btn1.place(x=190, y=330, height=150, width=430)

btn2 = CTkButton(
    master=appFrame,
    text=btntxt2,
    text_font=('yu gothic ui', 75, 'bold'),
    text_color='white',
    bg_color='#dfe3ee',
    fg_color='#5077bd',
    cursor='hand2',
    corner_radius=70,
    command=lambda : submit(2, btntxt2, final_solution)
)
btn2.place(x=640, y=330, height=150, width=430)

btn3 = CTkButton(
    master=appFrame,
    text=btntxt3,
    text_font=('yu gothic ui', 75, 'bold'),
    text_color='white',
    bg_color='#dfe3ee',
    fg_color='#5077bd',
    cursor='hand2',
    corner_radius=70,
    command=lambda : submit(3, btntxt3, final_solution)
)
btn3.place(x=190, y=500, height=150, width=430)

btn4 = CTkButton(
    master=appFrame,
    text=btntxt4,
    text_font=('yu gothic ui', 75, 'bold'),
    text_color='white',
    bg_color='#dfe3ee',
    fg_color='#5077bd',
    cursor='hand2',
    corner_radius=70,
    command=lambda : submit(4, btntxt4, final_solution)
)
btn4.place(x=640, y=500, height=150, width=430)


# Checkmark displays if choice is correct
tick_cross = Label(
    appFrame,
    text="✔",
    bg='#dfe3ee',
    font=('yu gothic ui', 80),
    fg='#069420'
)


text = StringVar()

message = Label(
    appFrame,
    textvariable=text,
    font=('yu gothic ui', 26, 'bold'),
    bg='#dfe3ee',
    anchor=CENTER
)
message.place(x=130, y=675)


blobmaths = Label(
    root,
    text="BlobMaths",
    font=("Loving Snow Trial", 60),
    bg='#3B7EC1',
    fg='white'
)
blobmaths.place(x=780, y=30)


root.mainloop()

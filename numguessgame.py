from tkinter import *
import tkinter.messagebox as msg
from customtkinter import CTkButton
import random


# BACKEND FUNCTIONS


# Function to validate inputs
def validation():
    guessed_num = guessEntry.get()
    if len(guessed_num) > 0:
        if not guessed_num.isdigit():
            msg.showinfo("Oops", "Letters, symbols and punctuation aren\'t allowed")
    if len(guessed_num) == 0 or int(guessed_num) > 50 or int(guessed_num) == 0:
        msg.showinfo("Oops", "Type a number between 1 and 50 in the box.")
    else:
        if int(guessed_num) < 0:
            msg.showinfo("Oops", "The number can\'t be negative")
        else:
            guess()


# Main backend function to compare input num to target num
def guess():
    global count
    global text
    global flag
    count -= 1
    guessed_num = int(guessEntry.get())
    if rand_num == guessed_num:
        text.set("             Whoopee! You guessed the right number! " + "\n             You scored " + str(
            count) + " out of 10.")
        tick.place(x=780, y=270)
        flag = True
    if count == 0:
        text.set("                 Game over! You have no attempts left.")
        cross.place(x=780, y=270)
        flag = True
    elif rand_num > guessed_num:
        text.set("\t   Uh-oh! Wrong number, guess higher.\n" + "\t   You have " + str(count) + " attempts remaining.")
    elif rand_num < guessed_num:
        text.set("\t   Yikes! Wrong number, guess lower.\n" + "\t   You have " + str(count) + " attempts remaining.")
    if flag == True:
        guessButton.configure(state='disabled')


# END OF BACKEND

root = Tk()
root.geometry('1366x768')
root.title('Guess the Number')
root.state('zoomed')
root.resizable(width=False, height=False)

# Image for the background
bg = PhotoImage(file="gamebg.png")
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
    text="Let's play a game! I've got a number from 1 to 50 in\n my head. Guess it right, and you win.",
    bg='#dfe3ee',
    font=('yu gothic ui', 28, 'bold')
)
text1.place(x=200, y=90)

# Input text box for the guessed number#
guessEntry = Entry(
    appFrame,
    highlightthickness=3,
    relief='flat',
    font=('yu gothic ui', 120, 'bold')
)
guessEntry.place(x=520, y=275, height=168, width=240)
guessEntry.config(highlightbackground='#6b6a69', highlightcolor='#7852e6')

# Button to confirm guess
flag = False
guessButton = CTkButton(
    master=appFrame,
    text="""GUESS""",
    text_font=('yu gothic ui', 36, 'bold'),
    text_color='white',
    bg_color='#dfe3ee',
    fg_color='#5077bd',
    cursor='hand2',
    corner_radius=27,
    command=lambda: validation()
)
guessButton.place(x=520, y=450, height=100, width=240)

# Checkmark displays if guess is correct
tick = Label(
    appFrame,
    text="✔",
    bg='#dfe3ee',
    font=('Helvetica', 120),
    fg='#069420'
)

# Cross displays if all guesses are incorrect
cross = Label(
    appFrame,
    text="✘",
    bg='#dfe3ee',
    font=('Helvetica', 120),
    fg='#bf372b'
)

count = 10

text = StringVar()
text.set('You have 10 chances to guess the secret number, good luck!')

rand_num = random.randint(1, 50)

guessCount = Label(
    appFrame,
    textvariable=text,
    font=('yu gothic ui', 26, 'bold'),
    bg='#dfe3ee',
    anchor=CENTER
)
guessCount.place(x=170, y=630)

blobmaths = Label(
    root,
    text="BlobMaths",
    font=("Loving Snow Trial", 60),
    bg='#3B7EC1',
    fg='white'
)
blobmaths.place(x=780, y=30)

root.mainloop()

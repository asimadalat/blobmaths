from tkinter import *
import tkinter.messagebox as msg
from customtkinter import CTkButton
import random
from random import shuffle


# Function to validate inputs
def validation():
    entered_word = wordEntry.get()

    if len(entered_word) == 0:
        msg.showinfo("Oops", "Type a word in the box")
    else:
        if entered_word.isalpha() == FALSE:
            msg.showinfo("Oops", "Only letters from A-Z are allowed")
        else:
            submit()


words = ["apple", "autumn", "answer", "afraid", "arrive", "ball", "bank", "birthday", "black", "bridge",
         "baby", "century", "cross", "coin", "country", "cake", "cool", "dirty", "dark", "destroy", "dream",
         "dance", "empty", "electric", "elephant", "evening", "family", "garden", "hobby", "island", "jelly",
         "king", "ladder", "morning", "needle", "opposite", "problem", "question", "ruler", "scissors", "table",
         "understand", "village", "water", "yesterday", "zero"]
questions = []


for word in words:
    answers = list(word)
    shuffle(answers)
    questions.append(answers)

num = random.randint(0, len(questions)-1)


def initialise_game():
    global questions
    global num
    scrambledWord.config(text=questions[num])


def next_word():
    global questions
    global num
    global words
    global tick
    tick_cross.config(text="")
    text.set("")
    checkButton.configure(state='normal')
    num = random.randint(0, len(questions)-1)
    scrambledWord.config(text=questions[num])
    user_line.config(fg='#03a9f4')


def submit():
    global questions
    global num
    global words
    user = wordEntry.get()
    if user == words[num]:
        message.config(fg='#006400')
        tick_cross.config(fg='#069420')
        tick_cross.config(text="✔")
        tick_cross.place(x=654, y=447, height=60, width=50)
        checkButton.configure(state='disabled')
        text.set("                             Well done!\n                             You found the right word.")
    else:
        message.config(fg='#8B0000')
        tick_cross.config(fg='#bf372b')
        tick_cross.config(text="✘")
        tick_cross.place(x=654, y=447, height=60, width=50)
        text.set("                                  Try again.\n                                Your guess was wrong.")
        wordEntry.delete(0, END)


root = Tk()


root.geometry('1366x768')
root.title('Unscramble the Word')
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


# Description of game rules
text1 = Label(
    appFrame,
    text="Time for some fun with words! These random \nwords have been scrambled up. Enter the right words\n below to win!",
    bg='#dfe3ee',
    font=('yu gothic ui', 28, 'bold')
)
text1.place(x=170, y=60)


# Word to be unscrambled
scrambledWord = Label(
    root,
    font=("Hack 20", 70),
    text=questions[num],
    bg='#dfe3ee'
)
scrambledWord.pack(pady=360, ipadx=10, ipady=10)


rounded_rec = PhotoImage(file="rectrounded.png")
rect = Label(
    appFrame,
    image=rounded_rec,
    bg='#dfe3ee'
)
rect.place(x=335, y=435)

# Input text box for the guessed number#
wordEntry = Entry(
    appFrame,
    #highlightthickness=3,
    relief='flat',
    border=0,
    font=('yu gothic ui', 35, 'bold')
)
wordEntry.place(x=360, y=450, height=60, width=340)
wordEntry.config(highlightbackground='#6b6a69', highlightcolor='#7852e6')



# Button to confirm guess
checkButton = CTkButton(
    master=appFrame,
    text="""Try""",
    text_color='white',
    text_font=('yu gothic ui', 36, 'bold'),
    corner_radius=45,
    bg_color='#dfe3ee',
    fg_color='#5077bd',
    cursor='hand2',
    command=lambda : validation()
)
checkButton.place(x=735, y=437, height=85, width=200)


# Displays another scrambled word
nextButton = CTkButton(
    master=appFrame,
    text="""Next word""",
    text_color='white',
    text_font=('yu gothic ui', 36, 'bold'),
    corner_radius=27,
    bg_color='#dfe3ee',
    fg_color='#5077bd',
    cursor='hand2',
    command=lambda :next_word()
)
nextButton.place(x=465, y=540, height=80, width=330)


# Checkmark displays if word is correct
tick_cross = Label(
    appFrame,
    text="✔",
    bg='#ffffff',
    font=('yu gothic ui', 50),
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
message.place(x=130, y=665)


blobmaths = Label(
    root,
    text="BlobMaths",
    font=("Loving Snow Trial", 60),
    bg='#3B7EC1',
    fg='white'
)
blobmaths.place(x=780, y=30)


initialise_game()

root.mainloop()
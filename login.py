from tkinter import *
import tkinter.messagebox as msg
from subprocess import call


# BACKEND FUNCTIONS




# END OF BACKEND

def main():
    def exit_window():
        root.destroy()

    def callback_entry1_focus(event):
        user = user_name.get()
        password = pass_word.get()
        user_line.config(fg='#03a9f4')
        pass_line.config(fg='#000000')
        if user == "Username":
            user_name.delete(0, END)
            user_name.config(fg='black')
        if password == "":
            pass_word.insert(0, "Password")
            pass_word.config(fg='grey', show='')

    def callback_entry2_focus(event):
        user = user_name.get()
        password = pass_word.get()
        pass_line.config(fg='#03a9f4')
        user_line.config(fg='#000000')
        if password == "Password":
            pass_word.delete(0, END)
            pass_word.config(fg='black', show='*')
        if user == "":
            user_name.insert(0, "Username")
            user_name.config(fg='grey')

    def login():
        user = user_name.get()
        password = pass_word.get()
        if user == 'User' and password == '54321':
            exit_window()
            call(["python", "mainGUI.py"])
        else:
            msg.showinfo("Oops", "Username or password is incorrect")

    root = Tk()

    height = 700
    width = 1100
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 2) - (height // 2)
    root.geometry('{}x{}+{}+{}'.format(width, height, x, y))

    root.title('Login')
    root.config(bg='#ffffff')
    root.resizable(False, False)

    # RIGHT

    side_image = PhotoImage(file="loginbg.png")
    side = Label(
        root,
        image=side_image,
    )
    side.place(x=598, y=-2)

    # RIGHT


    # LEFT

    plain = PhotoImage(file="plain.png")
    plane = Label(
        root,
        image=plain,
        bg='#ffffff'
    )
    plane.place(x=260, y=610)


    blobmaths = Label(
        root,
        text="BlobMaths",
        font=("Loving Snow Trial", 40),
        bg='#ffffff',
        fg='#000000'
    )
    blobmaths.place(x=185, y=30)


    logFrame = Frame(
        root,
        bg='#ffffff'
    )
    logFrame.place(x=75, y=100, width=450, height=480)


    welcome = Label(
        logFrame,
        text="Welcome!",
        font=("Calibri Light", 30),
        bg='#ffffff'
    )
    welcome.place(x=145, y=30)


    log_prompt = Label(
        logFrame,
        text="Please enter your login details below:",
        font=("Calibri Light", 15),
        bg='#ffffff'
    )
    log_prompt.place(x=85, y=100)


    user_name = Entry(
        logFrame,
        font=("Calibri Light", 25),
        fg='grey',
        bg='#ffffff',
        border=0
    )
    user_name.place(x=85, y=165, width=300, height=50)
    user_name.insert(0, "Username")

    user_line = Label(
        logFrame,
        text="━━━━━━━━━━━━━━━",
        font=("Calibri Light", 15),
        fg='#000000',
        bg='#ffffff'
    )
    user_line.place(x=82, y=210, height=5)

    pass_word = Entry(
        logFrame,
        font=("Calibri Light", 25),
        fg='grey',
        bg='#ffffff',
        border=0
    )
    pass_word.place(x=85, y=250, width=300, height=50)
    pass_word.insert(0, "Password")

    pass_line = Label(
        logFrame,
        text="━━━━━━━━━━━━━━━",
        font=("Calibri Light", 15),
        bg='#ffffff'
    )
    pass_line.place(x=82, y=295, height=5)


    log_in = Button(
        logFrame,
        text="""LOG IN""",
        font=("Loving Snow Trial", 30),
        fg='#ffffff',
        bg='#1676BC',
        bd=1,
        relief='flat',
        cursor='hand2',
        command=lambda : login()
    )
    log_in.place(x=135, y=350, width=200, height=80)


    account = Label(
        root,
        text="Don't have an account?\nVisit our website!",
        font=('Calibri Light', 15),
        bg='#ffffff',
        anchor=CENTER
    )
    account.place(x=215, y=575)

    # LEFT

    user_name.bind("<FocusIn>", callback_entry1_focus)
    pass_word.bind("<FocusIn>", callback_entry2_focus)

    root.mainloop()

main()
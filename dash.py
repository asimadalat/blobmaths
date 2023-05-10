from tkinter import *


root = Tk()
root.title("Dashboard")
root.geometry('1366x768')
root.state('zoomed')
root.config(background='#dfe3ee')
root.resizable(width=False, height=False)

def quit_screen():
    root.destroy()


# Sidebar
sidebar = Frame(root, bg='#000034')#
sidebar.place(x=0, y=0, width=400, height=1057)


avatar_image = PhotoImage(file="assets/avatar.png")
logo = Label(
    sidebar,
    image=avatar_image,
    bg='#000034'
)
logo.place(x=90, y=125)

name = Label(
    sidebar,
    text="John Doe",
    bg='#000034',
    fg='white',
    font=("Calibri Light", 35, "bold")
)
name.place(x=110, y=400)


dash_icon = PhotoImage(file="assets/dashicon.png")
dash = Label(
    sidebar,
    image=dash_icon,
    bg='#000034'
)
dash.place(x=45, y=520)

dash_button = Button(
    sidebar,
    text="Dashboard",
    bg='#000034',
    fg='white',
    font=("Calibri Light", 25),
    bd=0,
    cursor='hand2',
    activebackground='white'
)
dash_button.place(x=120, y=520)

manage_icon = PhotoImage(file="assets/manageicon.png")
manage = Label(
    sidebar,
    image=manage_icon,
    bg='#000034'
)
manage.place(x=45, y=600)

manage_button = Button(
    sidebar,
    text="Manage",
    bg='#000034',
    fg='white',
    font=("Calibri Light", 25),
    bd=0,
    cursor='hand2',
    activebackground='white'
)
manage_button.place(x=120, y=600)

cog_icon = PhotoImage(file="assets/cogicon.png")
cog = Label(
    sidebar,
    image=cog_icon,
    bg='#000034'
)
cog.place(x=45, y=680)

cog_button = Button(
    sidebar,
    text="Settings",
    bg='#000034',
    fg='white',
    font=("Calibri Light", 25),
    bd=0,
    cursor='hand2',
    activebackground='white'
)
cog_button.place(x=120, y=680)

exit_icon = PhotoImage(file="assets/exiticon.png")
exited = Label(
    sidebar,
    image=exit_icon,
    bg='#000034'
)
exited.place(x=45, y=760)

exit_button = Button(
    sidebar,
    text="Exit",
    bg='#000034',
    fg='white',
    font=("Calibri Light", 25),
    bd=0,
    cursor='hand2',
    activebackground='white',
    command=quit_screen
)
exit_button.place(x=120, y=760)


log_text = Button(
    sidebar,
    text="Log Out ➲",
    bg='#000034',
    font=("Calibri Light", 40),
    bd=0,
    fg='white',
    cursor='hand2',
    activebackground='white'
)
log_text.place(x=70, y=920, width=260, height=80)


blobmaths = Label(
    sidebar,
    text="BlobMaths",
    font=("Loving Snow Trial", 40),
    bg='#000034',
    fg='white'
)
blobmaths.place(x=80, y=30)
# Sidebar


# Body
heading = Label(
    root,
    text="Dashboard",
    font=("Calibri Light", 35, "bold"),
    fg='#0a08b2',
    bg='#dfe3ee'
)
heading.place(x=435, y=20)


frame1 = Frame(
    root,
    bg='white'
)
frame1.place(x=442, y=100, width=1425, height=550)

frame2 = Frame(
    root,
    bg='#006200'
)
frame2.place(x=520, y=700, width=360, height=280)
frame2_label = Label(
    frame2,
    text='Logged In:',
    font=("Calibri Light", 30),
    bg='#006200',
    fg='white'
)
frame2_label.place(x=20, y=20)
frame2_data = Label(
    frame2,
    text='27',
    font=("Calibri Light", 100),
    bg='#006200',
    fg='white'
)
frame2_data.place(x=110, y=70)

frame3 = Frame(
    root,
    bg='#FFBF00'
)
frame3.place(x=970, y=700, width=360, height=280)
frame3_label = Label(
    frame3,
    text='Completed Work:',
    font=("Calibri Light", 30),
    bg='#FFBF00',
    fg='white'
)
frame3_label.place(x=20, y=20)
frame3_data = Label(
    frame3,
    text='18',
    font=("Calibri Light", 100),
    bg='#FFBF00',
    fg='white'
)
frame3_data.place(x=110, y=70)

frame4 = Frame(
    root,
    bg='#4169e1'
)
frame4.place(x=1420, y=700, width=360, height=280)
frame4_label = Label(
    frame4,
    text='Overachieved:',
    font=("Calibri Light", 30),
    bg='#4169e1',
    fg='white'
)
frame4_label.place(x=20, y=20)
frame4_data = Label(
    frame4,
    text='6',
    font=("Calibri Light", 100),
    bg='#4169e1',
    fg='white'
)
frame4_data.place(x=110, y=70)


pie_chart = PhotoImage(file="assets/piechart.png")
pie = Label(
    frame1,
    image=pie_chart,
    bg='white'
)
pie.place(x=830, y=35)

bar_chart = PhotoImage(file="assets/barchart.png")
bar = Label(
    frame1,
    image=bar_chart,
    bg='white'
)
bar.place(x=130, y=50)
#body


root.mainloop()

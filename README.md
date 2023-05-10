# blobmaths
An platform for young learners to supplement education.
The Loving Snow.ttf file must be used to install the custom font.

## loading.py
If the application was a single executable, this would run first. It is a simple splash screen with a loading animation, leading into the login screen.

## login.py
The login window will be used by students and teachers to access the platform. The correct username and password is currently 'User' and '54321' respectively and on entry, the window will close. Any incorrect entry and an error message will popup informing the user.

## dash.py
Teacher dashboard where statistics about how many students completed the homework, how many logged in, overachievers etc. can be viewed. For now, as the database isn't developed, the stats are image mockups.

## idgenerate.py
Used to generate unique IDs for teachers, students or classes.

## numguessgame.py
A random number between 1 and 50 is generated and the student has 10 attempts to correctly guess it.

## wordmixupgame.py
The student must unscramble the words displayed on-screen.

## sumoftheday.py
A difficult sum is displayed on-screen and the student must pick the correct answer from a choice of four.

## Libraries/Packages Used:
future
customtkinter
random
string
subprocess
time


#Creating a simple button in Python


# '*' means import everything

from tkinter import *

master = Tk()

def closewindow():
    exit()

#Button not button

button = Button(master, text="Close Window", command=closewindow)

#Button.pack adds things to the window

button.pack()

#mainloop is to run a program

mainloop()

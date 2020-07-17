#List of functions that will help me with my other files.
from tkinter import *
from tkinter import messagebox

#Places window at center of the screen
def center_window(root, size):
    win_size = size.split("x")

    screen_height = root.winfo_screenheight()
    screen_width = root.winfo_screenwidth()

    win_x = int((screen_width/2) - (int(win_size[0])/2))
    win_y = int((screen_height/2) - (int(win_size[1])/2))

    root.geometry("{0}+{1}+{2}".format(size, win_x, win_y))

#Creates window using specifications
def create_window(root, title, color):
    root.title(title)
    root.configure(background=color)

#Displays error window with specified message
def errorBox(message):
    messagebox.showerror("ERROR", message)
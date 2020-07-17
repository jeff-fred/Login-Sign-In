#Create a sign up window that writes on to csv files new users

import funcs
import csv
from tkinter import *



#Creating a window
class SignIn:
    def __init__(self):
        """Initialize window and all its functions"""
        self.root = Tk()

        #Window options
        self.title = "Sign In"
        self.color = "lightgray"
        self.size = "225x200"

        funcs.create_window(self.root, self.title, self.color)
        funcs.center_window(self.root, self.size)

        #Creating window grid system
        rows = 0
        while rows < 4:
            self.root.rowconfigure(rows, weight=1)
            rows += 1
        
        cols = 0
        while cols < 2:
            self.root.columnconfigure(cols, weight=1)
            cols += 1

        self.userEntry = Entry(self.root)
        self.passEntry = Entry(self.root, show="*")

        self.setup_widgets()

        self.root.mainloop()


    def setup_widgets(self):
        """Set up window layout"""
        #Labels
        Label(
            self.root,
            text="Create a login.",
            bg=self.color
        ).grid(row=0, columnspan=2)       

        Label(
            self.root,
            text="Username:",
            bg=self.color
        ).grid(row=1, column=0)

        Label(
            self.root,
            text="Password:",
            bg=self.color
        ).grid(row=2, column=0)

        #Entries
        self.userEntry.grid(row=1, column=1)
        self.passEntry.grid(row=2, column=1)

        #Buttons
        Button(
            self.root,
            text="Sign In",
            bg=self.color,
            command=self.createUser
        ).grid(row=3, column=1)

        Button(
            self.root,
            text="Cancel",
            fg="red",
            command=self.cancel
        ).grid(row=3, column=0)

    def cancel(self):
        self.root.destroy()

    def createUser(self):
        user = str(self.userEntry.get())
        passwrd = str(self.passEntry.get())

        if user == "" or passwrd == "":
            funcs.errorBox("Input valid information")
        else:
            with open("C:\\Users\\jeffe\\OneDrive\\Python\\Projects\\finance\\login_data.csv", "a", newline="") as csvfile:
                fieldnames = ["usernames","passwords"]
                csv_writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                csv_writer.writerow({"usernames": user,"passwords": passwrd})

                self.userEntry.delete(0,"end")
                self.passEntry.delete(0,"end")



if __name__ == "__main__":
    SignIn()
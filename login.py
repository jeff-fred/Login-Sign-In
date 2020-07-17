#Create a login window that validates its entry from a file

import csv
import funcs
import signIn
from tkinter import *




#Window creation
class Login:
    def __init__(self):
        """Initialize window and funcs"""
        self.root = Tk()

        self.title = "Login"
        self.color = "lightgray"
        self.size = "250x250"

        funcs.create_window(self.root, self.title, self.color)
        funcs.center_window(self.root, self.size)

        #Create window grid system
        rows = 0
        while rows < 7:
            self.root.rowconfigure(rows, weight=1)
            rows += 1
        
        cols = 0
        while cols < 1:
            self.root.columnconfigure(cols, weight=1)
            cols += 1

        self.userEntry = Entry(self.root)
        self.passEntry = Entry(self.root, show="*")

        self.setup_widgets()

        self.root.mainloop()
        
    def setup_widgets(self):
        """Set up the layout of the window"""
        
        #Labels
        Label(
            self.root,
            text="Welcome! Please sign in and/or login",
            bg = self.color
        ).grid(row=0, column=0)

        Label(
            self.root,
            text="Username:",
            bg=self.color
        ).grid(row=1, columnspan=2)

        Label(
            self.root,
            text="Password:",
            bg=self.color
        ).grid(row=3, columnspan=2)

        #Entries
        self.userEntry.grid(row=2, columnspan=2)
        self.passEntry.grid(row=4, columnspan=2)

        #Buttons
            #Login Button
        Button(
            self.root,
            text="Login",
            bg=self.color,
            command=self.login
        ).grid(row=5, columnspan=2)

            #Sign In Button
        Button(
            self.root,
            text="Sign In",
            bg=self.color,
            fg="red",
            command=self.sign_in
        ).grid(row=6, columnspan=2)

    def login(self):
        """Allow user pass if name on csv file"""
        with open("C:\\Users\\jeffe\\OneDrive\\Python\\Projects\\finance\\login_data.csv", "r", newline="") as csvfile:
            csv_reader = csv.DictReader(csvfile, fieldnames=["usernames","passwords"])

            for line in csv_reader:
                if line["usernames"] == str(self.userEntry.get()) and line["passwords"] == str(self.passEntry.get()):
                    login = True
                    break
                else:
                    login = False

            if login == True:
                self.root.destroy()
            else:
                self.userEntry.delete(0,"end")
                self.passEntry.delete(0,"end")

    def sign_in(self):
        signIn.SignIn()

        
if __name__ == "__main__":
    Login()
import tkinter as tk
from tkinter import messagebox

window = tk.Tk()

## Need to implement logic for returning
## 1) Check if Book has been borrowed
## 1a) If not borrowed, show error message
## 2) Check if book returned on time
## 2a) If not, add fine to member
## 2b) Show message that fine has been added
## 3) Return book

def returnBook():
    tk.messagebox.showerror(
        "Filler Error",
        "Error: Function not complete yet!")

def isBookBorrowed():
    tk.messagebox.showerror(
        "Filler Error",
        "Error: Function not complete yet!")

def isBookReturnedOnTime():
    tk.messagebox.showerror(
        "Filler Error",
        "Error: Function not complete yet!")

def goBack():
    window.destroy()
    import loans

def goHome():
    window.destroy()
    import landingPage

titleLabel = tk.Label(
    text="Book Returning",
    bg="cornsilk",
    font=("20"))

bookNumLabel = tk.Label(
    text="Please Insert Book Accession Number")

bookNumEntry = tk.Entry(window);

returnBookButton = tk.Button(
    text="Confirm",
    width=8,
    height=2,
    command=returnBook)

backButton = tk.Button(text = "Back",
                         width=5,
                         height=2,
                         bg="AntiqueWhite",
                         command=goBack)

homeButton = tk.Button(text = "Home",
                         width=5,
                         height=2,
                         bg="AntiqueWhite",
                         command=goHome)

titleLabel.grid(row=0, column=0);
backButton.grid(row=0, column=1);
homeButton.grid(row=0, column=2);

bookNumLabel.grid(row=1, column=0);
bookNumEntry.grid(row=1, column=2);

returnBookButton.grid(row=2, column=1);

window.mainloop()


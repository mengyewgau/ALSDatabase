import tkinter as tk
from tkinter import messagebox

window = tk.Tk()

## Need to implement logic for borrowing
## 1) Check if Book has been borrowed
## 1a) If borrowed, show error message
## 2) Check if member can borrow books
## 2a) If cannot, show error message
## 3) Borrow book

def borrowBook():
    tk.messagebox.showerror(
        "Filler Error",
        "Error: Function not complete yet!")

def isBookBorrowed():
    tk.messagebox.showerror(
        "Filler Error",
        "Error: Function not complete yet!")

def canMemberBorrow():
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
    text="Book Borrowing",
    bg="cornsilk",
    font=("20"))

bookNumLabel = tk.Label(
    text="Please Insert Book Accession Number")

bookNumEntry = tk.Entry(window);

memberIdLabel = tk.Label(
    text="Please Insert Member Id")

memberIdEntry = tk.Entry(window);

borrowBookButton = tk.Button(
    text="Borrow",
    width=8,
    height=2,
    command=borrowBook)

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

memberIdLabel.grid(row=2, column=0);
memberIdEntry.grid(row=2, column=2);

borrowBookButton.grid(row=3, column=1);

window.mainloop()


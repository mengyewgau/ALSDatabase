from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image

window = Tk()


## Loans Landing Page
def destroyLoansMenu():
    loansMenu.destroy()

def openBorrow():
    loansBorrowMenuFunc()
    destroyLoansMenu()
    loansBorrowMenu.lift()
    loansBorrowMenu.lift()

def openReturn():
    loansReturnMenuFunc()
    destroyLoansMenu()
    loansReturnsMenu.lift()
    loansReturnsMenu.lift()


def goHome():
    window.destroy()
    import landingPage

def loansMenuFunc():
    global loansMenu
    loansMenu = Toplevel()
    loansMenu.title("Loans Menu")
    loansMenu.geometry("1280x720")

    topleftheader = Label(loansMenu,
    	text = "BT2102",
    	bg = "lightblue",
    	borderwidth = 2,
    	relief = "solid",
    	font = ("Mincho", 40))
    topleftheader.place(x = 0, y = 0, width = 280, height = 100)

    topbar = Label(loansMenu,
    	text = "ALS",
    	bg = "lightblue", 
    	borderwidth = 2,
    	relief = "ridge",
    	font = ("Mincho", 40))
    topbar.place(x = 280, y = 0, width = 1000, height = 100)

    sidebar = Label(loansMenu,
    	text = "Loans",
    	bg = "lightblue", 
    	borderwidth = 2,
    	relief = "ridge",
    	font = ("Mincho", 28))
    sidebar.place(x = 0, y = 100, width = 280, height = 620)    

    homeButton = Button(loansMenu,
                        text = "Back",
                         width=10,
                         height=2,
                         bg="AntiqueWhite",
                         command=goHome)
    homeButton.place(x=660, y=200, width=150, height=50)


    buttonBorrow = Button(loansMenu,
    					text = "Borrow",
                         width=25,
                         height=5,
                         bg="indianred",
                         command=openBorrow)
    buttonBorrow.place(x=360, y=400, width=250, height=100)


    buttonReturn = Button(loansMenu,
                          text = "Return",
                          width=25,
                          height=5,
                          bg="aquamarine",
                          command=openReturn)
    buttonReturn.place(x=960, y=400, width=250, height=100)

## Loans Borrow Page
def destroyLoansBorrowMenu():
    loansBorrowMenu.destroy()

def navFromLoansBorrowToLoans():
    loansMenuFunc()
    destroyLoansBorrowMenu()
    loansMenu.lift()
    loansMenu.lift()

def loansBorrowMenuFunc():
    global loansBorrowMenu
    loansBorrowMenu = Toplevel()
    loansBorrowMenu.title("Borrow a Book")
    loansBorrowMenu.geometry("1280x720")

    def borrowBook():
    	messagebox.showerror(
        	"Filler Error",
        	"Error: Function not complete yet!")

    def isBookBorrowed():
    	messagebox.showerror(
        	"Filler Error",
        	"Error: Function not complete yet!")

    def canMemberBorrow():
    	messagebox.showerror(
       		"Filler Error",
        	"Error: Function not complete yet!")

    topleftheader = Label(loansBorrowMenu,
    	text = "BT2102",
    	bg = "lightblue",
    	borderwidth = 2,
    	relief = "solid",
    	font = ("Mincho", 40))
    topleftheader.place(x = 0, y = 0, width = 280, height = 100)

    topbar = Label(loansBorrowMenu,
    	text = "ALS",
    	bg = "lightblue", 
    	borderwidth = 2,
    	relief = "ridge",
    	font = ("Mincho", 40))
    topbar.place(x = 280, y = 0, width = 1000, height = 100)

    sidebar = Label(loansBorrowMenu,
    	text = "Loans",
    	bg = "lightblue", 
    	borderwidth = 2,
    	relief = "ridge",
    	font = ("Mincho", 28))
    sidebar.place(x = 0, y = 100, width = 280, height = 620)   

    titleLabel = Label(loansBorrowMenu,
	    text="Book Borrowing",
	    bg="cornsilk",
	    font=("Mincho", 24))
    titleLabel.place(x=360, y=180)


    bookNumLabel = Label(loansBorrowMenu,
                         text="Please Insert Book Accession Number")
    bookNumLabel.place(x=460, y=300)


    bookNumEntry = Entry(loansBorrowMenu)
    bookNumEntry.place(x=760, y=300)

    memberIdLabel = Label(loansBorrowMenu,
                          text="Please Insert Member Id")
    memberIdLabel.place(x=460, y=400)


    memberIdEntry = Entry(loansBorrowMenu)
    memberIdEntry.place(x=760, y=400)

    borrowBookButton = Button(
        loansBorrowMenu,
        text="Borrow",
	width=8,
	height=2,
	command=borrowBook)
    borrowBookButton.place(x=660, y=500, width=250, height=100)

    homeButton = Button(
	loansBorrowMenu,
	text = "Home",
        width=5,
        height=2,
        bg="AntiqueWhite",
        command=goHome)
    homeButton.place(x=810, y=100, width=150, height=50)

    backButton = Button(loansBorrowMenu,
    	text = "Back",
    	width=10,
    	height=2,
    	bg="AntiqueWhite",
    	command=navFromLoansBorrowToLoans)
    backButton.place(x=560, y=100, width=150, height=50)



## Loans Return Page
def destroyLoansReturnMenu():
    loansReturnMenu.destroy()

def navFromLoansReturnToLoans():
    loansMenuFunc()
    destroyLoansReturnMenu()
    loansMenu.lift()
    loansMenu.lift()

def loansReturnMenuFunc():
    global loansReturnMenu
    loansReturnMenu = Toplevel()
    loansReturnMenu.title("Borrow a Book")
    loansReturnMenu.geometry("1280x720")

    def returnBook():
        messagebox.showerror(
            "Filler Error",
            "Error: Function not complete yet!")

    def isBookBorrowed():
        messagebox.showerror(
            "Filler Error",
            "Error: Function not complete yet!")

    def isBookReturnedOnTime():
        messagebox.showerror(
            "Filler Error",
            "Error: Function not complete yet!")

    topleftheader = Label(loansReturnMenu,
    	text = "BT2102",
    	bg = "lightblue",
    	borderwidth = 2,
    	relief = "solid",
    	font = ("Mincho", 40))
    topleftheader.place(x = 0, y = 0, width = 280, height = 100)

    topbar = Label(loansReturnMenu,
    	text = "ALS",
    	bg = "lightblue", 
    	borderwidth = 2,
    	relief = "ridge",
    	font = ("Mincho", 40))
    topbar.place(x = 280, y = 0, width = 1000, height = 100)

    sidebar = Label(loansReturnMenu,
    	text = "Loans",
    	bg = "lightblue", 
    	borderwidth = 2,
    	relief = "ridge",
    	font = ("Mincho", 28))
    sidebar.place(x = 0, y = 100, width = 280, height = 620)   

    titleLabel = Label(loansReturnMenu,
	    text="Book Returning",
	    bg="cornsilk",
	    font=("Mincho", 24))
    titleLabel.place(x=360, y=180)


    bookNumLabel = Label(loansReturnMenu,
                         text="Please Insert Book Accession Number")
    bookNumLabel.place(x=460, y=300)


    bookNumEntry = Entry(loansReturnMenu)
    bookNumEntry.place(x=760, y=300)

    returnBookButton = Button(
        loansReturnMenu,
        text="Confirm",
	width=8,
	height=2,
	command=returnBook)
    returnBookButton.place(x=660, y=500, width=250, height=100)

    homeButton = Button(loansReturnMenu,
	text = "Home",
        width=5,
        height=2,
        bg="AntiqueWhite",
        command=goHome)
    homeButton.place(x=810, y=100, width=150, height=50)

    backButton = Button(loansReturnMenu,
    	text = "Back",
    	width=10,
    	height=2,
    	bg="AntiqueWhite",
    	command=navFromLoansReturnToLoans)
    backButton.place(x=560, y=100, width=150, height=50)


## Dont delete - used to start the app
startButton = Button(window, text = "Start", command = loansMenuFunc, fg = "lightblue",
                     bg = "black", font = ("Mincho", 20))
startButton.pack()

window.mainloop()


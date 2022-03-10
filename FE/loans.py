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
    loansReturnMenu.lift()
    loansReturnMenu.lift()

def goHome():
    window.destroy()
    import landingPage

def loansMenuFunc():
    global loansMenu
    loansMenu = Toplevel()
    loansMenu.title("Loans Menu")
    loansMenu.geometry("1280x720")

    ## Information Header
    reportsLabel = Label(loansMenu,
                       text = "Select one of the Options below",
                       font =("calibre", 20, "bold"),
                       bg = "Slategray1")
    reportsLabel.place(x=0, y=0, width=1280, height=80);

    ##Loans Image Leftmost Label
    global loansIm
    loansIm = ImageTk.PhotoImage(Image.open("loansIm.jpg").resize((250,200)))
    displayLoansIm = Label(loansMenu,
                             image=loansIm);
    displayLoansText = Label(loansMenu,
                             text = "Loans",
                             font = ("calibre", 30, "italic", "bold"),
                             fg = "lavender",
                             bg = "black")
    displayLoansIm.place(x=40, y=160, width = 500, height = 500);
    displayLoansText.place(x=160, y=560, width = 250, height = 70);

    ##Book Borrow Button
    bookBorrowButton = Button(loansMenu,
        text = "Book Borrow",
        font = ("calibre", 30, "bold"),
        fg = "lavender blush",
        bg = "dodgerBlue2",
        command = openBorrow)

    bookBorrowButton.place(x=580, y=240, width=650, height=100)

    ##Book Return Button
    bookReturnButton = Button(loansMenu,
        text = "Book Return",
        font = ("calibre", 30, "bold"),
        fg = "lavender blush",
        bg = "dodgerBlue2",
        command = openReturn)

    bookReturnButton.place(x=580, y=360, width=650, height=100)
    
    ##Back Button
    backButton = Button(loansMenu,
        text = "Back",
        font = ("calibre", 15, "bold"),
        fg = "grey39",
        bg = "snow3",
        command = goHome)
    backButton.place(x=220, y=650, width=140, height=40)

############################################
## Loans 2 - Book Borrow 
############################################
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

    def closeBorrowDialog():
        loansBorrowMenu.lift()
        borrowConfirmDialog.destroy()

    ############################################
    ## Loans 2.1 - Borrow Confirmation 
    ############################################
    def borrowBook():
        global borrowConfirmDialog
        borrowConfirmDialog = Toplevel()
        borrowConfirmDialog.geometry("750x800")
        borrowConfirmDialog.configure(bg = "limegreen")

        def isBookBorrowed():
            return True

        def isLoanQuotaExceeded():
            return False

        def doesMemberHaveFine():
            return False


        def confirmBorrowBook():
            if isBookBorrowed():
                messagebox.showerror(
                    "Book Borrow Error",
                    "Error: Book currently on Loan until: {0}".format("DD/MM/YYYY"))
                closeBorrowDialog()
            else:
                if isLoanQuotaExceeded():
                    if doesMemberHaveFine():
                        messagebox.showerror(
                            "Book Borrow Error",
                            "Error: Member has outstanding fines")
                        closeBorrowDialog()
                    else:
                        ## Borrowing SQL call goes here
                        closeBorrowDialog()
                else:
                    messagebox.showerror(
                            "Book Borrow Error",
                            "Error: Member loan quota exceeded")
                    closeBorrowDialog()
 

        ## Information Header
        borrowConfirmTitleLabel = Label(borrowConfirmDialog,
                           text = "Confirm Loan Details",
                           font =("calibre", 32, "bold"),
                           bg = "LightSteelBlue2")
        borrowConfirmTitleLabel.place(x=0, y=0, width=750, height=100);

        ## Accession Number Field
        borrowConfirmAccInputLabel = Label(borrowConfirmDialog,
                                  text = "Accession Number: {0}"
                                           .format("Sample"),
                                  font = ("calibre", 15),
                                  bg = "SkyBlue2")
        borrowConfirmAccInputLabel.place(x=100, y=100, width=550, height=80)   

        ## Book Title Field
        borrowConfirmBookTitleLabel = Label(borrowConfirmDialog,
                                  text = "Book Title: {0}"
                                           .format("Sample"),
                                  font = ("calibre", 15),
                                  bg = "SkyBlue2")
        borrowConfirmBookTitleLabel.place(x=100, y=200, width=550, height=80)
                             
        ## MembershipId Field
        borrowMembershipIdLabel = Label(borrowConfirmDialog,
                                  text = "Membership ID: {0}"
                                           .format("Sample"),
                                  font = ("calibre", 15),
                                  bg = "SkyBlue2")
        borrowMembershipIdLabel.place(x=100, y=300, width=550, height=80)

        ## Member Name Field
        borrowMemberNameLabel = Label(borrowConfirmDialog,
                                  text = "Membership ID: {0}"
                                           .format("Sample"),
                                  font = ("calibre", 15),
                                  bg = "SkyBlue2")
        borrowMemberNameLabel.place(x=100, y=400, width=550, height=80)

        ## Borrow Due Date Field
        borrowDueDateLabel = Label(borrowConfirmDialog,
                                  text = "Return Date: {0}"
                                           .format("Sample"),
                                  font = ("calibre", 15),
                                  bg = "SkyBlue2")
        borrowDueDateLabel.place(x=100, y=500, width=550, height=80)


        ## Confirm Return Button
        borrowBookCloseButton = Button(borrowConfirmDialog,
            text = "Confirm\nReturn",
            font = ("Arial", 20, "bold"),
            fg = "ghost white",
            bg = "magenta2",
            command = confirmBorrowBook)
        borrowBookCloseButton.place(x=300, y=700, width=150, height=80)

    ## Information Header
    loansBorrowLabel = Label(loansBorrowMenu,
                       text = "To Borrow a Book, Please Enter Information Below",
                       font =("calibre", 20, "bold"),
                       bg = "LightSteelBlue2")
    loansBorrowLabel.place(x=0, y=0, width=1280, height=80);

    
    ## Book Accession Num Input Field
    loansBorrowAccNumLabel = Label(loansBorrowMenu,
                              text = "Book Accession Number",
                              font = ("calibre", 15),
                              bg = "powder blue")
    loansBorrowAccNumLabel.place(x=50, y=250, width=220, height=80)
    global loansBorrowAccNumEntry
    loansBorrowAccNumEntry = Entry(loansBorrowMenu,
                        font = ("calibre", 10, "italic"),
                        fg = "blue2")
    loansBorrowAccNumEntry.place(x=320, y=270, width=700, height=30)
    ## MembershipId Input Field
    loansBorrowMemberIdLabel = Label(loansBorrowMenu,
                              text = "MembershipId",
                              font = ("calibre", 15),
                              bg = "LightSkyBlue2")
    loansBorrowMemberIdLabel.place(x=50, y=400, width=220, height=80)
    global loansBorrowMemberIdEntry
    loansBorrowMemberIdEntry = Entry(loansBorrowMenu,
                        font = ("calibre", 10, "italic"),
                        fg = "blue2")
    loansBorrowMemberIdEntry.place(x=320, y=420, width=700, height=30)

    ## Book Borrow Button
    loansBorrowBookButton = Button(loansBorrowMenu,
        text = "Borrow",
        font = ("calibre", 10, "bold"),
        fg = "black",
        bg = "plum2",
        command = borrowBook)
    loansBorrowBookButton.place(x=360, y=670, width=150, height=40)

    ##Back Button
    backButton = Button(loansBorrowMenu,
        text = "Back",
        font = ("calibre", 15, "bold"),
        fg = "grey39",
        bg = "snow3",
        command = navFromLoansBorrowToLoans)
    backButton.place(x=860, y=670, width=150, height=40)




############################################
## Loans 3 - Book Returns 
############################################
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
    loansReturnMenu.title("Return a Book")
    loansReturnMenu.geometry("1280x720")

    def closeReturnDialog():
        loansReturnMenu.lift()
        returnConfirmDialog.destroy()

    ############################################
    ## Loans 3.1 - Return Confirmation 
    ############################################
    def returnBook():
        global returnConfirmDialog
        returnConfirmDialog = Toplevel()
        returnConfirmDialog.geometry("750x800")
        returnConfirmDialog.configure(bg = "limegreen")

        def isBookBorrowed():
            return True

        def isBookReturnedOnTime():
            return False

        def confirmReturnBook():
            if isBookBorrowed():
                if isBookReturnedOnTime():
                    closeReturnDialog()
                else:
                    messagebox.showwarning(
                        "Book Returned Late",
                        "Warning: Book returned late, fine credited to member!")
                    closeReturnDialog()
            else:
                messagebox.showerror(
                "Book Return Error",
                "Error: Book has not been borrowed")

        ## Information Header
        returnConfirmTitleLabel = Label(returnConfirmDialog,
                           text = "Confirm Return Details",
                           font =("calibre", 32, "bold"),
                           bg = "LightSteelBlue2")
        returnConfirmTitleLabel.place(x=0, y=0, width=750, height=100);

        ## Accession Number Field
        returnConfirmAccInputLabel = Label(returnConfirmDialog,
                                  text = "Accession Number: {0}"
                                           .format("Sample"),
                                  font = ("calibre", 15),
                                  bg = "SkyBlue2")
        returnConfirmAccInputLabel.place(x=100, y=100, width=550, height=80)   

        ## Book Title Field
        returnConfirmBookTitleLabel = Label(returnConfirmDialog,
                                  text = "Book Title: {0}"
                                           .format("Sample"),
                                  font = ("calibre", 15),
                                  bg = "SkyBlue2")
        returnConfirmBookTitleLabel.place(x=100, y=200, width=550, height=80)
                             
        ## MembershipId Field
        returnMembershipIdLabel = Label(returnConfirmDialog,
                                  text = "Membership ID: {0}"
                                           .format("Sample"),
                                  font = ("calibre", 15),
                                  bg = "SkyBlue2")
        returnMembershipIdLabel.place(x=100, y=300, width=550, height=80)

        ## Member Name Field
        returnMemberNameLabel = Label(returnConfirmDialog,
                                  text = "Membership ID: {0}"
                                           .format("Sample"),
                                  font = ("calibre", 15),
                                  bg = "SkyBlue2")
        returnMemberNameLabel.place(x=100, y=400, width=550, height=80)

        ## Return Date Field
        returnDateLabel = Label(returnConfirmDialog,
                                  text = "Return Date: {0}"
                                           .format("Sample"),
                                  font = ("calibre", 15),
                                  bg = "SkyBlue2")
        returnDateLabel.place(x=100, y=500, width=550, height=80)


        ## Confirm Return Button
        returnBookCloseButton = Button(returnConfirmDialog,
            text = "Confirm\nReturn",
            font = ("Arial", 20, "bold"),
            fg = "ghost white",
            bg = "magenta2",
            command = confirmReturnBook)
        returnBookCloseButton.place(x=300, y=700, width=150, height=80)

    ## Information Header
    loansReturnLabel = Label(loansReturnMenu,
                       text = "To Return a Book, Please Enter Information Below",
                       font =("calibre", 20, "bold"),
                       bg = "LightSteelBlue2")
    loansReturnLabel.place(x=0, y=0, width=1280, height=80);

    ## Book Accession Num Input Field
    loansReturnAccNumLabel = Label(loansReturnMenu,
                              text = "Book Accession Number",
                              font = ("calibre", 15),
                              bg = "powder blue")
    loansReturnAccNumLabel.place(x=50, y=250, width=220, height=80)

    global loansReturnAccNumEntry
    loansReturnAccNumEntry = Entry(loansReturnMenu,
                        font = ("calibre", 10, "italic"),
                        fg = "blue2")
    loansReturnAccNumEntry.place(x=320, y=270, width=700, height=30)

    ## Return Date Field
    loansReturnDateLabel = Label(loansReturnMenu,
                              text = "Return Date",
                              font = ("calibre", 15),
                              bg = "LightSkyBlue2")
    loansReturnDateLabel.place(x=50, y=400, width=220, height=80)

    global loansReturnDateEntry
    loansReturnDateEntry = Entry(loansReturnMenu,
                        font = ("calibre", 10, "italic"),
                        fg = "blue2")
    loansReturnDateEntry.place(x=320, y=420, width=700, height=30)

    ## Book Return Button
    returnBookButton = Button(loansReturnMenu,
        text = "Return",
        font = ("calibre", 10, "bold"),
        fg = "black",
        bg = "plum2",
        command = returnBook)
    returnBookButton.place(x=360, y=670, width=150, height=40)

    ## Back Button
    backButton = Button(loansReturnMenu,
        text = "Back",
        font = ("calibre", 15, "bold"),
        fg = "grey39",
        bg = "snow3",
        command = navFromLoansReturnToLoans)
    backButton.place(x=860, y=670, width=150, height=40)


## Dont delete - used to start the app
startButton = Button(window, text = "Start", command = loansMenuFunc, fg = "lightblue",
                     bg = "black", font = ("Mincho", 20))
startButton.pack()

window.mainloop()


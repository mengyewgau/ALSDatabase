from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image

window = Tk()


## Reports Landing Page
def destroyReportsMenu():
    reportsMenu.destroy()

def openBookSearch():
    bookSearchMenuFunc()
    destroyReportsMenu()
    bookSearchMenu.lift()
    bookSearchMenu.lift()

def openBooksOnLoan():
    booksOnLoanFunc()
    booksOnLoanMenu.lift()
    booksOnLoanMenu.lift()

def openBooksOnReserv():
    booksOnReservFunc()
    booksOnReservMenu.lift()
    booksOnReservMenu.lift()

def openOutstandingFines():
    outstandingFinesFunc()
    outstandingFinesMenu.lift()
    outstandingFinesMenu.lift()

def openBooksOnLoanToMember():
    booksOnLoanToMemberMenuFunc()
    destroyReportsMenu()
    booksOnLoanToMemberMenu.lift()
    booksOnLoanToMemberMenu.lift()

def goHome():
    window.destroy()
    import landingPage

def reportsMenuFunc():
    global reportsMenu
    reportsMenu = Toplevel()
    reportsMenu.title("Reports Menu")
    reportsMenu.geometry("1280x720")

    ## Information Header
    reportsLabel = Label(reportsMenu,
                       text = "Select one of the Options below",
                       font =("calibre", 20, "bold"),
                       bg = "Slategray1")
    reportsLabel.place(x=0, y=0, width=1280, height=80);

    ##Reports Image Leftmost Label
    global reportIm
    reportIm = ImageTk.PhotoImage(Image.open("booksIm.jpg").resize((250,200)))
    displayReportsIm = Label(reportsMenu,
                             image=reportIm);
    displayReportsText = Label(reportsMenu,
                             text = "Reports",
                             font = ("calibre", 30, "italic", "bold"),
                             fg = "lavender",
                             bg = "black")
    displayReportsIm.place(x=40, y=160, width = 500, height = 500);
    displayReportsText.place(x=160, y=560, width = 250, height = 70);

    ##Book Search Button
    bookSearchButton = Button(reportsMenu,
        text = "Book Search",
        font = ("calibre", 30, "bold"),
        fg = "lavender blush",
        bg = "dodgerBlue2",
        command = openBookSearch)

    bookSearchButton.place(x=580, y=120, width=650, height=100)

    ##Books on Loan Button
    booksOnLoanButton = Button(reportsMenu,
        text = "Books on Loan",
        font = ("calibre", 30, "bold"),
        fg = "lavender blush",
        bg = "dodgerBlue2",
        command = openBooksOnLoan)

    booksOnLoanButton.place(x=580, y=240, width=650, height=100)

    ##Books on Reservation Button
    booksOnReservButton = Button(reportsMenu,
        text = "Books on Reservation",
        font = ("calibre", 30, "bold"),
        fg = "lavender blush",
        bg = "dodgerBlue2",
        command = openBooksOnReserv)

    booksOnReservButton.place(x=580, y=360, width=650, height=100)

    ##Outstanding Fines Button
    outstandingFinesButton = Button(reportsMenu,
        text = "Outstanding Fines",
        font = ("calibre", 30, "bold"),
        fg = "lavender blush",
        bg = "dodgerBlue2",
        command = openOutstandingFines)

    outstandingFinesButton.place(x=580, y=480, width=650, height=100)

    ##Books on Loan to Member Button
    booksOnLoanToMemberButton = Button(reportsMenu,
        text = "Books on Loan to Member",
        font = ("calibre", 30, "bold"),
        fg = "lavender blush",
        bg = "dodgerBlue2",
        command = openBooksOnLoanToMember)

    booksOnLoanToMemberButton.place(x=580, y=600, width=650, height=100)

    ##Back Button
    buttonBack = Button(reportsMenu,
        text = "Back",
        font = ("calibre", 15, "bold"),
        fg = "grey39",
        bg = "snow3",
        command = goHome)
    buttonBack.place(x=220, y=650, width=140, height=40)

############################################
## Reports 2 - Books on Loan 
############################################

def booksOnLoanFunc():
    global booksOnLoanMenu
    booksOnLoanMenu = Toplevel()
    booksOnLoanMenu.title("Books on Loan")
    booksOnLoanMenu.geometry("1100x600")

    def closeBooksOnLoanMenu():
        reportsMenu.lift()
        booksOnLoanMenu.destroy()

    ## Information Header
    booksOnLoanLabel = Label(booksOnLoanMenu,
                       text = "Books on Loan Report",
                       font =("calibre", 20, "bold"),
                       bg = "Slategray1")
    booksOnLoanLabel.place(x=0, y=0, width=1100, height=80);

    ##Back Button
    buttonBack = Button(booksOnLoanMenu,
        text = "Back to Reports",
        font = ("calibre", 15, "bold"),
        fg = "grey39",
        bg = "snow3",
        command = closeBooksOnLoanMenu)
    buttonBack.place(x=480, y=500, width=180, height=40)

############################################
## Reports 3 - Books on Reserv 
############################################

def booksOnReservFunc():
    global booksOnReservMenu
    booksOnReservMenu = Toplevel()
    booksOnReservMenu.title("Books on Reservation")
    booksOnReservMenu.geometry("1100x600")

    def closeBooksOnReservMenu():
        reportsMenu.lift()
        booksOnReservMenu.destroy()

    ## Information Header
    booksOnLoanLabel = Label(booksOnReservMenu,
                       text = "Books on Reservation Report",
                       font =("calibre", 20, "bold"),
                       bg = "Slategray1")
    booksOnLoanLabel.place(x=0, y=0, width=1100, height=80);

    ##Back Button
    buttonBack = Button(booksOnReservMenu,
        text = "Back to Reports",
        font = ("calibre", 15, "bold"),
        fg = "grey39",
        bg = "snow3",
        command = closeBooksOnReservMenu)
    buttonBack.place(x=480, y=500, width=180, height=40)

############################################
## Reports 4 - Members with Outstanding Fines
############################################

def outstandingFinesFunc():
    global outstandingFinesMenu
    outstandingFinesMenu = Toplevel()
    outstandingFinesMenu.title("Members with Fines")
    outstandingFinesMenu.geometry("1100x600")

    def closeOutstandingFinesMenuMenu():
        reportsMenu.lift()
        outstandingFinesMenu.destroy()

    ## Information Header
    booksOnLoanLabel = Label(outstandingFinesMenu,
                       text = "Members with Outstanding Fines",
                       font =("calibre", 20, "bold"),
                       bg = "Slategray1")
    booksOnLoanLabel.place(x=0, y=0, width=1100, height=80);

    ##Back Button
    buttonBack = Button(outstandingFinesMenu,
        text = "Back to Reports",
        font = ("calibre", 15, "bold"),
        fg = "grey39",
        bg = "snow3",
        command = closeOutstandingFinesMenuMenu)
    buttonBack.place(x=480, y=500, width=180, height=40)

############################################
## Reports 1 - Book Search 
############################################
    ## TODO Implement the pop-up window + table for dynamic data
    
def destroyBookSearchMenu():
    bookSearchMenu.destroy()

def navFromBookSearchToReports():
    reportsMenuFunc()
    destroyBookSearchMenu()
    reportsMenu.lift()
    reportsMenu.lift()

def bookSearchMenuFunc():
    global bookSearchMenu
    bookSearchMenu = Toplevel()
    bookSearchMenu.title("Search a Book")
    bookSearchMenu.geometry("1280x720")

    def searchForBook():
        return
    
    ## Information Header
    bookSearchMenuLabel = Label(bookSearchMenu,
                       text = "Please Enter Requested Information Below",
                       font =("calibre", 20, "bold"),
                       bg = "LightSteelBlue2")
    bookSearchMenuLabel.place(x=0, y=0, width=1280, height=80);
                         

    ## Book Title Input Field
    bookSearchTitleLabel = Label(bookSearchMenu,
                              text = "Title",
                              font = ("calibre", 15),
                              bg = "LightSkyBlue2")
    bookSearchTitleLabel.place(x=50, y=150, width=200, height=80)

    global bookSearchTitleEntry
    bookSearchTitleEntry = Entry(bookSearchMenu,
                        font = ("calibre", 10, "italic"),
                        fg = "blue2")
    bookSearchTitleEntry.place(x=300, y=170, width=700, height=30)
                         
    ## Authors Input Field
    bookSearchAuthorInputLabel = Label(bookSearchMenu,
                              text = "Authors",
                              font = ("calibre", 15),
                              bg = "powder blue")
    bookSearchAuthorInputLabel.place(x=50, y=250, width=200, height=80)

    global bookSearchAuthorEntry
    bookSearchAuthorEntry = Entry(bookSearchMenu,
                        font = ("calibre", 10, "italic"),
                        fg = "blue2")
    bookSearchAuthorEntry.place(x=300, y=270, width=700, height=30)

    ## ISBN Input Field
    bookSearchISBNInputLabel = Label(bookSearchMenu,
                              text = "ISBN",
                              font = ("calibre", 15),
                              bg = "LightBlue1")
    bookSearchISBNInputLabel.place(x=50, y=350, width=200, height=80)

    global bookSearchISBNEntry
    bookSearchISBNEntry = Entry(bookSearchMenu,
                        font = ("calibre", 10, "italic"),
                        fg = "blue2")
    bookSearchISBNEntry.place(x=300, y=370, width=700, height=30)

    ## Publisher Input Field
    bookSearchPublisherInputLabel = Label(bookSearchMenu,
                              text = "Publisher",
                              font = ("calibre", 15),
                              bg = "LightCyan2")
    bookSearchPublisherInputLabel.place(x=50, y=450, width=200, height=80)

    global bookSearchPublisherEntry
    bookSearchPublisherEntry = Entry(bookSearchMenu,
                        font = ("calibre", 10, "italic"),
                        fg = "blue2")
    bookSearchPublisherEntry.place(x=300, y=470, width=700, height=30)

    ## Publication Year Input Field
    bookSearchPublicationYearInputLabel = Label(bookSearchMenu,
                              text = "Publication Year",
                              font = ("calibre", 15),
                              bg = "CadetBlue1")
    bookSearchPublicationYearInputLabel.place(x=50, y=550, width=200, height=80)

    global bookSearchPublicationYearEntry
    bookSearchPublicationYearEntry = Entry(bookSearchMenu,
                        font = ("calibre", 10, "italic"),
                        fg = "blue2")
    bookSearchPublicationYearEntry.place(x=300, y=570, width=700, height=30)

    ## Book Search Button
    bookSearchButton = Button(bookSearchMenu,
        text = "Search",
        font = ("calibre", 10, "bold"),
        fg = "black",
        bg = "plum2",
        command = searchForBook)
    bookSearchButton.place(x=360, y=670, width=150, height=40)

    ## Back Button
    bookSearchBackButton = Button(bookSearchMenu,
        text = "Back",
        font = ("calibre", 15, "bold"),
        fg = "grey39",
        bg = "snow3",
        command = navFromBookSearchToReports)

    bookSearchBackButton.place(x=860, y=670, width=150, height=40)

############################################
## Reports 5 - Books on Loan to Member
############################################
    ## TODO Implement the pop-up window + table for dynamic data
    
def destroyBooksOnLoanToMemberMenu():
    booksOnLoanToMemberMenu.destroy()

def navFromBooksOnLoanToMemberMenuToReports():
    reportsMenuFunc()
    destroyBooksOnLoanToMemberMenu()
    reportsMenu.lift()
    reportsMenu.lift()

def booksOnLoanToMemberMenuFunc():
    global booksOnLoanToMemberMenu
    booksOnLoanToMemberMenu = Toplevel()
    booksOnLoanToMemberMenu.title("Books on Loan to Member")
    booksOnLoanToMemberMenu.geometry("1280x720")

    def searchForBooksOnLoanToMember():
        return
    
    ## Information Header
    booksOnLoanToMemberLabel = Label(booksOnLoanToMemberMenu,
                                     text = "Books on Loan to Member",
                                     font =("calibre", 20, "bold"),
                                     bg = "LightSteelBlue2")
    booksOnLoanToMemberLabel.place(x=0, y=0, width=1280, height=80);
                         

    ## MembershipId Input Field
    booksOnLoanToMemberIdLabel = Label(booksOnLoanToMemberMenu,
                              text = "MembershipId",
                              font = ("calibre", 15),
                              bg = "LightSkyBlue2")
    booksOnLoanToMemberIdLabel.place(x=50, y=150, width=200, height=80)

    global booksOnLoanToMemberIdEntry
    booksOnLoanToMemberIdEntry = Entry(booksOnLoanToMemberMenu,
                        font = ("calibre", 10, "italic"),
                        fg = "blue2")
    booksOnLoanToMemberIdEntry.place(x=300, y=170, width=700, height=30)

    ## Member Search Button
    booksOnLoanToMemberSearchButton = Button(booksOnLoanToMemberMenu,
        text = "Search Member",
        font = ("Arial", 10, "bold"),
        fg = "black",
        bg = "plum2",
        command = searchForBooksOnLoanToMember)
    booksOnLoanToMemberSearchButton.place(x=360, y=670, width=150, height=40)

    ## Back Button
    booksOnLoanToMemberBackButton = Button(booksOnLoanToMemberMenu,
        text = "Back",
        font = ("calibre", 15, "bold"),
        fg = "grey39",
        bg = "snow3",
        command = navFromBooksOnLoanToMemberMenuToReports)

    booksOnLoanToMemberBackButton.place(x=860, y=670, width=150, height=40)


## Dont delete - used to start the app
startButton = Button(window, text = "Start", command = reportsMenuFunc, fg = "lightblue",
                     bg = "black", font = ("Mincho", 20))
startButton.pack()

window.mainloop()


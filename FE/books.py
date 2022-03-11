from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import backendSQL as sqlFuncs
from datetime import datetime

###################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################################
##Book Landing Window###########################################################

def destroyBookMenu():
    bookMenu.destroy()

def navFromBookToBookAcq():
    createBookAcquisition()
    destroyBookMenu()
    bookAcq.lift()
    bookAcq.lift()
	
def navFromBookToBookWith():
    createBookWithdrawal()
    destroyBookMenu()
    bookWith.lift()
    bookWith.lift()

def navFromBookToLP():
    landingPageFunc()
    destroyBookMenu()
    landingPage.lift()
    landingPage.lift()

def navFromConfirmAcqToBookAcq():
    acquisitionConfirmationDialog.destroy()
    bookAcq.lift()
    bookAcq.lift()
    
def createBookMenu():
    ##Book Page Background
    global bookMenu
    bookMenu = Toplevel()
    bookMenu.grab_set()
    bookMenu.geometry("1280x750");
    bookMenu.configure(bg="Slategray2")

    ##Book Page Header
    bookLabel = Label(bookMenu,
                         text = "Please select one of the following options:",
                         font=("calibre", 20, "bold"),
                         bg = "Slategray1")
    bookLabel.place(x=0,y=0, width=1280, height=80)

    ##Book Image Leftmost Label
    displayBookIm = Label(bookMenu,
                             image=memIm);
    displayBookText = Label(bookMenu,
                             text = "Books",
                             font = ("calibre", 30, "italic", "bold"),
                             fg = "lavender",
                             bg = "black")
    displayBookIm.place(x=40, y=160, width = 500, height = 500);
    displayBookText.place(x=160, y=560, width = 250, height = 70);

    ##Acquisition Button
    buttonAcquisition = Button(bookMenu,
        text = "Acquisition",
        font = ("calibre", 30, "bold"),
        fg = "lavender blush",
        bg = "dodgerBlue2",
        command = navFromBookToBookAcq)

    buttonAcquisition.place(x=580, y=250, width=650, height=100)

    ##Withdrawal Button
    buttonWithdrawal = Button(bookMenu,
        text = "Withdrawal",
        font = ("calibre", 30, "bold"),
        fg = "lavender blush",
        bg = "SteelBlue2",
        command = navFromBookToBookWith)

    buttonWithdrawal.place(x=580, y=450, width=650, height=100)

    ##Back Button
    buttonBack = Button(bookMenu,
        text = "Back",
        font = ("calibre", 15, "bold"),
        fg = "grey39",
        bg = "snow3",
        command = navFromBookToLP)

    buttonBack.place(x=1090, y=650, width=140, height=40)


################################################################################

## BOOK SUCCESS PAGES (BOTH ACQUISITION AND WITHDRAWAL) ###############################

def destroySuccessAcq():
    bookAcq.destroy()
    successAcq.destroy()
    createBookAcquisition()
    bookAcq.lift()
    bookAcq.lift()
    
def createSuccessAcq():
    global successAcq
    successAcq = Toplevel()
    successAcq.grab_set()
    successAcq.geometry("500x500")
    successAcq.configure(bg = "limegreen")

    ## Success Message
    createAcqSuccessLabel1 = Label(successAcq,           
                       text = "SUCCESS!",
                       font =("calibre", 40, "bold"),
                       bg = "green yellow",
                       fg = "black")
    createAcqSuccessLabel1.place(x=25, y=20, width=450, height=80);

    createAcqSucessLabel2 = Label(successAcq,           
                       text = "New Book added in Library",
                       font =("calibre", 25),
                       bg = "limegreen",
                       fg = "black")
    createAcqSucessLabel2.place(x=25, y=120, width=450, height=200);

    ## Success Back Button
    buttonAcqBack = Button(successAcq,
        text = "Back",
        font = ("calibre", 15, "bold"),
        fg = "grey39",
        bg = "snow3",
        command = destroySuccessAcq)

    buttonAcqBack.place(x=300, y=450, width=140, height=40)

def destroySuccessWith():
    bookWith.destroy()
    successWith.destroy()
    createBookWithdrawal()
    bookWith.lift()
    bookWith.lift()

def createSuccessWith():
    global successWith
    successWith = Toplevel()
    successWith.grab_set()
    successWith.geometry("500x500")
    successWith.configure(bg = "limegreen")

    ## Success Message
    createWithSuccessLabel1 = Label(successWith,           
                       text = "SUCCESS!",
                       font =("calibre", 40, "bold"),
                       bg = "green yellow",
                       fg = "black")
    createWithSuccessLabel1.place(x=25, y=20, width=450, height=80);

    createWithSuccessLabel2 = Label(successWith,           
                       text = "Book withdrawn from Library",
                       font =("calibre", 20, "bold"),
                       bg = "limegreen",
                       fg = "black")
    createWithSuccessLabel2.place(x=25, y=120, width=450, height=200);

    ## Success Back Button
    buttonWithBack = Button(successWith,
        text = "Back",
        font = ("calibre", 15, "bold"),
        fg = "grey39",
        bg = "snow3",
        command = destroySuccessWith)

    buttonWithBack.place(x=300, y=450, width=140, height=40)
    
################################################################################
    
## BOOK ACQUISITION PAGE #######################################################

def destroyBookAcquisition():
    bookAcq.destroy()

def navFromBookAcqToBook():
    createBookMenu()
    destroyBookAcquisition()
    bookMenu.lift()
    bookMenu.lift()

def navFromAcqConfirmationToSuccessPage():
    createSuccessAcq()
    acquisitionConfirmationDialog.destroy()
    successAcq.lift()
    successAcq.lift()

    ##Confirmation Page
def confirmAcqDialog():
    global acquisitionConfirmationDialog
    acquisitionConfirmationDialog = Toplevel()
    acquisitionConfirmationDialog.grab_set()
    acquisitionConfirmationDialog.geometry("720x800")
    acquisitionConfirmationDialog.configure(bg = "limegreen")

    accessionNum = str(accAcqEntry.get())
    title = str(bookTitleEntry.get())
    authorsStr = str(authorEntry.get())
    authors = tuple(str(authorEntry.get()).split(", "))
    isbn = str(ISBNEntry.get())
    publisher = str(publisherEntry.get())
    publicationYear = str(publicationYearEntry.get())

    def confirmBookAcq ():
        try:
            sqlFuncs.createBook(accessionNum, title, isbn, publisher, publicationYear)
            for a in authors:
                sqlFuncs.createBkAuthor(accessionNum,a)
            
            navFromAcqConfirmationToSuccessPage()   
                
            
        except:
            messagebox.showerror(
                "Book Acquisition Error",
                "Book already added;\nDuplicate, Missing or\nIncomplete fields.")
            
            
    ## Information Header
    confirmAcqHeader = Label(acquisitionConfirmationDialog,
                       text = "Please confirm the following details:",
                       font =("calibre", 20, "bold"),
                       bg = "pale green")
    confirmAcqHeader.place(x=0, y=0, width=800, height=90);

    ## Accession Number Confirmation
    confirmAccNum = Label(acquisitionConfirmationDialog,
                              text = "Accession Number: {0}"
                                  .format(accessionNum),
                              font = ("calibre", 15),
                              bg = "limegreen")
    confirmAccNum.place(x=0, y=100, width=750, height=80)                         

    ## Book Title Confirmation
    confirmBookTitle = Label(acquisitionConfirmationDialog,
                              text = "Title: {0}"
                               .format(title),
                              font = ("calibre", 15),
                              bg = "limegreen")
    confirmBookTitle.place(x=0, y=200, width=750, height=80)

                         
    ## Authors Input Confirmation
    confirmAuthor = Label(acquisitionConfirmationDialog,
                              text = "Authors: {0}"
                                 .format(authorsStr),
                              font = ("calibre", 15),
                              bg = "limegreen")
    confirmAuthor.place(x=0, y=300, width=750, height=80)

    ## ISBN Input Confirmation
    confirmISBN = Label(acquisitionConfirmationDialog,
                              text = "ISBN: {0}"
                                .format(isbn),
                              font = ("calibre", 15),
                              bg = "limegreen")
    confirmISBN.place(x=0, y=400, width=750, height=80)

    ## Publisher Input Field
    confirmPublisher = Label(acquisitionConfirmationDialog,
                              text = "Publisher: {0}"
                                 .format(publisher),
                              font = ("calibre", 15),
                              bg = "limegreen")
    confirmPublisher.place(x=0, y=500, width=750, height=80)

    ## Publication Year Input Field
    confirmPubYear = Label(acquisitionConfirmationDialog,
                              text = "Publication Year: {0}"
                               .format(publicationYear),
                              font = ("calibre", 15),
                              bg = "limegreen")
    confirmPubYear.place(x=0, y=600, width=750, height=80)


    ## Confirm Acquisition Button
    buttonConfirmAcq = Button(acquisitionConfirmationDialog,
        text = "Confirm New Book",
        font = ("Arial", 20, "bold"),
        borderwidth = 4,
        relief = "solid",           
        fg = "ghost white",
        bg = "DodgerBlue4",
        command = confirmBookAcq)
    buttonConfirmAcq.place(x=50, y=680, width=300, height=80)
    

    ## Back Button
    buttonAcqBack = Button(acquisitionConfirmationDialog,
        text = "Back",
        font = ("calibre", 15, "bold"),
        fg = "grey39",
        bg = "snow3",
        command = navFromConfirmAcqToBookAcq)

    buttonAcqBack.place(x=550, y=700, width=100, height=50)
            
    
def createBookAcquisition():
    global bookAcq
    bookAcq = Toplevel()
    bookAcq.grab_set()
    bookAcq.geometry("1280x750")
    bookAcq.configure(bg = "LightSteelBlue1")

    ## Information Header
    createAcqHeader = Label(bookAcq,
                       text = "Please fill in the information below for a new book acquisition",
                       font =("calibre", 20, "bold"),
                       bg = "LightSteelBlue2")
    createAcqHeader.place(x=0, y=0, width=1280, height=80);

    ## Accession Number Input Field
    accInputLabel = Label(bookAcq,
                              text = "Accession Number",
                              font = ("calibre", 15),
                              bg = "SkyBlue2")
    accInputLabel.place(x=50, y=100, width=200, height=80)

    global accAcqEntry
    accAcqEntry = Entry(bookAcq,
                        font = ("calibre", 10, "italic"),
                        fg = "blue2")

    accAcqEntry.place(x=300, y=120, width=700, height=30)
                         

    ## Book Title Input Field
    bookTitleLabel = Label(bookAcq,
                              text = "Title",
                              font = ("calibre", 15),
                              bg = "LightSkyBlue2")
    bookTitleLabel.place(x=50, y=200, width=200, height=80)

    global bookTitleEntry
    bookTitleEntry = Entry(bookAcq,
                        font = ("calibre", 10, "italic"),
                        fg = "blue2")
    bookTitleEntry.place(x=300, y=220, width=700, height=30)
                         
    ## Authors Input Field
    authorInputLabel = Label(bookAcq,
                              text = "Authors",
                              font = ("calibre", 15),
                              bg = "powder blue")
    authorInputLabel.place(x=50, y=300, width=200, height=80)

    global authorEntry
    authorEntry = Entry(bookAcq,
                        font = ("calibre", 10, "italic"),
                        fg = "blue2")
    authorEntry.place(x=300, y=320, width=700, height=30)

    ## ISBN Input Field
    ISBNInputLabel = Label(bookAcq,
                              text = "ISBN",
                              font = ("calibre", 15),
                              bg = "LightBlue1")
    ISBNInputLabel.place(x=50, y=400, width=200, height=80)

    global ISBNEntry
    ISBNEntry = Entry(bookAcq,
                        font = ("calibre", 10, "italic"),
                        fg = "blue2")
    ISBNEntry.place(x=300, y=420, width=700, height=30)

    ## Publisher Input Field
    publisherInputLabel = Label(bookAcq,
                              text = "Publisher",
                              font = ("calibre", 15),
                              bg = "LightCyan2")
    publisherInputLabel.place(x=50, y=500, width=200, height=80)

    global publisherEntry
    publisherEntry = Entry(bookAcq,
                        font = ("calibre", 10, "italic"),
                        fg = "blue2")
    publisherEntry.place(x=300, y=520, width=700, height=30)

    ## Publication Year Input Field
    publicationYearInputLabel = Label(bookAcq,
                              text = "Publication Year",
                              font = ("calibre", 15),
                              bg = "CadetBlue1")
    publicationYearInputLabel.place(x=50, y=600, width=200, height=80)

    global publicationYearEntry
    publicationYearEntry = Entry(bookAcq,
                        font = ("calibre", 10, "italic"),
                        fg = "blue2")
    publicationYearEntry.place(x=300, y=620, width=700, height=30)

    ## Acquisition Submit Button
    buttonSubmitAcq = Button(bookAcq,
        text = "Submit\nNew\nBook",
        font = ("Arial", 20, "bold"),
        borderwidth = 4,
        relief = "solid",
        fg = "ghost white",
        bg = "DeepSkyBlue4",
        command = confirmAcqDialog)
    buttonSubmitAcq.place(x=1040, y=150, width=210, height=400)
    

    ## Back Button
    buttonAcqBack = Button(bookAcq,
        text = "Back",
        font = ("calibre", 15, "bold"),
        fg = "grey39",
        bg = "snow3",
        command = navFromBookAcqToBook)

    buttonAcqBack.place(x=1100, y=600, width=140, height=40)

################################################################################    

## WITHDRAWAL PAGE #############################################################

def destroyBookWithdrawal():
    bookWith.destroy()

def navFromWithConfirmationToSuccessPage():
    createSuccessWith()
    confirmWithDialog.destroy()
    successWith.lift()
    successWith.lift()

def navFromConfirmWithToBookWith():
    confirmWithDialog.destroy()
    
def confirmWithDialog():

    try:
        withBookDetails = sqlFuncs.confirmWithdrawal(str(accWithEntry.get()))
        accessionNum = withBookDetails[0]
        title = withBookDetails[1]
        authorsStr = withBookDetails[2]
        isbn = withBookDetails[3]
        publisher = withBookDetails[4]
        publicationYear = withBookDetails[5]
        
        global confirmWithDialog
        confirmWithDialog = Toplevel()
        confirmWithDialog.geometry("750x800")
        confirmWithDialog.configure(bg = "limegreen")
    except:
        messagebox.showerror(
                    "Book Withdrawal Error",
                    "This Book Accession Number Does Not Exist.")

    def confirmBookWith():
        try:
            sqlFuncs.withdrawBook(accessionNum)            
            navFromWithConfirmationToSuccessPage()   
                 
        except Exception as excp:
            if excp.args[0] == "Books is on Loan":
                messagebox.showerror(
                    "Book Withdrawal Error",
                    "Book is currently on Loan.")
            elif excp.args[0] == "Book has reservations":
                messagebox.showerror(
                    "Book Withdrawal Error",
                    "Book is currently Reserved.")
            confirmWithDialog.destroy()
            
            
    ## Information Header
    confirmWithHeader = Label(confirmWithDialog,
                       text = "Please confirm the following details:",
                       font =("calibre", 20, "bold"),
                       bg = "pale green")
    confirmWithHeader.place(x=0, y=0, width=800, height=90);

    ## Accession Number Confirmation
    confirmWithNum = Label(confirmWithDialog,
                              text = "Accession Number: {0}"
                                  .format(accessionNum),
                              font = ("calibre", 15),
                              bg = "limegreen")
    confirmWithNum.place(x=0, y=100, width=750, height=80)                         

    ## Book Title Confirmation
    confirmBookTitle = Label(confirmWithDialog,
                              text = "Title: {0}"
                               .format(title),
                              font = ("calibre", 15),
                              bg = "limegreen")
    confirmBookTitle.place(x=0, y=200, width=750, height=80)

                         
    ## Authors Input Confirmation
    confirmAuthor = Label(confirmWithDialog,
                              text = "Authors: {0}"
                                 .format(authorsStr),
                              font = ("calibre", 15),
                              bg = "limegreen")
    confirmAuthor.place(x=0, y=300, width=750, height=80)

    ## ISBN Input Confirmation
    confirmISBN = Label(confirmWithDialog,
                              text = "ISBN: {0}"
                                .format(isbn),
                              font = ("calibre", 15),
                              bg = "limegreen")
    confirmISBN.place(x=0, y=400, width=750, height=80)

    ## Publisher Input Field
    confirmPublisher = Label(confirmWithDialog,
                              text = "Publisher: {0}"
                                 .format(publisher),
                              font = ("calibre", 15),
                              bg = "limegreen")
    confirmPublisher.place(x=0, y=500, width=750, height=80)

    ## Publication Year Input Field
    confirmPubYear = Label(confirmWithDialog,
                              text = "Publication Year: {0}"
                               .format(publicationYear),
                              font = ("calibre", 15),
                              bg = "limegreen")
    confirmPubYear.place(x=0, y=600, width=750, height=80)


    ## Confirm Withdrawal Button
    buttonConfirmWith = Button(confirmWithDialog,
        text = "Confirm Withdrawal",
        font = ("Arial", 20, "bold"),
        borderwidth = 4,
        relief = "solid",           
        fg = "ghost white",
        bg = "DodgerBlue4",
        command = confirmBookWith)
    buttonConfirmWith.place(x=50, y=680, width=300, height=80)
    

    ## Back Button
    buttonWithBack = Button(confirmWithDialog,
        text = "Back",
        font = ("calibre", 15, "bold"),
        fg = "grey39",
        bg = "snow3",
        command = navFromConfirmWithToBookWith)

    buttonWithBack.place(x=550, y=700, width=100, height=50)

def navFromBookWithToBook():
    createBookMenu()
    destroyBookWithdrawal()
    bookMenu.lift()
    bookMenu.lift()

def createBookWithdrawal():
    global bookWith
    bookWith = Toplevel()
    bookWith.grab_set()
    bookWith.geometry("1280x750")
    bookWith.configure(bg = "azure2")

    ## Information Header
    createWithHeader = Label(bookWith,
                       text = "To Remove Outdated Books From System, Please Enter Required Information Below:",
                       font =("calibre", 20, "bold"),
                       bg = "azure3")
    createWithHeader.place(x=0, y=0, width=1280, height=80);

    ## Accession Number Input Field
    accInputLabel = Label(bookWith,
                              text = "Accession Number",
                              font = ("calibre", 15),
                              bg = "SkyBlue2")
    accInputLabel.place(x=100, y=150, width=300, height=100)

    global accWithEntry
    accWithEntry = Entry(bookWith,
                        font = ("calibre", 10, "italic"),
                        fg = "blue2")

    accWithEntry.place(x=490, y=180, width=700, height=30)

    ## Withdraw Submit Button
    buttonSubmitWith = Button(bookWith,
        text = "Withdraw Book",
        font = ("Arial", 30, "bold"),
        borderwidth = 4,
        relief = "solid",                      
        fg = "ghost white",
        bg = "DeepSkyBlue4",
        command = confirmWithDialog)
    buttonSubmitWith.place(x=460, y=450, width=400, height=100)

    ## Back Button
    buttonWithBack = Button(bookWith,
        text = "Back",
        font = ("calibre", 15, "bold"),
        fg = "grey39",
        bg = "snow3",
        command = navFromBookWithToBook)

    buttonWithBack.place(x=1100, y=600, width=140, height=40)
################################################################################

## LANDING PAGE ################################################################

def destroyLandingPage():
    landingPage.destroy()

def navFromLpToBooks(): #navigate from LP to Books
    createBookMenu()
    destroyLandingPage()
    bookMenu.lift()
    bookMenu.lift()

def landingPageFunc():
    global landingPage
    landingPage = Toplevel()
    landingPage.title("Landing Page")
    landingPage.geometry("1280x820")

    ##EMPTY FUNCTION
    def empty():
        global emptyPage
        emptyPage = Toplevel()
        emptyPage.geometry("1280x820")
        emptyPageLabel = Label(emptyPage,
                                 text = "Under Construction",
                                 font=("Arial, 20"),
                                 borderwidth = 4,
                                 relief = "solid",
                                 bg="paleturquoise1");
        emptyPageLabel.place(x=140, y=0, width=1000, height=200)

    ## (ALS) title centred in the screen
    titleLabel = Label(landingPage,
                          text = "(ALS)",
                          font=("calibre, 40"),
                          bg="white")
    titleLabel.place(x=0,y=20, width=1280, height=100)

    ## First row, leftmost button and icon
    global memIm
    memIm = ImageTk.PhotoImage(Image.open("membersIm.jpg").resize((250,200)))
    displayMemIm = Label(landingPage, image=memIm);
    displayMemIm.place(x=200, y=120, width=250, height=200);

    buttonMember = Button(landingPage,
                             text = "Membership",
                             font=("Arial, 18"),
                             bg="indianred",
                             command=empty)
    buttonMember.place(x=200, y=325, width=250, height=50)

    ## First row, middle button and icon
    global bookIm
    bookIm = ImageTk.PhotoImage(Image.open("booksIm.jpg").resize((250,200)))
    displayBkIm = Label(landingPage, image=bookIm);
    displayBkIm.place(x=515, y=120, width=250, height=200);

    buttonBooks = Button(landingPage,
                            text = "Books",
                            font=("Arial, 18"),
                            bg="aquamarine",
                            command=navFromLpToBooks)
    buttonBooks.place(x=515, y=325, width=250, height=50)


    ## First row, rightmost button and icon
    global loanIm
    loanIm = ImageTk.PhotoImage(Image.open("loansIm.jpg").resize((250,200)))
    displayLoanIm = Label(landingPage, image=loanIm);
    displayLoanIm.place(x=830, y=120, width=250, height=200);

    buttonLoans = Button(landingPage,
                            text = "Loans",
                            font=("Arial, 18"),
                            bg="darksalmon",
                            command=empty)
    buttonLoans.place(x=830, y=325, width=250, height=50)

    ## Second row, leftmost button and icon
    global reserveIm
    reserveIm = ImageTk.PhotoImage(Image.open("reserveIm.jpg").resize((250,200)))
    displayResIm = Label(landingPage, image=reserveIm);
    displayResIm.place(x=200, y=410, width=250, height=200);

    buttonReservation = Button(landingPage,
                                  text = "Reservation",
                                  font=("Arial, 18"),
                                  bg="darkseagreen")
    buttonReservation.place(x=200, y=615, width=250, height=50)

    ## Second row, middle button and icon
    global fineIm
    fineIm = ImageTk.PhotoImage(Image.open("fineIm.jpg").resize((250,200)))
    displayFineIm = Label(landingPage, image=fineIm);
    displayFineIm.place(x=515, y=410, width=250, height=200);

    buttonFines = Button(landingPage,
                            text = "Fines",
                            font=("Arial, 18"),
                            bg="cadetblue")
    buttonFines.place(x=515, y=615, width=250, height=50)


    ## Second row, rightmost button and icon
    global reportIm
    reportIm = ImageTk.PhotoImage(Image.open("reportIm.jpg").resize((250,200)))
    displayReportIm = Label(landingPage, image=reportIm);
    displayReportIm.place(x=830, y=410, width=250, height=200);

    buttonReports = Button(landingPage,
                              text = "Reports",
                              font=("Arial, 18"),
                              bg="peru")
    buttonReports.place(x=830, y=615, width=250, height=50)

################################################################################


def openMain():
	landingPageFunc()
	
window = Tk()

window.configure(bg="white")
startButton = Button(window, text = "Start", command = openMain, fg = "lightblue",
		bg = "black", font = ("Mincho", 20))

startButton.pack()

window.mainloop()

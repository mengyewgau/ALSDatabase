import tkinter as tk
from PIL import ImageTk, Image

##Book Landing Window###########################################################

def destroyBookMenu():
    bookMenu.destroy()
    
def createBookMenu():
    ##Book Page Background
    global bookMenu
    bookMenu = tk.Toplevel()
    bookMenu.geometry("1280x750");
    bookMenu.configure(bg="Slategray2")

    ##Book Page Header
    bookLabel = tk.Label(bookMenu,
                         text = "Please select one of the following options:",
                         font=("calibre", 20, "bold"),
                         bg = "Slategray1")
    bookLabel.place(x=0,y=0, width=1280, height=80)

    ##Book Image Leftmost Label
    displayBookIm = tk.Label(bookMenu,
                             image=memIm);
    displayBookText = tk.Label(bookMenu,
                             text = "Books",
                             font = ("calibre", 30, "italic", "bold"),
                             fg = "lavender",
                             bg = "black")
    displayBookIm.place(x=40, y=160, width = 500, height = 500);
    displayBookText.place(x=160, y=560, width = 250, height = 70);

    ##Acquisition Button
    buttonAcquisition = tk.Button(bookMenu,
        text = "Acquisition",
        font = ("calibre", 30, "bold"),
        fg = "lavender blush",
        bg = "dodgerBlue2",
        command = createBookAcquisition)

    buttonAcquisition.place(x=580, y=250, width=650, height=100)

    ##Withdrawal Button
    buttonWithdrawal = tk.Button(bookMenu,
        text = "Withdrawal",
        font = ("calibre", 30, "bold"),
        fg = "lavender blush",
        bg = "SteelBlue2",
        command = createBookWithdrawal)

    buttonWithdrawal.place(x=580, y=450, width=650, height=100)

    ##Back Button
    buttonBack = tk.Button(bookMenu,
        text = "Back",
        font = ("calibre", 15, "bold"),
        fg = "grey39",
        bg = "snow3",
        command = destroyBookMenu)

    buttonBack.place(x=1090, y=650, width=140, height=40)

################################################################################

## BOOK ERRORS/SUCCESS (BOTH ACQUISITION AND WITHDRAWAL) ###############################

#### To be added: Error for books that have already been added (Need to connect to mySQL)

def destroyAcqError():
    acqError.destroy()
    
def createAcqError():
    global acqError
    acqError = tk.Toplevel()
    acqError.geometry("500x500")
    acqError.configure(bg = "firebrick1")

    ## Error Message
    createAcqErrorLabel1 = tk.Label(acqError,           
                       text = "ERROR!",
                       font =("calibre", 40, "bold"),
                       bg = "firebrick4",
                       fg = "gold")
    createAcqErrorLabel1.place(x=25, y=20, width=450, height=80);

    createAcqErrorLabel2 = tk.Label(acqError,           
                       text = "Book Already Added;\nDuplicate, Missing or\nIncomplete fields.",
                       font =("calibre", 20, "bold"),
                       bg = "firebrick1",
                       fg = "yellow")
    createAcqErrorLabel2.place(x=25, y=120, width=450, height=200);

    ## Error Back Button
    buttonAcqBack = tk.Button(acqError,
        text = "Back",
        font = ("calibre", 15, "bold"),
        fg = "grey39",
        bg = "snow3",
        command = destroyAcqError)

    buttonAcqBack.place(x=300, y=450, width=140, height=40)

def destroySuccessAcq():
    successAcq.destroy()
    
def createSuccessAcq():
    global successAcq
    successAcq = tk.Toplevel()
    successAcq.geometry("500x500")
    successAcq.configure(bg = "limegreen")

    ## Success Message
    createAcqSuccessLabel1 = tk.Label(successAcq,           
                       text = "SUCCESS!",
                       font =("calibre", 40, "bold"),
                       bg = "green yellow",
                       fg = "black")
    createAcqSuccessLabel1.place(x=25, y=20, width=450, height=80);

    createAcqSucessLabel2 = tk.Label(successAcq,           
                       text = "New Book added in Library",
                       font =("calibre", 20, "bold"),
                       bg = "limegreen",
                       fg = "black")
    createAcqSucessLabel2.place(x=25, y=120, width=450, height=200);

    ## Success Back Button
    buttonAcqBack = tk.Button(successAcq,
        text = "Back",
        font = ("calibre", 15, "bold"),
        fg = "grey39",
        bg = "snow3",
        command = destroySuccessAcq)

    buttonAcqBack.place(x=300, y=450, width=140, height=40)

def destroySuccessWith():
    successWith.destroy()

def createSuccessWith():
    global successWith
    successWith = tk.Toplevel()
    successWith.geometry("500x500")
    successWith.configure(bg = "limegreen")

    ## Success Message
    createWithSuccessLabel1 = tk.Label(successWith,           
                       text = "SUCCESS!",
                       font =("calibre", 40, "bold"),
                       bg = "green yellow",
                       fg = "black")
    createWithSuccessLabel1.place(x=25, y=20, width=450, height=80);

    createWithSuccessLabel2 = tk.Label(successWith,           
                       text = "Book withdrawn from Library",
                       font =("calibre", 20, "bold"),
                       bg = "limegreen",
                       fg = "black")
    createWithSuccessLabel2.place(x=25, y=120, width=450, height=200);

    ## Success Back Button
    buttonWithBack = tk.Button(successWith,
        text = "Back",
        font = ("calibre", 15, "bold"),
        fg = "grey39",
        bg = "snow3",
        command = destroySuccessWith)

    buttonWithBack.place(x=300, y=450, width=140, height=40)
    
################################################################################
    
## BOOK ACQUISITION PAGE #######################################################

#### To be added: For submitAcq, need to insert data into mySQL
####              Errors for BookWithdrawal need to be done

def destroyBookAcquisition():
    bookAcq.destroy()

def submitAcq():
    accessionNum = str(accAcqEntry.get())
    title = str(bookTitleEntry.get())
    authors = tuple(str(authorEntry.get()).split(", "))
    isbn = str(ISBNEntry.get())
    publisher = str(publisherEntry.get())
    publicationYear = str(publicationYearEntry.get())

    if len(accessionNum) == 0 or len(title) == 0 or len(authors) == 0 or len(isbn) == 0 or len(publisher) == 0 or len(publicationYear) == 0:
        createAcqError()
    else:
        createSuccessAcq()
    
def createBookAcquisition():
    global bookAcq
    bookAcq = tk.Toplevel()
    bookAcq.geometry("1280x750")
    bookAcq.configure(bg = "LightSteelBlue1")

    ## Information Header
    createAcqHeader = tk.Label(bookAcq,
                       text = "Please fill in the information below for a new book acquisition",
                       font =("calibre", 20, "bold"),
                       bg = "LightSteelBlue2")
    createAcqHeader.place(x=0, y=0, width=1280, height=80);

    ## Accession Number Input Field
    accInputLabel = tk.Label(bookAcq,
                              text = "Accession Number",
                              font = ("calibre", 15),
                              bg = "SkyBlue2")
    accInputLabel.place(x=50, y=100, width=200, height=80)

    global accAcqEntry
    accAcqEntry = tk.Entry(bookAcq,
                        font = ("calibre", 10, "italic"),
                        fg = "blue2")

    accAcqEntry.place(x=300, y=120, width=700, height=30)
                         

    ## Book Title Input Field
    bookTitleLabel = tk.Label(bookAcq,
                              text = "Title",
                              font = ("calibre", 15),
                              bg = "LightSkyBlue2")
    bookTitleLabel.place(x=50, y=200, width=200, height=80)

    global bookTitleEntry
    bookTitleEntry = tk.Entry(bookAcq,
                        font = ("calibre", 10, "italic"),
                        fg = "blue2")
    bookTitleEntry.place(x=300, y=220, width=700, height=30)
                         
    ## Authors Input Field
    authorInputLabel = tk.Label(bookAcq,
                              text = "Authors",
                              font = ("calibre", 15),
                              bg = "powder blue")
    authorInputLabel.place(x=50, y=300, width=200, height=80)

    global authorEntry
    authorEntry = tk.Entry(bookAcq,
                        font = ("calibre", 10, "italic"),
                        fg = "blue2")
    authorEntry.place(x=300, y=320, width=700, height=30)

    ## ISBN Input Field
    ISBNInputLabel = tk.Label(bookAcq,
                              text = "ISBN",
                              font = ("calibre", 15),
                              bg = "LightBlue1")
    ISBNInputLabel.place(x=50, y=400, width=200, height=80)

    global ISBNEntry
    ISBNEntry = tk.Entry(bookAcq,
                        font = ("calibre", 10, "italic"),
                        fg = "blue2")
    ISBNEntry.place(x=300, y=420, width=700, height=30)

    ## Publisher Input Field
    publisherInputLabel = tk.Label(bookAcq,
                              text = "Publisher",
                              font = ("calibre", 15),
                              bg = "LightCyan2")
    publisherInputLabel.place(x=50, y=500, width=200, height=80)

    global publisherEntry
    publisherEntry = tk.Entry(bookAcq,
                        font = ("calibre", 10, "italic"),
                        fg = "blue2")
    publisherEntry.place(x=300, y=520, width=700, height=30)

    ## Publication Year Input Field
    publicationYearInputLabel = tk.Label(bookAcq,
                              text = "Publication Year",
                              font = ("calibre", 15),
                              bg = "CadetBlue1")
    publicationYearInputLabel.place(x=50, y=600, width=200, height=80)

    global publicationYearEntry
    publicationYearEntry = tk.Entry(bookAcq,
                        font = ("calibre", 10, "italic"),
                        fg = "blue2")
    publicationYearEntry.place(x=300, y=620, width=700, height=30)

    ## Acquisition Submit Button
    buttonSubmitAcq = tk.Button(bookAcq,
        text = "Submit\nNew\nBook",
        font = ("Arial", 20, "bold"),
        fg = "ghost white",
        bg = "magenta2",
        command = submitAcq)
    buttonSubmitAcq.place(x=1040, y=150, width=210, height=400)
    

    ## Back Button
    buttonAcqBack = tk.Button(bookAcq,
        text = "Back",
        font = ("calibre", 15, "bold"),
        fg = "grey39",
        bg = "snow3",
        command = destroyBookAcquisition)

    buttonAcqBack.place(x=1100, y=600, width=140, height=40)

################################################################################    

## WITHDRAWAL PAGE #############################################################
#### TO BE ADDED: CONFIRMATION OF DETAILS (confirmWith(), submitWith())

def destroyBookWithdrawal():
    bookWith.destroy()

def confirmWith():
    createSuccessWith()
    #TO BE EDITED

def destroySubmitWith():
    submitWith.destroy()
    
def submitWith():
    global submitWith
    submitWith = tk.Toplevel()
    submitWith.geometry("500x400")
    submitWith.configure(bg = "honeydew3")

    ## Information Header
    submitWithHeader = tk.Label(submitWith,
                       text = "Please Confirm Details\nto Be Correct:",
                       font =("calibre", 20, "bold"),
                       bg = "honeydew3")
    submitWithHeader.place(x=0, y=0, width=500, height=80);

    ## Withdraw Submit Button
    buttonConfirmWith = tk.Button(submitWith,
        text = "Withdraw Book",
        font = ("Arial", 10, "bold"),
        fg = "black",
        bg = "plum2",
        command = confirmWith)
    buttonConfirmWith.place(x=80, y=350, width=150, height=40)

    ## Back Button
    buttonWithBack = tk.Button(submitWith,
        text = "Back",
        font = ("calibre", 15, "bold"),
        fg = "grey39",
        bg = "snow3",
        command = destroySubmitWith)

    buttonWithBack.place(x=280, y=350, width=150, height=40)
    
def createBookWithdrawal():
    global bookWith
    bookWith = tk.Toplevel()
    bookWith.geometry("1280x750")
    bookWith.configure(bg = "azure2")

    ## Information Header
    createWithHeader = tk.Label(bookWith,
                       text = "To Remove Outdated Books From System, Please Enter Required Information Below:",
                       font =("calibre", 20, "bold"),
                       bg = "azure3")
    createWithHeader.place(x=0, y=0, width=1280, height=80);

    ## Accession Number Input Field
    accInputLabel = tk.Label(bookWith,
                              text = "Accession Number",
                              font = ("calibre", 15),
                              bg = "SkyBlue2")
    accInputLabel.place(x=200, y=100, width=200, height=80)

    global accWithEntry
    accWithEntry = tk.Entry(bookWith,
                        font = ("calibre", 10, "italic"),
                        fg = "blue2")

    accWithEntry.place(x=500, y=120, width=700, height=30)

    ## Withdraw Submit Button
    buttonSubmitWith = tk.Button(bookWith,
        text = "Withdraw Book",
        font = ("Arial", 30, "bold"),
        fg = "ghost white",
        bg = "magenta2",
        command = submitWith)
    buttonSubmitWith.place(x=500, y=300, width=300, height=100)

    ## Back Button
    buttonWithBack = tk.Button(bookWith,
        text = "Back",
        font = ("calibre", 15, "bold"),
        fg = "grey39",
        bg = "snow3",
        command = destroyBookWithdrawal)

    buttonWithBack.place(x=1100, y=600, width=140, height=40)
################################################################################

## LANDING PAGE ################################################################

window = tk.Tk()
window.geometry("1280x750");
window.configure(bg="white")

##EMPTY FUNCTION
def empty():
    global emptyPage
    emptyPage = tk.Toplevel()
    emptyPage.geometry("1280x820")
    emptyPageLabel = tk.Label(emptyPage,
                             text = "Under Construction",
                             font=("Arial, 20"),
                             borderwidth = 4,
                             relief = "solid",
                             bg="paleturquoise1");
    emptyPageLabel.place(x=140, y=0, width=1000, height=200)

## (ALS) title centred in the screen
titleLabel = tk.Label(window,
                      text = "(ALS)",
                      font=("calibre, 40"),
                      bg="white")
titleLabel.place(x=0,y=20, width=1280, height=100)

## First row, leftmost button and icon
global memIm
memIm = ImageTk.PhotoImage(Image.open("membersIm.jpg").resize((250,200)))
displayMemIm = tk.Label(window, image=memIm);
displayMemIm.place(x=200, y=120, width=250, height=200);

buttonMember = tk.Button(window,
                         text = "Membership",
                         font=("Arial, 18"),
                         bg="indianred",
                         command=empty)
buttonMember.place(x=200, y=325, width=250, height=50)

## First row, middle button and icon
global bookIm
bookIm = ImageTk.PhotoImage(Image.open("booksIm.jpg").resize((250,200)))
displayBkIm = tk.Label(window, image=bookIm);
displayBkIm.place(x=515, y=120, width=250, height=200);

buttonBooks = tk.Button(window,
                        text = "Books",
                        font=("Arial, 18"),
                        bg="aquamarine",
                        command=createBookMenu)
buttonBooks.place(x=515, y=325, width=250, height=50)


## First row, rightmost button and icon
global loanIm
loanIm = ImageTk.PhotoImage(Image.open("loansIm.jpg").resize((250,200)))
displayLoanIm = tk.Label(window, image=loanIm);
displayLoanIm.place(x=830, y=120, width=250, height=200);

buttonLoans = tk.Button(window,
                        text = "Loans",
                        font=("Arial, 18"),
                        bg="darksalmon",
                        command=empty)
buttonLoans.place(x=830, y=325, width=250, height=50)

## Second row, leftmost button and icon
global reserveIm
reserveIm = ImageTk.PhotoImage(Image.open("reserveIm.jpg").resize((250,200)))
displayResIm = tk.Label(window, image=reserveIm);
displayResIm.place(x=200, y=410, width=250, height=200);

buttonReservation = tk.Button(window,
                              text = "Reservation",
                              font=("Arial, 18"),
                              bg="darkseagreen")
buttonReservation.place(x=200, y=615, width=250, height=50)

## Second row, middle button and icon
global fineIm
fineIm = ImageTk.PhotoImage(Image.open("fineIm.jpg").resize((250,200)))
displayFineIm = tk.Label(window, image=fineIm);
displayFineIm.place(x=515, y=410, width=250, height=200);

buttonFines = tk.Button(window,
                        text = "Fines",
                        font=("Arial, 18"),
                        bg="cadetblue")
buttonFines.place(x=515, y=615, width=250, height=50)


## Second row, rightmost button and icon
global reportIm
reportIm = ImageTk.PhotoImage(Image.open("reportIm.jpg").resize((250,200)))
displayReportIm = tk.Label(window, image=reportIm);
displayReportIm.place(x=830, y=410, width=250, height=200);

buttonReports = tk.Button(window,
                          text = "Reports",
                          font=("Arial, 18"),
                          bg="peru")
buttonReports.place(x=830, y=615, width=250, height=50)

################################################################################

window.mainloop()

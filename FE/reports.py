from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from PIL import ImageTk, Image
import backendSQL as sqlFuncs

window = Tk()


## Reports Landing Page
def destroyReportsMenu():
    reportsMenu.destroy()

def openBookSearch():
    openChooseSearchField()
    chooseSearchFieldMenu.lift()

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

def destroyBookSearchFieldMenu():
    chooseSearchFieldMenu.destroy()

def navFromBookSearchToReports():
    reportsMenuFunc()
    destroyBookSearchMenu()
    reportsMenu.lift()
    reportsMenu.lift()


############################################
## Reports 1.1 - Book Search Field Selection 
############################################
def openChooseSearchField():
    global chooseSearchFieldMenu
    chooseSearchFieldMenu = Toplevel()
    chooseSearchFieldMenu.title("Choose A Search Field")
    chooseSearchFieldMenu.geometry("500x500")

    def chooseTitleField():
        bookSearchMenuFunc("Title")
        destroyBookSearchFieldMenu()
        destroyReportsMenu()
        bookSearchMenu.lift()

    def chooseAuthorField():
        bookSearchMenuFunc("Author")
        destroyBookSearchFieldMenu()
        destroyReportsMenu()
        bookSearchMenu.lift()

    def chooseISBNField():
        bookSearchMenuFunc("ISBN")
        destroyBookSearchFieldMenu()
        destroyReportsMenu()
        bookSearchMenu.lift()

    def choosePublisherField():
        bookSearchMenuFunc("Publisher")
        destroyBookSearchFieldMenu()
        destroyReportsMenu()
        bookSearchMenu.lift()

    def choosePublishingYearField():
        bookSearchMenuFunc("Publishing Year")
        destroyBookSearchFieldMenu()
        destroyReportsMenu()
        bookSearchMenu.lift()

    ## Information Header
    bookSearchMenuLabel = Label(chooseSearchFieldMenu,
                       text = "Please Choose a Search Field",
                       font =("calibre", 20, "bold"),
                       bg = "LightSteelBlue2")
    bookSearchMenuLabel.place(x=0, y=0, width=500, height=80);

    ## Book Search Title Button
    bookSearchTitleButton = Button(chooseSearchFieldMenu,
        text = "Title",
        font = ("calibre", 10, "bold"),
        fg = "black",
        bg = "plum2",
        command = chooseTitleField)
    bookSearchTitleButton.place(x=90, y=150, width=150, height=50)

    ## Book Search Author Button
    bookSearchAuthorButton = Button(chooseSearchFieldMenu,
        text = "Author",
        font = ("calibre", 10, "bold"),
        fg = "black",
        bg = "plum2",
        command = chooseAuthorField)
    bookSearchAuthorButton.place(x=260, y=150, width=150, height=50)

    ## Book Search ISBN Button
    bookSearchISBNButton = Button(chooseSearchFieldMenu,
        text = "ISBN",
        font = ("calibre", 10, "bold"),
        fg = "black",
        bg = "plum2",
        command = chooseISBNField)
    bookSearchISBNButton.place(x=90, y=220, width=150, height=50)

    ## Book Search Publisher Button
    bookSearchPublisherButton = Button(chooseSearchFieldMenu,
        text = "Publisher",
        font = ("calibre", 10, "bold"),
        fg = "black",
        bg = "plum2",
        command = choosePublisherField)
    bookSearchPublisherButton.place(x=260, y=220, width=150, height=50)

    ## Book Search Publication Year Button
    bookSearchPublicationYearButton = Button(chooseSearchFieldMenu,
        text = "Publication\nYear",
        font = ("calibre", 10, "bold"),
        fg = "black",
        bg = "plum2",
        command = choosePublishingYearField)
    bookSearchPublicationYearButton.place(x=175, y=290, width=150, height=50)

    ## Back Button
    bookSearchFieldBackButton = Button(chooseSearchFieldMenu,
        text = "Back",
        font = ("calibre", 15, "bold"),
        fg = "grey39",
        bg = "snow3",
        command = destroyBookSearchFieldMenu)
    bookSearchFieldBackButton.place(x=200, y=400, width=100, height=50)

def bookSearchMenuFunc(searchField):
    global bookSearchMenu
    bookSearchMenu = Toplevel()
    bookSearchMenu.title("Search a Book")
    bookSearchMenu.geometry("1280x720")

    def closeSearchResultTable():
        searchResultTable.destroy()
        bookSearchMenu.lift()

    def openSearchResultTable(result):
        global searchResultTable
        searchResultTable = Toplevel()
        searchResultTable.title("Search Results")
        searchResultTable.geometry("1100x600")

        numResultRows = len(result)
        numPages = numResultRows/3
        currentPage = 0

        ## Information Header
        searchResultInfoLabel = Label(searchResultTable,
                                    text = "Search Results",
                                    font =("calibre", 20, "bold"),
                                    bg = "LightSteelBlue2")
        searchResultInfoLabel.place(x=0, y=0, width=1100, height=80);

        ########################
        ## Table Headers
        ########################
        ## Acc Num
        searchResultAccNumLabel = Label(searchResultTable,
                                    text = "Accession Number",
                                    font =("calibre", 15, "bold"),
                                    bg = "LightSteelBlue1",
                                    wraplength=100,
                                    justify="center")
        searchResultAccNumLabel.place(x=20, y=100, width=150, height=80);

        ## Title 
        searchResultTitleLabel = Label(searchResultTable,
                                    text = "Title",
                                    font =("calibre", 15, "bold"),
                                    bg = "LightSteelBlue1",
                                    wraplength=180,
                                    justify="center")
        searchResultTitleLabel.place(x=170, y=100, width=250, height=80);

        ## Author
        searchResultAuthorsLabel = Label(searchResultTable,
                                    text = "Authors",
                                    font =("calibre", 15, "bold"),
                                    bg = "LightSteelBlue1",
                                    wraplength=180,
                                    justify="center")
        searchResultAuthorsLabel.place(x=420, y=100, width=250, height=80);

        ## ISBN
        searchResultISBNLabel = Label(searchResultTable,
                                    text = "ISBN",
                                    font =("calibre", 15, "bold"),
                                    bg = "LightSteelBlue1",
                                    wraplength=100,
                                    justify="center")
        searchResultISBNLabel.place(x=670, y=100, width=150, height=80);

        ## Publisher
        searchResultPublisherLabel = Label(searchResultTable,
                                    text = "Publisher",
                                    font =("calibre", 15, "bold"),
                                    bg = "LightSteelBlue1",
                                    wraplength=100,
                                    justify="center")
        searchResultPublisherLabel.place(x=820, y=100, width=150, height=80);

        ## Publishing Year
        searchResultPublisherLabel = Label(searchResultTable,
                                    text = "Year",
                                    font =("calibre", 15, "bold"),
                                    bg = "LightSteelBlue1",
                                    wraplength=100,
                                    justify="center")
        searchResultPublisherLabel.place(x=970, y=100, width=110, height=80);

        ## Table rows here - 3 rows per page
        resultsOnCurrPage = (result[0+currentPage*3],
                                result[1+currentPage*3],
                                result[2+currentPage*3])

        #####################################
        ## Row 1
        #####################################
        ## Acc Num
        searchResultRow1AccNumLabel = Label(searchResultTable,
                                    text = resultsOnCurrPage[0][0],
                                    font =("calibre", 15, "bold"),
                                    bg = "GhostWhite",
                                    wraplength=100,
                                    justify="center")
        searchResultRow1AccNumLabel.place(x=20, y=180, width=150, height=80);

        ## Title 
        searchResultRow1TitleLabel = Label(searchResultTable,
                                    text = resultsOnCurrPage[0][1],
                                    font =("calibre", 15, "bold"),
                                    bg = "GhostWhite",
                                    wraplength=180,
                                    justify="center")
        searchResultRow1TitleLabel.place(x=170, y=180, width=250, height=80);

        ## Author
        searchResultRow1AuthorsLabel = Label(searchResultTable,
                                    text = resultsOnCurrPage[0][2],
                                    font =("calibre", 15, "bold"),
                                    bg = "GhostWhite",
                                    wraplength=180,
                                    justify="center")
        searchResultRow1AuthorsLabel.place(x=420, y=180, width=250, height=80);

        ## ISBN
        searchResultRow1ISBNLabel = Label(searchResultTable,
                                    text = resultsOnCurrPage[0][3],
                                    font =("calibre", 15, "bold"),
                                    bg = "GhostWhite",
                                    wraplength=100,
                                    justify="center")
        searchResultRow1ISBNLabel.place(x=670, y=180, width=150, height=80);

        ## Publisher
        searchResultRow1PublisherLabel = Label(searchResultTable,
                                    text = resultsOnCurrPage[0][4],
                                    font =("calibre", 15, "bold"),
                                    bg = "GhostWhite",
                                    wraplength=100,
                                    justify="center")
        searchResultRow1PublisherLabel.place(x=820, y=180, width=150, height=80);

        ## Publishing Year
        searchResultRow1PublisherLabel = Label(searchResultTable,
                                    text = resultsOnCurrPage[0][5],
                                    font =("calibre", 15, "bold"),
                                    bg = "GhostWhite",
                                    wraplength=100,
                                    justify="center")
        searchResultRow1PublisherLabel.place(x=970, y=180, width=110, height=80);

        #####################################
        ## Row 2
        #####################################
        ## Acc Num
        searchResultRow2AccNumLabel = Label(searchResultTable,
                                    text = resultsOnCurrPage[1][0],
                                    font =("calibre", 15, "bold"),
                                    bg = "GhostWhite",
                                    wraplength=100,
                                    justify="center")
        searchResultRow2AccNumLabel.place(x=20, y=260, width=150, height=80);

        ## Title 
        searchResultRow2TitleLabel = Label(searchResultTable,
                                    text = resultsOnCurrPage[1][1],
                                    font =("calibre", 15, "bold"),
                                    bg = "GhostWhite",
                                    wraplength=180,
                                    justify="center")
        searchResultRow2TitleLabel.place(x=170, y=260, width=250, height=80);

        ## Author
        searchResultRow2AuthorsLabel = Label(searchResultTable,
                                    text = resultsOnCurrPage[1][2],
                                    font =("calibre", 15, "bold"),
                                    bg = "GhostWhite",
                                    wraplength=180,
                                    justify="center")
        searchResultRow2AuthorsLabel.place(x=420, y=260, width=250, height=80);

        ## ISBN
        searchResultRow2ISBNLabel = Label(searchResultTable,
                                    text = resultsOnCurrPage[1][3],
                                    font =("calibre", 15, "bold"),
                                    bg = "GhostWhite",
                                    wraplength=100,
                                    justify="center")
        searchResultRow2ISBNLabel.place(x=670, y=260, width=150, height=80);

        ## Publisher
        searchResultRow2PublisherLabel = Label(searchResultTable,
                                    text = resultsOnCurrPage[1][4],
                                    font =("calibre", 15, "bold"),
                                    bg = "GhostWhite",
                                    wraplength=100,
                                    justify="center")
        searchResultRow2PublisherLabel.place(x=820, y=260, width=150, height=80);

        ## Publishing Year
        searchResultRow2PublisherLabel = Label(searchResultTable,
                                    text = resultsOnCurrPage[1][5],
                                    font =("calibre", 15, "bold"),
                                    bg = "GhostWhite",
                                    wraplength=100,
                                    justify="center")
        searchResultRow2PublisherLabel.place(x=970, y=260, width=110, height=80);

        #####################################
        ## Row 3
        #####################################
        ## Acc Num
        searchResultRow3AccNumLabel = Label(searchResultTable,
                                    text = resultsOnCurrPage[2][0],
                                    font =("calibre", 15, "bold"),
                                    bg = "GhostWhite",
                                    wraplength=100,
                                    justify="center")
        searchResultRow3AccNumLabel.place(x=20, y=340, width=150, height=80);

        ## Title 
        searchResultRow3TitleLabel = Label(searchResultTable,
                                    text = resultsOnCurrPage[2][1],
                                    font =("calibre", 15, "bold"),
                                    bg = "GhostWhite",
                                    wraplength=180,
                                    justify="center")
        searchResultRow3TitleLabel.place(x=170, y=340, width=250, height=80);

        ## Author
        searchResultRow3AuthorsLabel = Label(searchResultTable,
                                    text = resultsOnCurrPage[2][2],
                                    font =("calibre", 15, "bold"),
                                    bg = "GhostWhite",
                                    wraplength=180,
                                    justify="center")
        searchResultRow3AuthorsLabel.place(x=420, y=340, width=250, height=80);

        ## ISBN
        searchResultRow3ISBNLabel = Label(searchResultTable,
                                    text = resultsOnCurrPage[2][3],
                                    font =("calibre", 15, "bold"),
                                    bg = "GhostWhite",
                                    wraplength=100,
                                    justify="center")
        searchResultRow3ISBNLabel.place(x=670, y=340, width=150, height=80);

        ## Publisher
        searchResultRow3PublisherLabel = Label(searchResultTable,
                                    text = resultsOnCurrPage[2][4],
                                    font =("calibre", 15, "bold"),
                                    bg = "GhostWhite",
                                    wraplength=100,
                                    justify="center")
        searchResultRow3PublisherLabel.place(x=820, y=340, width=150, height=80);

        ## Publishing Year
        searchResultRow3PublisherLabel = Label(searchResultTable,
                                    text = resultsOnCurrPage[2][5],
                                    font =("calibre", 15, "bold"),
                                    bg = "GhostWhite",
                                    wraplength=100,
                                    justify="center")
        searchResultRow3PublisherLabel.place(x=970, y=340, width=110, height=80);

        ## Table nav buttons

        ## Back Button
        searchResultBackButton = Button(searchResultTable,
                                        text = "Back",
                                        font = ("calibre", 15, "bold"),
                                        fg = "grey39",
                                        bg = "snow3",
                                        command = closeSearchResultTable)
        searchResultBackButton.place(x=475, y=500, width=150, height=40)

    def searchForBook():
        categoryToSearch = searchField
        if searchField == "Publishing Year":
            categoryToSearch = "PubYear"
        
        print("Searching for book")
        result = sqlFuncs.bookSearchReport(bookSearchFieldEntry.get(), searchField)

        openSearchResultTable(result)
    
    ## Information Header
    bookSearchMenuLabel = Label(bookSearchMenu,
                       text = "Please Enter Requested Information Below",
                       font =("calibre", 20, "bold"),
                       bg = "LightSteelBlue2")
    bookSearchMenuLabel.place(x=0, y=0, width=1280, height=80);               

    ## Input Field
    bookSearchFieldInputLabel = Label(bookSearchMenu,
                              text = searchField,
                              font = ("calibre", 15),
                              bg = "LightBlue1")
    bookSearchFieldInputLabel.place(x=50, y=350, width=200, height=80)

    global bookSearchFieldEntry
    bookSearchFieldEntry = Entry(bookSearchMenu,
                        font = ("calibre", 10, "italic"),
                        fg = "blue2")
    bookSearchFieldEntry.place(x=300, y=370, width=700, height=30)

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


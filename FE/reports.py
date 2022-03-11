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
    result = sqlFuncs.loanReport()
    booksOnLoanFunc(result,0)
    booksOnLoanMenu.lift()
    booksOnLoanMenu.lift()

def openBooksOnReserv():
    result = sqlFuncs.reservationReport()
    booksOnReservFunc(result,0)
    booksOnReservMenu.lift()
    booksOnReservMenu.lift()

def openOutstandingFines():
    result = sqlFuncs.outsFineReport()
    outstandingFinesFunc(result, 0)
    outstandingFinesMenu.lift()
    outstandingFinesMenu.lift()

def openBooksOnLoanToMember():
    booksOnLoanToMemberMenuFunc()
    destroyReportsMenu()
    booksOnLoanToMemberMenu.lift()
    booksOnLoanToMemberMenu.lift()

def goHome():
    landingPageFunc()
    destroyReportsMenu()
    landingPage.lift()

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

##HERE1

############################################
## Reports 2 - Books on Loan 
############################################

def booksOnLoanFunc(sqlResult,currentPage):
    global booksOnLoanMenu
    booksOnLoanMenu = Toplevel()
    booksOnLoanMenu.title("Books on Loan")
    booksOnLoanMenu.geometry("1100x600")

    numResultRows = len(sqlResult)
    numPages = numResultRows/3

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

    ########################
    ## Table Headers
    ########################
    ## Acc Num
    booksOnLoanResultAccNumLabel = Label(booksOnLoanMenu,
                                text = "Accession Number",
                                font =("calibre", 15, "bold"),
                                bg = "LightSteelBlue1",
                                wraplength=100,
                                justify="center")
    booksOnLoanResultAccNumLabel.place(x=20, y=100, width=150, height=80);

    ## Title 
    booksOnLoanResultTitleLabel = Label(booksOnLoanMenu,
                                text = "Title",
                                font =("calibre", 15, "bold"),
                                bg = "LightSteelBlue1",
                                wraplength=180,
                                justify="center")
    booksOnLoanResultTitleLabel.place(x=170, y=100, width=250, height=80);

    ## Author
    booksOnLoanResultAuthorsLabel = Label(booksOnLoanMenu,
                                text = "Authors",
                                font =("calibre", 15, "bold"),
                                bg = "LightSteelBlue1",
                                wraplength=180,
                                justify="center")
    booksOnLoanResultAuthorsLabel.place(x=420, y=100, width=250, height=80);

    ## ISBN
    booksOnLoanResultISBNLabel = Label(booksOnLoanMenu,
                                text = "ISBN",
                                font =("calibre", 15, "bold"),
                                bg = "LightSteelBlue1",
                                wraplength=100,
                                justify="center")
    booksOnLoanResultISBNLabel.place(x=670, y=100, width=150, height=80);

    ## Publisher
    booksOnLoanResultPublisherLabel = Label(booksOnLoanMenu,
                                text = "Publisher",
                                font =("calibre", 15, "bold"),
                                bg = "LightSteelBlue1",
                                wraplength=100,
                                justify="center")
    booksOnLoanResultPublisherLabel.place(x=820, y=100, width=150, height=80);

    ## Publishing Year
    booksOnLoanResultPubYearLabel = Label(booksOnLoanMenu,
                                text = "Year",
                                font =("calibre", 15, "bold"),
                                bg = "LightSteelBlue1",
                                wraplength=100,
                                justify="center")
    booksOnLoanResultPubYearLabel.place(x=970, y=100, width=110, height=80);

    ## Table rows here - 3 rows per page
    result = sqlResult
    numResultsOnCurrPageOnwards = len(result)-(currentPage)*3
    tempTuple = ((result[0+currentPage*3]), ())
    resultsOnCurrPageList = list(tempTuple)

    if numResultsOnCurrPageOnwards >= 2:
        resultsOnCurrPageList.pop()
        resultsOnCurrPageList.append(result[1+currentPage*3])

    if numResultsOnCurrPageOnwards >= 3:
        resultsOnCurrPageList.append(result[2+currentPage*3])

    resultsOnCurrPage = tuple(resultsOnCurrPageList)
    #####################################
    ## Row 1
    #####################################
    if numResultsOnCurrPageOnwards >= 1:
        ## Acc Num
        booksOnLoanResultRow1AccNumLabel = Label(booksOnLoanMenu,
                                    text = resultsOnCurrPage[0][0],
                                    font =("calibre", 15, "bold"),
                                    bg = "GhostWhite",
                                    wraplength=100,
                                    justify="center")
        booksOnLoanResultRow1AccNumLabel.place(x=20, y=180, width=150, height=80);

        ## Title 
        booksOnLoanResultRow1TitleLabel = Label(booksOnLoanMenu,
                                    text = resultsOnCurrPage[0][1],
                                    font =("calibre", 15, "bold"),
                                    bg = "GhostWhite",
                                    wraplength=180,
                                    justify="center")
        booksOnLoanResultRow1TitleLabel.place(x=170, y=180, width=250, height=80);

        ## Author
        booksOnLoanResultRow1AuthorsLabel = Label(booksOnLoanMenu,
                                    text = resultsOnCurrPage[0][2],
                                    font =("calibre", 15, "bold"),
                                    bg = "GhostWhite",
                                    wraplength=180,
                                    justify="center")
        booksOnLoanResultRow1AuthorsLabel.place(x=420, y=180, width=250, height=80);

        ## ISBN
        booksOnLoanResultRow1ISBNLabel = Label(booksOnLoanMenu,
                                    text = resultsOnCurrPage[0][3],
                                    font =("calibre", 15, "bold"),
                                    bg = "GhostWhite",
                                    wraplength=100,
                                    justify="center")
        booksOnLoanResultRow1ISBNLabel.place(x=670, y=180, width=150, height=80);

        ## Publisher
        booksOnLoanResultRow1PublisherLabel = Label(booksOnLoanMenu,
                                    text = resultsOnCurrPage[0][4],
                                    font =("calibre", 15, "bold"),
                                    bg = "GhostWhite",
                                    wraplength=100,
                                    justify="center")
        booksOnLoanResultRow1PublisherLabel.place(x=820, y=180, width=150, height=80);

        ## Publishing Year
        booksOnLoanResultRow1PubYearLabel = Label(booksOnLoanMenu,
                                    text = resultsOnCurrPage[0][5],
                                    font =("calibre", 15, "bold"),
                                    bg = "GhostWhite",
                                    wraplength=100,
                                    justify="center")
        booksOnLoanResultRow1PubYearLabel.place(x=970, y=180, width=110, height=80);

    #####################################
    ## Row 2
    #####################################
    ## Acc Num
    if numResultsOnCurrPageOnwards >= 2:
        booksOnLoanResultRow2AccNumLabel = Label(booksOnLoanMenu,
                                    text = resultsOnCurrPage[1][0],
                                    font =("calibre", 15, "bold"),
                                    bg = "GhostWhite",
                                    wraplength=100,
                                    justify="center")
        booksOnLoanResultRow2AccNumLabel.place(x=20, y=260, width=150, height=80);

        ## Title 
        booksOnLoanResultRow2TitleLabel = Label(booksOnLoanMenu,
                                    text = resultsOnCurrPage[1][1],
                                    font =("calibre", 15, "bold"),
                                    bg = "GhostWhite",
                                    wraplength=180,
                                    justify="center")
        booksOnLoanResultRow2TitleLabel.place(x=170, y=260, width=250, height=80);

        ## Author
        booksOnLoanResultRow2AuthorsLabel = Label(booksOnLoanMenu,
                                    text = resultsOnCurrPage[1][2],
                                    font =("calibre", 15, "bold"),
                                    bg = "GhostWhite",
                                    wraplength=180,
                                    justify="center")
        booksOnLoanResultRow2AuthorsLabel.place(x=420, y=260, width=250, height=80);

        ## ISBN
        booksOnLoanResultRow2ISBNLabel = Label(booksOnLoanMenu,
                                    text = resultsOnCurrPage[1][3],
                                    font =("calibre", 15, "bold"),
                                    bg = "GhostWhite",
                                    wraplength=100,
                                    justify="center")
        booksOnLoanResultRow2ISBNLabel.place(x=670, y=260, width=150, height=80);

        ## Publisher
        booksOnLoanResultRow2PublisherLabel = Label(booksOnLoanMenu,
                                    text = resultsOnCurrPage[1][4],
                                    font =("calibre", 15, "bold"),
                                    bg = "GhostWhite",
                                    wraplength=100,
                                    justify="center")
        booksOnLoanResultRow2PublisherLabel.place(x=820, y=260, width=150, height=80);

        ## Publishing Year
        booksOnLoanResultRow2PublisherLabel = Label(booksOnLoanMenu,
                                    text = resultsOnCurrPage[1][5],
                                    font =("calibre", 15, "bold"),
                                    bg = "GhostWhite",
                                    wraplength=100,
                                    justify="center")
        booksOnLoanResultRow2PublisherLabel.place(x=970, y=260, width=110, height=80);

    #####################################
    ## Row 3
    #####################################
    if numResultsOnCurrPageOnwards >= 3:
        ## Acc Num
        booksOnLoanResultRow3AccNumLabel = Label(booksOnLoanMenu,
                                    text = resultsOnCurrPage[2][0],
                                    font =("calibre", 15, "bold"),
                                    bg = "GhostWhite",
                                    wraplength=100,
                                    justify="center")
        booksOnLoanResultRow3AccNumLabel.place(x=20, y=340, width=150, height=80);

        ## Title 
        booksOnLoanResultRow3TitleLabel = Label(booksOnLoanMenu,
                                    text = resultsOnCurrPage[2][1],
                                    font =("calibre", 15, "bold"),
                                    bg = "GhostWhite",
                                    wraplength=180,
                                    justify="center")
        booksOnLoanResultRow3TitleLabel.place(x=170, y=340, width=250, height=80);

        ## Author
        booksOnLoanResultRow3AuthorsLabel = Label(booksOnLoanMenu,
                                    text = resultsOnCurrPage[2][2],
                                    font =("calibre", 15, "bold"),
                                    bg = "GhostWhite",
                                    wraplength=180,
                                    justify="center")
        booksOnLoanResultRow3AuthorsLabel.place(x=420, y=340, width=250, height=80);

        ## ISBN
        booksOnLoanResultRow3ISBNLabel = Label(booksOnLoanMenu,
                                    text = resultsOnCurrPage[2][3],
                                    font =("calibre", 15, "bold"),
                                    bg = "GhostWhite",
                                    wraplength=100,
                                    justify="center")
        booksOnLoanResultRow3ISBNLabel.place(x=670, y=340, width=150, height=80);

        ## Publisher
        booksOnLoanResultRow3PublisherLabel = Label(booksOnLoanMenu,
                                    text = resultsOnCurrPage[2][4],
                                    font =("calibre", 15, "bold"),
                                    bg = "GhostWhite",
                                    wraplength=100,
                                    justify="center")
        booksOnLoanResultRow3PublisherLabel.place(x=820, y=340, width=150, height=80);

        ## Publishing Year
        booksOnLoanResultRow3PublisherLabel = Label(booksOnLoanMenu,
                                    text = resultsOnCurrPage[2][5],
                                    font =("calibre", 15, "bold"),
                                    bg = "GhostWhite",
                                    wraplength=100,
                                    justify="center")
        booksOnLoanResultRow3PublisherLabel.place(x=970, y=340, width=110, height=80);

    ## Table nav buttons
    def openNextTable():
        if currentPage != numPages-1:
            booksOnLoanMenu.destroy()
            booksOnLoanFunc(result, currentPage+1)


    def openPrevTable():
        if currentPage != 0:
            booksOnLoanMenu.destroy()
            booksOnLoanFunc(result, currentPage-1)

    booksOnLoanResultPrevTableButton = Button(booksOnLoanMenu,
                                    text = "<<",
                                    font = ("calibre", 15, "bold"),
                                    fg = "grey39",
                                    bg = "snow3",
                                    command = openPrevTable)
    booksOnLoanResultPrevTableButton.place(x=200, y=450, width=20, height=20)

    booksOnLoanResultCurrPageLabel = Label(booksOnLoanMenu,
                                text = "Current Page: {}".format(currentPage+1),
                                font =("calibre", 15, "bold"))
    booksOnLoanResultCurrPageLabel.place(x=470, y=430, width=180, height=60);

    booksOnLoanResultNextTableButton = Button(booksOnLoanMenu,
                                    text = ">>",
                                    font = ("calibre", 15, "bold"),
                                    fg = "grey39",
                                    bg = "snow3",
                                    command = openNextTable)
    booksOnLoanResultNextTableButton.place(x=900, y=450, width=20, height=20)


############################################
## Reports 3 - Books on Reserv 
############################################

def booksOnReservFunc(sqlResult,currentPage):
    global booksOnReservMenu
    booksOnReservMenu = Toplevel()
    booksOnReservMenu.title("Books on Reservation")
    booksOnReservMenu.geometry("1100x600")

    numResultRows = len(sqlResult)
    numPages = numResultRows/3

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


    ########################
    ## Table Headers
    ########################
    ## Acc Num
    reservationResultAccNumLabel = Label(booksOnReservMenu,
                                text = "Accession Number",
                                font =("calibre", 15, "bold"),
                                bg = "LightSteelBlue1",
                                wraplength=100,
                                justify="center")
    reservationResultAccNumLabel.place(x=120, y=100, width=150, height=80);

    ## Title 
    reservationResultTitleLabel = Label(booksOnReservMenu,
                                text = "Title",
                                font =("calibre", 15, "bold"),
                                bg = "LightSteelBlue1",
                                wraplength=180,
                                justify="center")
    reservationResultTitleLabel.place(x=270, y=100, width=250, height=80);

    ## Membership Id
    reservationResultMembershipIDLabel = Label(booksOnReservMenu,
                                text = "Membership ID",
                                font =("calibre", 15, "bold"),
                                bg = "LightSteelBlue1",
                                wraplength=180,
                                justify="center")
    reservationResultMembershipIDLabel.place(x=520, y=100, width=250, height=80);

    ## Name
    reservationResultNameLabel = Label(booksOnReservMenu,
                                text = "Name",
                                font =("calibre", 15, "bold"),
                                bg = "LightSteelBlue1",
                                wraplength=100,
                                justify="center")
    reservationResultNameLabel.place(x=770, y=100, width=150, height=80);

    ## Table rows here - 3 rows per page
    result = sqlResult
    numResultsOnCurrPageOnwards = len(result)-(currentPage)*3
    tempTuple = ((result[0+currentPage*3]), ())
    resultsOnCurrPageList = list(tempTuple)

    if numResultsOnCurrPageOnwards >= 2:
        resultsOnCurrPageList.pop()
        resultsOnCurrPageList.append(result[1+currentPage*3])

    if numResultsOnCurrPageOnwards >= 3:
        resultsOnCurrPageList.append(result[2+currentPage*3])


    resultsOnCurrPage = tuple(resultsOnCurrPageList)
    #####################################
    ## Row 1
    #####################################
    if numResultsOnCurrPageOnwards >= 1:
        ## Acc Num
        reservationResultRow1AccNumLabel = Label(booksOnReservMenu,
                                    text = resultsOnCurrPage[0][0],
                                    font =("calibre", 15, "bold"),
                                    bg = "GhostWhite",
                                    wraplength=100,
                                    justify="center")
        reservationResultRow1AccNumLabel.place(x=120, y=180, width=150, height=80);

        ## Title 
        reservationResultRow1TitleLabel = Label(booksOnReservMenu,
                                    text = resultsOnCurrPage[0][1],
                                    font =("calibre", 15, "bold"),
                                    bg = "GhostWhite",
                                    wraplength=180,
                                    justify="center")
        reservationResultRow1TitleLabel.place(x=270, y=180, width=250, height=80);

        ## Membership ID
        reservationResultRow1MembershipIDLabel = Label(booksOnReservMenu,
                                    text = resultsOnCurrPage[0][2],
                                    font =("calibre", 15, "bold"),
                                    bg = "GhostWhite",
                                    wraplength=180,
                                    justify="center")
        reservationResultRow1MembershipIDLabel.place(x=520, y=180, width=250, height=80);

        ## Name
        reservationResultRow1NameLabel = Label(booksOnReservMenu,
                                    text = resultsOnCurrPage[0][3],
                                    font =("calibre", 15, "bold"),
                                    bg = "GhostWhite",
                                    wraplength=100,
                                    justify="center")
        reservationResultRow1NameLabel.place(x=770, y=180, width=150, height=80);

        
    #####################################
    ## Row 2
    #####################################
    if numResultsOnCurrPageOnwards >= 2:
        ## Acc Num
        reservationResultRow2AccNumLabel = Label(booksOnReservMenu,
                                    text = resultsOnCurrPage[1][0],
                                    font =("calibre", 15, "bold"),
                                    bg = "GhostWhite",
                                    wraplength=100,
                                    justify="center")
        reservationResultRow2AccNumLabel.place(x=120, y=260, width=150, height=80);

        ## Title 
        reservationResultRow2TitleLabel = Label(booksOnReservMenu,
                                    text = resultsOnCurrPage[1][1],
                                    font =("calibre", 15, "bold"),
                                    bg = "GhostWhite",
                                    wraplength=180,
                                    justify="center")
        reservationResultRow2TitleLabel.place(x=270, y=260, width=250, height=80);

        ## Membership ID
        reservationResultRow2MembershipIDLabel = Label(booksOnReservMenu,
                                    text = resultsOnCurrPage[1][2],
                                    font =("calibre", 15, "bold"),
                                    bg = "GhostWhite",
                                    wraplength=180,
                                    justify="center")
        reservationResultRow2MembershipIDLabel.place(x=520, y=260, width=250, height=80);

        ## Name
        reservationResultRow2NameLabel = Label(booksOnReservMenu,
                                    text = resultsOnCurrPage[1][3],
                                    font =("calibre", 15, "bold"),
                                    bg = "GhostWhite",
                                    wraplength=100,
                                    justify="center")
        reservationResultRow2NameLabel.place(x=770, y=260, width=150, height=80)

    #####################################
    ## Row 3
    #####################################
    if numResultsOnCurrPageOnwards >= 3:
        ## Acc Num
        reservationResultRow3AccNumLabel = Label(booksOnReservMenu,
                                    text = resultsOnCurrPage[2][0],
                                    font =("calibre", 15, "bold"),
                                    bg = "GhostWhite",
                                    wraplength=100,
                                    justify="center")
        reservationResultRow3AccNumLabel.place(x=120, y=340, width=150, height=80);

        ## Title 
        reservationResultRow3TitleLabel = Label(booksOnReservMenu,
                                    text = resultsOnCurrPage[2][1],
                                    font =("calibre", 15, "bold"),
                                    bg = "GhostWhite",
                                    wraplength=180,
                                    justify="center")
        reservationResultRow3TitleLabel.place(x=270, y=340, width=250, height=80);

        ## Membership ID
        reservationResultRow3MembershipIDLabel = Label(booksOnReservMenu,
                                    text = resultsOnCurrPage[2][2],
                                    font =("calibre", 15, "bold"),
                                    bg = "GhostWhite",
                                    wraplength=180,
                                    justify="center")
        reservationResultRow3MembershipIDLabel.place(x=520, y=340, width=250, height=80);

        ## Name
        reservationResultRow3NameLabel = Label(booksOnReservMenu,
                                    text = resultsOnCurrPage[2][3],
                                    font =("calibre", 15, "bold"),
                                    bg = "GhostWhite",
                                    wraplength=100,
                                    justify="center")
        reservationResultRow3NameLabel.place(x=770, y=340, width=150, height=80)

    ## Table nav buttons
    def openNextTable():
        if currentPage != numPages-1:
            booksOnReservMenu.destroy()
            booksOnReservFunc(result, currentPage+1)

    def openPrevTable():
        if currentPage != 0:
            booksOnReservMenu.destroy()
            booksOnReservFunc(result, currentPage-1)

    reservationResultPrevTableButton = Button(booksOnReservMenu,
                                    text = "<<",
                                    font = ("calibre", 15, "bold"),
                                    fg = "grey39",
                                    bg = "snow3",
                                    command = openPrevTable)
    reservationResultPrevTableButton.place(x=200, y=450, width=20, height=20)

    reservationResultCurrPageLabel = Label(booksOnReservMenu,
                                text = "Current Page: {}".format(currentPage+1),
                                font =("calibre", 15, "bold"))
    reservationResultCurrPageLabel.place(x=470, y=430, width=180, height=60);

    reservationResultNextTableButton = Button(booksOnReservMenu,
                                    text = ">>",
                                    font = ("calibre", 15, "bold"),
                                    fg = "grey39",
                                    bg = "snow3",
                                    command = openNextTable)
    reservationResultNextTableButton.place(x=900, y=450, width=20, height=20)



############################################
## Reports 4 - Members with Outstanding Fines
############################################

def outstandingFinesFunc(result, currentPage):
    global outstandingFinesMenu
    outstandingFinesMenu = Toplevel()
    outstandingFinesMenu.title("Members with Fines")
    outstandingFinesMenu.geometry("1100x600")

    def closeOutstandingFinesMenuMenu():
        reportsMenu.lift()
        outstandingFinesMenu.destroy()

    numResultRows = len(result)
    numPages = numResultRows/3

    ## Information Header
    searchResultInfoLabel = Label(outstandingFinesMenu,
                                text = "Search Results",
                                font =("calibre", 20, "bold"),
                                bg = "LightSteelBlue2")
    searchResultInfoLabel.place(x=0, y=0, width=1100, height=80);

    ########################
    ## Table Headers
    ########################
    ## MembershipId
    finesMembershipIdLabel = Label(outstandingFinesMenu,
                                text = "Membership\nId",
                                font =("calibre", 15, "bold"),
                                bg = "LightSteelBlue1",
                                wraplength=120,
                                justify="center")
    finesMembershipIdLabel.place(x=20, y=100, width=150, height=80);

    ## Name 
    finesNameLabel = Label(outstandingFinesMenu,
                                text = "Name",
                                font =("calibre", 15, "bold"),
                                bg = "LightSteelBlue1",
                                wraplength=180,
                                justify="center")
    finesNameLabel.place(x=170, y=100, width=250, height=80);

    ## Faculty
    finesFacultyLabel = Label(outstandingFinesMenu,
                                text = "Faculty",
                                font =("calibre", 15, "bold"),
                                bg = "LightSteelBlue1",
                                wraplength=180,
                                justify="center")
    finesFacultyLabel.place(x=420, y=100, width=250, height=80);

    ## Phone Number
    finesPhoneNumberLabel = Label(outstandingFinesMenu,
                                text = "Phone Number",
                                font =("calibre", 15, "bold"),
                                bg = "LightSteelBlue1",
                                wraplength=100,
                                justify="center")
    finesPhoneNumberLabel.place(x=670, y=100, width=170, height=80);

    ## Email Address
    finesEmailLabel = Label(outstandingFinesMenu,
                            text = "Email Address",
                            font =("calibre", 15, "bold"),
                            bg = "LightSteelBlue1",
                            wraplength=180,
                            justify="center")
    finesEmailLabel.place(x=840, y=100, width=240, height=80);

    ## Table rows here - 3 rows per page
    numResultsOnCurrPageOnwards = len(result)-(currentPage)*3
    tempTuple = ((result[0+currentPage*3]), ())
    resultsOnCurrPageList = list(tempTuple)

    if numResultsOnCurrPageOnwards >= 2:
        resultsOnCurrPageList.pop()
        resultsOnCurrPageList.append(result[1+currentPage*3])

    if numResultsOnCurrPageOnwards >= 3:
        resultsOnCurrPageList.append(result[2+currentPage*3])

    resultsOnCurrPage = tuple(resultsOnCurrPageList)
    #####################################
    ## Row 1
    #####################################
    if numResultsOnCurrPageOnwards >= 1:
        ## Acc Num
        finesResultRow1MembershipIdLabel = Label(outstandingFinesMenu,
                                                text = resultsOnCurrPage[0][0],
                                                font =("calibre", 15, "bold"),
                                                bg = "GhostWhite",
                                                wraplength=120,
                                                justify="center")
        finesResultRow1MembershipIdLabel.place(x=20, y=180, width=150, height=80);

        ## Title 
        finesResultRow1NameLabel = Label(outstandingFinesMenu,
                                    text = resultsOnCurrPage[0][1],
                                    font =("calibre", 15, "bold"),
                                    bg = "GhostWhite",
                                    wraplength=180,
                                    justify="center")
        finesResultRow1NameLabel.place(x=170, y=180, width=250, height=80);

        ## Author
        finesResultRow1FacultyLabel = Label(outstandingFinesMenu,
                                    text = resultsOnCurrPage[0][2],
                                    font =("calibre", 15, "bold"),
                                    bg = "GhostWhite",
                                    wraplength=180,
                                    justify="center")
        finesResultRow1FacultyLabel.place(x=420, y=180, width=250, height=80);

        ## ISBN
        finesResultRow1PhoneNumberLabel = Label(outstandingFinesMenu,
                                    text = resultsOnCurrPage[0][3],
                                    font =("calibre", 15, "bold"),
                                    bg = "GhostWhite",
                                    wraplength=100,
                                    justify="center")
        finesResultRow1PhoneNumberLabel.place(x=670, y=180, width=170, height=80);

        ## Publisher
        finesResultRow1EmailLabel = Label(outstandingFinesMenu,
                                    text = resultsOnCurrPage[0][4],
                                    font =("calibre", 15, "bold"),
                                    bg = "GhostWhite",
                                    wraplength=180,
                                    justify="center")
        finesResultRow1EmailLabel.place(x=840, y=180, width=240, height=80);

    #####################################
    ## Row 2
    #####################################
    ## Acc Num
    if numResultsOnCurrPageOnwards >= 2:
        finesResultRow2MembershipIdLabel = Label(outstandingFinesMenu,
                                                    text = resultsOnCurrPage[1][0],
                                                    font =("calibre", 15, "bold"),
                                                    bg = "GhostWhite",
                                                    wraplength=120,
                                                    justify="center")
        finesResultRow2MembershipIdLabel.place(x=20, y=260, width=150, height=80);

        ## Title 
        finesResultRow2NameLabel = Label(outstandingFinesMenu,
                                    text = resultsOnCurrPage[1][1],
                                    font =("calibre", 15, "bold"),
                                    bg = "GhostWhite",
                                    wraplength=180,
                                    justify="center")
        finesResultRow2NameLabel.place(x=170, y=260, width=250, height=80);

        ## Author
        finesResultRow2FacultyLabel = Label(outstandingFinesMenu,
                                    text = resultsOnCurrPage[1][2],
                                    font =("calibre", 15, "bold"),
                                    bg = "GhostWhite",
                                    wraplength=180,
                                    justify="center")
        finesResultRow2FacultyLabel.place(x=420, y=260, width=250, height=80);

        ## ISBN
        finesResultRow2PhoneNumberLabel = Label(outstandingFinesMenu,
                                    text = resultsOnCurrPage[1][3],
                                    font =("calibre", 15, "bold"),
                                    bg = "GhostWhite",
                                    wraplength=100,
                                    justify="center")
        finesResultRow2PhoneNumberLabel.place(x=670, y=260, width=170, height=80);

        ## Publisher
        finesResultRow2EmailLabel = Label(outstandingFinesMenu,
                                    text = resultsOnCurrPage[1][4],
                                    font =("calibre", 15, "bold"),
                                    bg = "GhostWhite",
                                    wraplength=180,
                                    justify="center")
        finesResultRow2EmailLabel.place(x=840, y=260, width=240, height=80);

    #####################################
    ## Row 3
    #####################################
    if numResultsOnCurrPageOnwards >= 3:
        ## Acc Num
        finesResultRow3MembershipIdLabel = Label(outstandingFinesMenu,
                                            text = resultsOnCurrPage[2][0],
                                            font =("calibre", 15, "bold"),
                                            bg = "GhostWhite",
                                            wraplength=120,
                                            justify="center")
        finesResultRow3MembershipIdLabel.place(x=20, y=340, width=150, height=80);

        ## Title 
        finesResultRow3NameLabel = Label(outstandingFinesMenu,
                                    text = resultsOnCurrPage[2][1],
                                    font =("calibre", 15, "bold"),
                                    bg = "GhostWhite",
                                    wraplength=180,
                                    justify="center")
        finesResultRow3NameLabel.place(x=170, y=340, width=250, height=80);

        ## Author
        finesResultRow3FacultyLabel = Label(outstandingFinesMenu,
                                    text = resultsOnCurrPage[2][2],
                                    font =("calibre", 15, "bold"),
                                    bg = "GhostWhite",
                                    wraplength=180,
                                    justify="center")
        finesResultRow3FacultyLabel.place(x=420, y=340, width=250, height=80);

        ## ISBN
        finesResultRow3PhoneNumberLabel = Label(outstandingFinesMenu,
                                    text = resultsOnCurrPage[2][3],
                                    font =("calibre", 15, "bold"),
                                    bg = "GhostWhite",
                                    wraplength=100,
                                    justify="center")
        finesResultRow3PhoneNumberLabel.place(x=670, y=340, width=170, height=80);

        ## Publisher
        finesResultRow3EmailLabel = Label(outstandingFinesMenu,
                                    text = resultsOnCurrPage[2][4],
                                    font =("calibre", 15, "bold"),
                                    bg = "GhostWhite",
                                    wraplength=180,
                                    justify="center")
        finesResultRow3EmailLabel.place(x=840, y=340, width=240, height=80);

    ## Table nav buttons
    def openNextTable():
        if currentPage != len(result)-1:
            outstandingFinesMenu.destroy()
            outstandingFinesFunc(result, currentPage+1)


    def openPrevTable():
        if currentPage != 0:
            outstandingFinesMenu.destroy()
            outstandingFinesFunc(result, currentPage-1)

    searchResultPrevTableButton = Button(outstandingFinesMenu,
                                    text = "<<",
                                    font = ("calibre", 15, "bold"),
                                    fg = "grey39",
                                    bg = "snow3",
                                    command = openPrevTable)
    searchResultPrevTableButton.place(x=200, y=450, width=20, height=20)

    searchResultCurrPageLabel = Label(outstandingFinesMenu,
                                text = "Current Page: {}".format(currentPage+1),
                                font =("calibre", 15, "bold"))
    searchResultCurrPageLabel.place(x=470, y=430, width=180, height=60);

    searchResultNextTableButton = Button(outstandingFinesMenu,
                                    text = ">>",
                                    font = ("calibre", 15, "bold"),
                                    fg = "grey39",
                                    bg = "snow3",
                                    command = openNextTable)
    searchResultNextTableButton.place(x=900, y=450, width=20, height=20)

    ## Back Button
    searchResultBackButton = Button(outstandingFinesMenu,
                                    text = "Back",
                                    font = ("calibre", 15, "bold"),
                                    fg = "grey39",
                                    bg = "snow3",
                                    command = closeOutstandingFinesMenuMenu)
    searchResultBackButton.place(x=475, y=500, width=150, height=40)

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

    def openSearchResultTable(result, currentPage):
        global searchResultTable
        searchResultTable = Toplevel()
        searchResultTable.title("Search Results")
        searchResultTable.geometry("1100x600")

        numResultRows = len(result)
        numPages = numResultRows/3

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
        numResultsOnCurrPageOnwards = len(result)-(currentPage)*3
        tempTuple = ((result[0+currentPage*3]), ())
        resultsOnCurrPageList = list(tempTuple)

        if numResultsOnCurrPageOnwards >= 2:
            resultsOnCurrPageList.pop()
            resultsOnCurrPageList.append(result[1+currentPage*3])

        if numResultsOnCurrPageOnwards >= 3:
            resultsOnCurrPageList.append(result[2+currentPage*3])

        resultsOnCurrPage = tuple(resultsOnCurrPageList)
        #####################################
        ## Row 1
        #####################################
        if numResultsOnCurrPageOnwards >= 1:
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
        if numResultsOnCurrPageOnwards >= 2:
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
        if numResultsOnCurrPageOnwards >= 3:
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
        def openNextTable():
            if currentPage != len(result)-1:
                searchResultTable.destroy()
                openSearchResultTable(result, currentPage+1)


        def openPrevTable():
            if currentPage != 0:
                searchResultTable.destroy()
                openSearchResultTable(result, currentPage-1)

        searchResultPrevTableButton = Button(searchResultTable,
                                        text = "<<",
                                        font = ("calibre", 15, "bold"),
                                        fg = "grey39",
                                        bg = "snow3",
                                        command = openPrevTable)
        searchResultPrevTableButton.place(x=200, y=450, width=20, height=20)

        searchResultCurrPageLabel = Label(searchResultTable,
                                    text = "Current Page: {}".format(currentPage+1),
                                    font =("calibre", 15, "bold"))
        searchResultCurrPageLabel.place(x=470, y=430, width=180, height=60);

        searchResultNextTableButton = Button(searchResultTable,
                                        text = ">>",
                                        font = ("calibre", 15, "bold"),
                                        fg = "grey39",
                                        bg = "snow3",
                                        command = openNextTable)
        searchResultNextTableButton.place(x=900, y=450, width=20, height=20)

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

            
        if len(bookSearchFieldEntry.get()) == 0:
            messagebox.showerror(
                        "Input Error",
                        "Error: Please insert a search term")
        else:
            result = sqlFuncs.bookSearchReport(bookSearchFieldEntry.get(), categoryToSearch)

            openSearchResultTable(result, 0)
    
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

    def closeSearchResultTable():
        loanToMemberSearchResultTable.destroy()
        booksOnLoanToMemberMenu.lift()

    def openSearchResultTable(result, currentPage):
        global loanToMemberSearchResultTable
        loanToMemberSearchResultTable = Toplevel()
        loanToMemberSearchResultTable.title("Search Results")
        loanToMemberSearchResultTable.geometry("1100x600")

        numResultRows = len(result)
        numPages = numResultRows/3

        ## Information Header
        searchResultInfoLabel = Label(loanToMemberSearchResultTable,
                                    text = "Books on Loan to Member: {0}"
                                        .format(booksOnLoanToMemberIdEntry.get()),
                                    font =("calibre", 20, "bold"),
                                    bg = "LightSteelBlue2")
        searchResultInfoLabel.place(x=0, y=0, width=1100, height=80);

        ########################
        ## Table Headers
        ########################
        ## Acc Num
        searchResultAccNumLabel = Label(loanToMemberSearchResultTable,
                                    text = "Accession Number",
                                    font =("calibre", 15, "bold"),
                                    bg = "LightSteelBlue1",
                                    wraplength=100,
                                    justify="center")
        searchResultAccNumLabel.place(x=20, y=100, width=150, height=80);

        ## Title 
        searchResultTitleLabel = Label(loanToMemberSearchResultTable,
                                    text = "Title",
                                    font =("calibre", 15, "bold"),
                                    bg = "LightSteelBlue1",
                                    wraplength=180,
                                    justify="center")
        searchResultTitleLabel.place(x=170, y=100, width=250, height=80);

        ## Author
        searchResultAuthorsLabel = Label(loanToMemberSearchResultTable,
                                    text = "Authors",
                                    font =("calibre", 15, "bold"),
                                    bg = "LightSteelBlue1",
                                    wraplength=180,
                                    justify="center")
        searchResultAuthorsLabel.place(x=420, y=100, width=250, height=80);

        ## ISBN
        searchResultISBNLabel = Label(loanToMemberSearchResultTable,
                                    text = "ISBN",
                                    font =("calibre", 15, "bold"),
                                    bg = "LightSteelBlue1",
                                    wraplength=100,
                                    justify="center")
        searchResultISBNLabel.place(x=670, y=100, width=150, height=80);

        ## Publisher
        searchResultPublisherLabel = Label(loanToMemberSearchResultTable,
                                    text = "Publisher",
                                    font =("calibre", 15, "bold"),
                                    bg = "LightSteelBlue1",
                                    wraplength=100,
                                    justify="center")
        searchResultPublisherLabel.place(x=820, y=100, width=150, height=80);

        ## Publishing Year
        searchResultPublisherLabel = Label(loanToMemberSearchResultTable,
                                    text = "Year",
                                    font =("calibre", 15, "bold"),
                                    bg = "LightSteelBlue1",
                                    wraplength=100,
                                    justify="center")
        searchResultPublisherLabel.place(x=970, y=100, width=110, height=80);

        ## Table rows here - 3 rows per page
        numResultsOnCurrPageOnwards = len(result)-(currentPage)*3
        tempTuple = ((result[0+currentPage*3]), ())
        resultsOnCurrPageList = list(tempTuple)

        if numResultsOnCurrPageOnwards >= 2:
            resultsOnCurrPageList.pop()
            resultsOnCurrPageList.append(result[1+currentPage*3])

        if numResultsOnCurrPageOnwards >= 3:
            resultsOnCurrPageList.append(result[2+currentPage*3])

        resultsOnCurrPage = tuple(resultsOnCurrPageList)
        #####################################
        ## Row 1
        #####################################
        if numResultsOnCurrPageOnwards >= 1:
            ## Acc Num
            searchResultRow1AccNumLabel = Label(loanToMemberSearchResultTable,
                                        text = resultsOnCurrPage[0][0],
                                        font =("calibre", 15, "bold"),
                                        bg = "GhostWhite",
                                        wraplength=100,
                                        justify="center")
            searchResultRow1AccNumLabel.place(x=20, y=180, width=150, height=80);

            ## Title 
            searchResultRow1TitleLabel = Label(loanToMemberSearchResultTable,
                                        text = resultsOnCurrPage[0][1],
                                        font =("calibre", 15, "bold"),
                                        bg = "GhostWhite",
                                        wraplength=180,
                                        justify="center")
            searchResultRow1TitleLabel.place(x=170, y=180, width=250, height=80);

            ## Author
            searchResultRow1AuthorsLabel = Label(loanToMemberSearchResultTable,
                                        text = resultsOnCurrPage[0][2],
                                        font =("calibre", 15, "bold"),
                                        bg = "GhostWhite",
                                        wraplength=180,
                                        justify="center")
            searchResultRow1AuthorsLabel.place(x=420, y=180, width=250, height=80);

            ## ISBN
            searchResultRow1ISBNLabel = Label(loanToMemberSearchResultTable,
                                        text = resultsOnCurrPage[0][3],
                                        font =("calibre", 15, "bold"),
                                        bg = "GhostWhite",
                                        wraplength=100,
                                        justify="center")
            searchResultRow1ISBNLabel.place(x=670, y=180, width=150, height=80);

            ## Publisher
            searchResultRow1PublisherLabel = Label(loanToMemberSearchResultTable,
                                        text = resultsOnCurrPage[0][4],
                                        font =("calibre", 15, "bold"),
                                        bg = "GhostWhite",
                                        wraplength=100,
                                        justify="center")
            searchResultRow1PublisherLabel.place(x=820, y=180, width=150, height=80);

            ## Publishing Year
            searchResultRow1PublisherLabel = Label(loanToMemberSearchResultTable,
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
        if numResultsOnCurrPageOnwards >= 2:
            searchResultRow2AccNumLabel = Label(loanToMemberSearchResultTable,
                                        text = resultsOnCurrPage[1][0],
                                        font =("calibre", 15, "bold"),
                                        bg = "GhostWhite",
                                        wraplength=100,
                                        justify="center")
            searchResultRow2AccNumLabel.place(x=20, y=260, width=150, height=80);

            ## Title 
            searchResultRow2TitleLabel = Label(loanToMemberSearchResultTable,
                                        text = resultsOnCurrPage[1][1],
                                        font =("calibre", 15, "bold"),
                                        bg = "GhostWhite",
                                        wraplength=180,
                                        justify="center")
            searchResultRow2TitleLabel.place(x=170, y=260, width=250, height=80);

            ## Author
            searchResultRow2AuthorsLabel = Label(loanToMemberSearchResultTable,
                                        text = resultsOnCurrPage[1][2],
                                        font =("calibre", 15, "bold"),
                                        bg = "GhostWhite",
                                        wraplength=180,
                                        justify="center")
            searchResultRow2AuthorsLabel.place(x=420, y=260, width=250, height=80);

            ## ISBN
            searchResultRow2ISBNLabel = Label(loanToMemberSearchResultTable,
                                        text = resultsOnCurrPage[1][3],
                                        font =("calibre", 15, "bold"),
                                        bg = "GhostWhite",
                                        wraplength=100,
                                        justify="center")
            searchResultRow2ISBNLabel.place(x=670, y=260, width=150, height=80);

            ## Publisher
            searchResultRow2PublisherLabel = Label(loanToMemberSearchResultTable,
                                        text = resultsOnCurrPage[1][4],
                                        font =("calibre", 15, "bold"),
                                        bg = "GhostWhite",
                                        wraplength=100,
                                        justify="center")
            searchResultRow2PublisherLabel.place(x=820, y=260, width=150, height=80);

            ## Publishing Year
            searchResultRow2PublisherLabel = Label(loanToMemberSearchResultTable,
                                        text = resultsOnCurrPage[1][5],
                                        font =("calibre", 15, "bold"),
                                        bg = "GhostWhite",
                                        wraplength=100,
                                        justify="center")
            searchResultRow2PublisherLabel.place(x=970, y=260, width=110, height=80);

        #####################################
        ## Row 3
        #####################################
        if numResultsOnCurrPageOnwards >= 3:
            ## Acc Num
            searchResultRow3AccNumLabel = Label(loanToMemberSearchResultTable,
                                        text = resultsOnCurrPage[2][0],
                                        font =("calibre", 15, "bold"),
                                        bg = "GhostWhite",
                                        wraplength=100,
                                        justify="center")
            searchResultRow3AccNumLabel.place(x=20, y=340, width=150, height=80);

            ## Title 
            searchResultRow3TitleLabel = Label(loanToMemberSearchResultTable,
                                        text = resultsOnCurrPage[2][1],
                                        font =("calibre", 15, "bold"),
                                        bg = "GhostWhite",
                                        wraplength=180,
                                        justify="center")
            searchResultRow3TitleLabel.place(x=170, y=340, width=250, height=80);

            ## Author
            searchResultRow3AuthorsLabel = Label(loanToMemberSearchResultTable,
                                        text = resultsOnCurrPage[2][2],
                                        font =("calibre", 15, "bold"),
                                        bg = "GhostWhite",
                                        wraplength=180,
                                        justify="center")
            searchResultRow3AuthorsLabel.place(x=420, y=340, width=250, height=80);

            ## ISBN
            searchResultRow3ISBNLabel = Label(loanToMemberSearchResultTable,
                                        text = resultsOnCurrPage[2][3],
                                        font =("calibre", 15, "bold"),
                                        bg = "GhostWhite",
                                        wraplength=100,
                                        justify="center")
            searchResultRow3ISBNLabel.place(x=670, y=340, width=150, height=80);

            ## Publisher
            searchResultRow3PublisherLabel = Label(loanToMemberSearchResultTable,
                                        text = resultsOnCurrPage[2][4],
                                        font =("calibre", 15, "bold"),
                                        bg = "GhostWhite",
                                        wraplength=100,
                                        justify="center")
            searchResultRow3PublisherLabel.place(x=820, y=340, width=150, height=80);

            ## Publishing Year
            searchResultRow3PublisherLabel = Label(loanToMemberSearchResultTable,
                                        text = resultsOnCurrPage[2][5],
                                        font =("calibre", 15, "bold"),
                                        bg = "GhostWhite",
                                        wraplength=100,
                                        justify="center")
            searchResultRow3PublisherLabel.place(x=970, y=340, width=110, height=80);


        ## Back Button
        searchResultBackButton = Button(loanToMemberSearchResultTable,
                                        text = "Back",
                                        font = ("calibre", 15, "bold"),
                                        fg = "grey39",
                                        bg = "snow3",
                                        command = closeSearchResultTable)
        searchResultBackButton.place(x=475, y=500, width=150, height=40)

    def searchForBooksOnLoanToMember():
        if len(booksOnLoanToMemberIdEntry.get()) == 0:
            messagebox.showerror(
                        "Input Error",
                        "Error: Please insert a MembershipId")
        else:
            result = sqlFuncs.booksLoanedToMemReport(booksOnLoanToMemberIdEntry.get())

            openSearchResultTable(result, 0)
    
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


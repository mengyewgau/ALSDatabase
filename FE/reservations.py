from email import message
from tkinter import *
from PIL import ImageTk, Image
from setuptools import Command
from tkinter import messagebox
import backendSQL as sqlFuncs

window = Tk()

####################################################################################################################################################################################
## Navigation stuff
def destroyReservationMenu():
    reservationMenu.destroy()

def destroyBookReservation():
    createBookReservation.destroy()

def destroyReservationConfirmDetailsPopUp():
    confirmReservationDetails.destroy()

def destroySuccessReservation():
    reserveSuccess.destroy()

def destroyCancelBookReservation():
    cancelBookReservation.destroy()

def destroyCancelConfirmDetailsPopUp():
    confirmCancellationDetails.destroy()

def destroySuccessCancel():
    cancelSuccess.destroy()    

def goReservationsMenuFromMakeReservation():
    reservationMenuWindow()
    destroyBookReservation()
    reservationMenu.lift()

def goReservationsMenuFromCancelReservation():
    reservationMenuWindow()
    destroyCancelBookReservation()
    reservationMenu.lift()

def goHome():
    landingPageFunc()
    destroyReservationMenu()
    landingPage.lift()

def openBookReservationMenuFunction():
    reservationMenu.destroy()
    openBookReservation()

def openReservationCancelMenuFunction():
    reservationMenu.destroy()
    openReservationCancellation()
####################################################################################################################################################################################
## Main Reservation Menu #################################################################
def reservationMenuWindow():
    global reservationMenu
    reservationMenu = Toplevel()
    reservationMenu.geometry("1280x820")
    reservationMenu.title("Reservations")
    
    ## Title Label
    reservationTitleLabel = Label(reservationMenu,
                                    text = "Select one of the Options below",
                                    font=("Arial, 20"),
                                    borderwidth=4,
                                    relief="solid",
                                    bg="paleturquoise1")
    reservationTitleLabel.place(x=140, y=0, width=1000, height=200)

    ## Picture
    global reservationsIm 
    reservationsIm = ImageTk.PhotoImage(Image.open("reserveIm.jpg"))
    displayReservationsIm = Label(reservationMenu, image=reservationsIm)
    displayReservationsIm.place(x=40, y=260, width=400, height=360) 

    ## Reserve A Book button
    reserveBookButton = Button(reservationMenu,
                                text="8. Reserve a\nBook",
                                font=("Arial, 14"),
                                bg="royalblue",
                                fg="white",
                                command=openBookReservationMenuFunction)
    reserveBookButton.place(x=480, y=280, width=180, height=160)

    reserveBookLabel = Label(reservationMenu,
                                text="Book Reservation",
                                anchor="w",
                                font=("Times", 14, "normal"))
    
    reserveBookLabel.place(x=680, y=280, width=600, height=180)

    ## Cancel Reservation button
    reservationCancelButton = Button(reservationMenu,
                                    text="9.Cancel \nReservation",
                                    font=("Arial, 14"),
                                    bg="royalblue",
                                    fg="white",
                                    command=openReservationCancelMenuFunction)
    reservationCancelButton.place(x=480, y=440, width=180, height=160)

    reservationCancelLabel = Label(reservationMenu, 
                                    text="Reservation Cancellation",
                                    anchor="w",
                                    font=('Times',14,'normal'))

    reservationCancelLabel.place(x=680, y=440, width=600, height=160)

    goMainFromReservationMenu = Button(reservationMenu,
                                  font=("Arial, 24"),
                                  text = "Back to Main Menu",
                                  bg="aquamarine",
                                  borderwidth = 4,
                                  relief = "solid",
                                  command=goHome)
    goMainFromReservationMenu.place(x=140,y=700, width=1000, height=80);

##########################################################################################
## Main Book Reservation Window ##########################################################
def openBookReservation():
    global createBookReservation
    createBookReservation = Toplevel()
    createBookReservation.geometry("1280x720")
    destroyReservationMenu()
    createBookReservation.lift()

    ###################################################################################################################
    ## Book Reservation - Create Confirmation and Error Handling ######################################################

    def reserveBook():
        try:
            result = sqlFuncs.confirmReservation(entryMemberID.get(),
                                entryAccessionNumber.get(),
                                entryDate.get())
            confirmReservationDetailsPopUpWindow(result)
        except Exception as excp :
            if excp.args[0] == "MemberId/Accesion Number fields are wrong!":
                messagebox.showerror("Reservation Error",
                                 "MembershipID/Accesion Number fields is/are wrong")
            else:
                messagebox.showerror("Reservation Error",
                                 "Member has outstanding Fine/Member has exceed reservation quota")
            

    ###################################################################################################################
    ## Confirm Reservation Details ####################################################################################
    def confirmReservationDetailsPopUpWindow(sqlResult):
        global confirmReservationDetails
        confirmReservationDetails = Toplevel()
        confirmReservationDetails.grab_set();
        confirmReservationDetails.geometry("450x400")
        confirmReservationDetails.configure(bg="chartreuse2")

        def confirmReserveBook():
            try:
                sqlFuncs.reserveBook(sqlResult[2], sqlResult[0], sqlResult[4])
                destroyReservationConfirmDetailsPopUp()
                reserveSuccessWindow()
                reserveSuccess.lift()
            except Exception as excp:
                if excp.args[0] == "Member has outstanding Fine":
                    fineAmount = sqlFuncs.checkFineValue(sqlResult[2])
                    messagebox.showerror("Reservation Error", "Member has Outstanding Fine of: ${0}".format(fineAmount))
                    destroyReservationConfirmDetailsPopUp()
                elif excp.args[0] == "Member has exceed reservation quota":
                    messagebox.showerror(
                        "Reservation Error",
                        "Member currently has 2 Books on Reservation")
                    destroyReservationConfirmDetailsPopUp()
                else:
                    messagebox.showerror("Reservation Error", "Member has already reserved the book")
                    destroyReservationConfirmDetailsPopUp()

        ## Title Label
        titleLabel = Label(confirmReservationDetails,
                            text="Please Confirm Details to Be Correct",
                            font=("Arial", 20, "bold"),
                            bg="chartreuse2",
                            wraplength=440)
        titleLabel.place(x=0, y=0, width=450, height=140)

        ## Accession Number Field
        accessionNumberLabel = Label(confirmReservationDetails,
                                text = "Accession Number: {0}".format(sqlResult[0]),
                                font=("Arial, 14"),
                                bg="chartreuse2",
                                anchor="w")
        accessionNumberLabel.place(x=50, y=100, width=380, height=40);
        ## Book Title Field
        bookTitleLabel = Label(confirmReservationDetails,
                        text = "Book Title: {0}".format(sqlResult[1]),
                        font=("Arial, 14"),
                        bg="chartreuse2",
                        anchor="w")
        bookTitleLabel.place(x=50, y=140, width=380, height=40);
        ## Membership ID Field
        memIDLabel = Label(confirmReservationDetails,
                        text = "Membership ID: {0}".format(sqlResult[2]),
                        font=("Arial, 14"),
                        bg="chartreuse2",
                        anchor="w")
        memIDLabel.place(x=50, y=180, width=380, height=40);
        ## Members Name Field
        memNameLabel = Label(confirmReservationDetails,
                        text = "Member Name: {0}".format(sqlResult[3]),
                        font=("Arial, 14"),
                        bg="chartreuse2",
                        anchor="w")
        memNameLabel.place(x=50, y=220, width=380, height=40);
        ## Reserve Date Field
        reserveDateLabel = Label(confirmReservationDetails,
                        text = "Reserve Date: {0}".format(sqlResult[4]),
                        font=("Arial, 14"),
                        bg="chartreuse2",
                        anchor="w")
        reserveDateLabel.place(x=50, y=260, width=380, height=40);

        ## Confirm Reservation
        confirmReservationButton = Button(confirmReservationDetails,
                                            text="Confirm \n Reservation",
                                            font=("Arial", 12,"bold"),
                                            borderwidth=6,
                                            bg="aquamarine",
                                            command=confirmReserveBook)
        confirmReservationButton.place(x=20, y=300, width=180, height=80)

        ## Return to reserve function
        returnTo = Button(confirmReservationDetails,
                        text="Back to \n Reserve \n Function",
                        font=("Arial", 12,"bold"),
                        borderwidth=6,
                        bg="aquamarine",
                        command=destroyReservationConfirmDetailsPopUp); 
        returnTo.place(x=250, y=300, width=180, height=80)

    ##########################################################################################
    ## Reserve Book Success Popup ############################################################
    def reserveSuccessWindow():
        global reserveSuccess
        reserveSuccess = Toplevel()
        reserveSuccess.configure(bg="chartreuse2")
        reserveSuccess.geometry("450x400")

        successTitle = Label(reserveSuccess,
                            text="Success!",
                            font=("Arial", 40,"bold"),
                            bg="chartreuse2",
                            fg="Black")
        successTitle.place(x=0, y=100, width=450, height=100)

        outcomeMsg = Label(reserveSuccess,
                            text="Reservation has been made",
                            font=("Arial", 16,"bold"),
                            bg="chartreuse2",
                            fg="black")
        outcomeMsg.place(x=0, y=200, width=450, height=100)

        returnButton = Button(reserveSuccess,
                                text="Back to \n Reserve \n Function",
                                font=("Arial", 12,"bold"),
                                borderwidth=8,
                                bg="aquamarine",
                                command=destroySuccessReservation)
        returnButton.place(x=125, y=300, width=200, height=80)
        
    ##########################################################################################
    ## Window design and placements ##########################################################
    ## Title Label 
    createBookReservationTitle = Label(createBookReservation,
                                        text="To Reserve a Book, Please Enter Information Below:",
                                        font=("Arial", 20, "bold"),
                                        bg="aquamarine")
    createBookReservationTitle.place(x=0, y=0, width=1280, height=150);

    ## Accession Number input field
    createReservationAccessionLabel = Label(createBookReservation,
                                text="Accession Number",
                                font =("calibre", 14, "bold"),
                                bg="DodgerBlue4",
                                fg="white")
    createReservationAccessionLabel.place(x=280, y=230, width=300, height=90);
    entryAccessionNumber = Entry(createBookReservation, font=('Arial',10,'italic'))
    entryAccessionNumber.place(x=620, y=260, width=450, height=30);

    ## Membership ID input field
    createMemberIDLabel = Label(createBookReservation,
                                text="Membership ID",
                                font =("calibre", 14, "bold"),
                                bg="DodgerBlue3",
                                fg="white")
    createMemberIDLabel.place(x=280, y=330, width=300, height=90);
    entryMemberID = Entry(createBookReservation, font=("Arial", 10, "italic"))
    entryMemberID.place(x=620, y=360, width=450, height=30)

    ## Reserve Date input field   
    createDateLabel = Label(createBookReservation,
                                text="Reserve date",
                                font =("calibre", 14, "bold"),
                                bg="DodgerBlue2",
                                fg="white")
    createDateLabel.place(x=280, y=430, width=300, height=90);
    entryDate = Entry(createBookReservation, font=("Arial", 10, "italic"))
    entryDate.place(x=620, y=460, width=450, height=30);
    ## Make Book Reservation Button
    makeBookReservation = Button(createBookReservation,
                        text="Reserve Book",
                        font=("Arial, 18"),
                        bg="aquamarine",
                        command=reserveBook)
    makeBookReservation.place(x=355, y=610, width=250, height=80);

    ## Back to Reservations Menu Button
    backToReservation = Button(createBookReservation,
                        text="Back to Reservations Menu",
                        font=("Arial, 18"),
                        bg="aquamarine",
                        wraplength=230,
                        command=goReservationsMenuFromMakeReservation)
    backToReservation.place(x=675, y=610, width=250, height=80);





##########################################################################################
## Main Reservation Cancellation Page ####################################################
def openReservationCancellation():
    global cancelBookReservation
    cancelBookReservation = Toplevel()
    cancelBookReservation.geometry("1280x720")
    destroyReservationMenu()
    cancelBookReservation.lift()

    ###################################################################################################################
    ## Reservation Cancellation - Create Confirmation and Error Handling ######################################################

    def cancelReservation():
        try:
            result = sqlFuncs.confirmCancel(entryMemberID.get(),
                                entryAccessionNumber.get(),
                                entryDate.get())
            confirmCancellationDetailsPopUpWindow(result)
        except Exception as excp :
            print(excp.args[0])
            messagebox.showerror("Cancellation Error", "Reservation does not exist")
            

    ##########################################################################################
    ## Comfirm canccellation details #########################################################
    def confirmCancellationDetailsPopUpWindow(sqlResult):
        global confirmCancellationDetails
        confirmCancellationDetails = Toplevel()
        confirmCancellationDetails.geometry("450x400")
        confirmCancellationDetails.configure(bg="chartreuse2")
        
        def confirmCancelReservation():
            try:
                sqlFuncs.cancelReservation(sqlResult[2], sqlResult[0])
                destroyCancelConfirmDetailsPopUp()
                cancelSuccessWindow()
                cancelSuccess.lift()
            except Exception as excp:
                destroyCancelConfirmDetailsPopUp()
                messagebox.showerror("Cancellation Error", "Reservation does not exist")

        ## Title Label
        titleLabel = Label(confirmCancellationDetails,
                            text="Please Confirm Details to Be Correct",
                            font=("Arial", 20, "bold"),
                            bg="chartreuse2",
                            wraplength=440)
        titleLabel.place(x=0, y=0, width=450, height=140)

        ## Accession Number Field
        cancelAccessionLabel = Label(confirmCancellationDetails,
                            text = "Accession Number: {0}".format(sqlResult[0]),
                            font=("Arial, 14"),
                            bg="chartreuse2",
                            anchor="w")
        cancelAccessionLabel.place(x=50, y=100, width=380, height=40)
        ## Book Title Field
        cancelBookTitleLabel = Label(confirmCancellationDetails,
                        text = "Book Title: {0}".format(sqlResult[1]),
                        font=("Arial, 14"),
                        bg="chartreuse2",
                        anchor="w")
        cancelBookTitleLabel.place(x=50, y=140, width=380, height=40)
        ## Membership ID Field
        cancelMemIDLabel = Label(confirmCancellationDetails,
                        text = "Membership ID: {0}".format(sqlResult[2]),
                        font=("Arial, 14"),
                        bg="chartreuse2",
                        anchor="w")
        cancelMemIDLabel.place(x=50, y=180, width=380, height=40)
        ## Member Name Field
        cancelNameLabel = Label(confirmCancellationDetails,
                        text = "Member Name: {0}".format(sqlResult[3]),
                        font=("Arial, 14"),
                        bg="chartreuse2",
                        anchor="w")
        cancelNameLabel.place(x=50, y=220, width=380, height=40)
        ## Cancellation Date Field
        cancelDateLabel = Label(confirmCancellationDetails,
                        text = "Cancellation Date: {0}".format(sqlResult[4]),
                        font=("Arial, 14"),
                        bg="chartreuse2",
                        anchor="w")
        cancelDateLabel.place(x=50, y=260, width=380, height=40)
        ## Confirm Cancellation
        confirmCancellationButton = Button(confirmCancellationDetails,
                                            text="Confirm \n Cancellation",
                                            font=("Arial", 12,"bold"),
                                            borderwidth=6,
                                            bg="aquamarine",
                                            command=confirmCancelReservation) 
        confirmCancellationButton.place(x=20, y=300, width=180, height=80)
        ## Return to Cancel function
        returnToCancel = Button(confirmCancellationDetails,
                        text="Back to \n Cancellation \n Function",
                        font=("Arial", 12,"bold"),
                        borderwidth=6,
                        bg="aquamarine",
                        command=destroyCancelConfirmDetailsPopUp)
        returnToCancel.place(x=250, y=300, width=180, height=80)

    ##########################################################################################
    ## Cancel Reservation Success Popup ######################################################
    def cancelSuccessWindow():
        global cancelSuccess
        cancelSuccess = Toplevel()
        cancelSuccess.configure(bg="chartreuse2")
        cancelSuccess.geometry("450x400")

        successTitle = Label(cancelSuccess,
                            text="Success!",
                            font=("Arial", 40,"bold"),
                            bg="chartreuse2",
                            fg="Black")
        successTitle.place(x=0, y=100, width=450, height=100)

        outcomeMsg = Label(cancelSuccess,
                            text="Reservation has been cancelled",
                            font=("Arial", 16,"bold"),
                            bg="chartreuse2",
                            fg="black")
        outcomeMsg.place(x=0, y=200, width=450, height=100)

        returnButton = Button(cancelSuccess,
                                text="Back to \n Cancellation \n Function",
                                font=("Arial", 12,"bold"),
                                borderwidth=8,
                                bg="aquamarine",
                                command=destroySuccessCancel)
        returnButton.place(x=125, y=300, width=200, height=80)


    ## Title Label
    cancelBookReservationTitle = Label(cancelBookReservation,
                                        text="To Cancel a Reservation, Please Enter Information Below:",
                                        font=("Arial, 18"),
                                        bg="aquamarine")
    cancelBookReservationTitle.place(x=0, y=0, width=1280, height=150)

    ## Accession Number input field
    cancelReservationAccessionLabel = Label(cancelBookReservation,
                                text="Accession Number",
                                font=("calibre", 14, "bold"),
                                bg="DodgerBlue3",
                                fg="white")
    cancelReservationAccessionLabel.place(x=280, y=230, width=300, height=90);
    entryAccessionNumber = Entry(cancelBookReservation, font=("Arial", 10, "italic"))
    entryAccessionNumber.place(x=620, y=260, width=450, height=30)

    ## Membership ID input field
    cancelMemberIDLabel = Label(cancelBookReservation,
                                text="Membership ID",
                                font=("calibre", 14, "bold"),
                                bg="DodgerBlue2",
                                fg="white")
    cancelMemberIDLabel.place(x=280, y=330, width=300, height=90);
    entryMemberID = Entry(cancelBookReservation, font=("Arial", 10, "italic"))
    entryMemberID.place(x=620, y=360, width=450, height=30)

    ## Reserve Date input field   
    cancelDateLabel = Label(cancelBookReservation,
                                text="Cancel date",
                                font=("calibre", 14, "bold"),
                                bg="DodgerBlue1",
                                fg="white")
    cancelDateLabel.place(x=280, y=430, width=300, height=90);
    entryDate = Entry(cancelBookReservation, font=("Arial", 10, "italic"))
    entryDate.place(x=620, y=460, width=450, height=30)    

    ## Cancel Book Reservation Button
    cancelBookReservationButton = Button(cancelBookReservation,
                                text="Cancel Reservation",
                                font=("Arial, 18"),
                                bg="aquamarine",
                                command=cancelReservation)
    cancelBookReservationButton.place(x=355, y=610, width=250, height=80);

    ## Back to Reservations Menu Button
    backToReservationButton = Button(cancelBookReservation,
                                text="Back to Reservations Menu",
                                font=("Arial, 18"),
                                bg="aquamarine",
                                wraplength=230,
                        command=goReservationsMenuFromCancelReservation)
    backToReservationButton.place(x=675, y=610, width=250, height=80);

## Dont delete - used to start the app
startButton = Button(window, text = "Start", command = reservationMenuWindow, fg = "lightblue",
                     bg = "black", font = ("Mincho", 20))
startButton.pack()

window.mainloop()

from tkinter import *
from PIL import ImageTk, Image
from setuptools import Command

window = Tk()


## Navigation stuff
def destroyReservationMenu():
    reservationMenu.destroy()

def destroyBookReservation():
    createBookReservation.destroy()

def destroyReservationConfirmDetailsPopUp():
    confirmReservationDetails.destroy()

def destroyReserveFail():
    reserveFail.destroy()

def destroySuccessReservation():
    reserveSuccess.destroy()

def destroyCancelBookReservation():
    cancelBookReservation.destroy()

def destroyCancelConfirmDetailsPopUp():
    confirmCancellationDetails.destroy()

def destroyCancelFail():
    cancelFail.destroy()

def destroySuccessCancel():
    cancelSuccess.destroy()    

def openBookReservation():
    createBookReservationWindow()
    destroyReservationMenu()
    createBookReservation.lift()

def goReservationsMenuFromMakeReservation():
    reservationMenuWindow()
    destroyBookReservation()
    reservationMenu.lift()

def openReservationCancellation():
    cancelBookReservationWindow();
    destroyReservationMenu()
    cancelBookReservation.lift()

def goReservationsMenuFromCancelReservation():
    reservationMenuWindow()
    destroyCancelBookReservation()
    reservationMenu.lift()
    

def goHome():
    window.destroy()
    import landingPage


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
                                text="8. Reserve a Book",
                                font=("Arial, 14"),
                                bg="LightBlue",
                                fg="white",
                                command=openBookReservation)
    reserveBookButton.place(x=480, y=280, width=180, height=160)

    reserveBookLabel = Label(reservationMenu,
                                text="Book Reservation",
                                anchor="w",
                                font=("Times", 14, "normal"))
    
    reserveBookLabel.place(x=680, y=280, width=600, height=180)

    ## Cancel Reservation button
    reservationCancelButton = Button(reservationMenu,
                                    text="9.Cancel Reservation",
                                    font=("Arial, 14"),
                                    bg="royalblue",
                                    fg="white",
                                    command=openReservationCancellation)
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

## Main Book Reservation Window
def createBookReservationWindow():
    global createBookReservation
    createBookReservation = Toplevel()
    createBookReservation.geometry("750x820")

    ## Title Label
    createBookReservationTitle = Label(createBookReservation,
                                        text="To Reserve a Book, Please Enter Information Below:",
                                        font=("Arial, 18"),
                                        bg="aquamarine")
    createBookReservationTitle.place(x=0, y=0, width=750, height=200)

    ## Accension Number input field
    createReservationAccensionLabel = Label(createBookReservation,
                                            text="Accension Number",
                                            font=("Arial, 10"),
                                            bg="DodgerBlue3",
                                            fg="white")
    createReservationAccensionLabel.place(x=0, y=200, width=300, height=100)
    entryAccensionNumber = Entry(createBookReservation, font=("Arial, 10"))
    entryAccensionNumber.place(x=300, y=260, width=450, height=40)

    ## Membership ID input field
    createMemberIDLabel = Label(createBookReservation,
                                text="Membership ID",
                                font=("Arial, 10"),
                                bg="DodgerBlue2",
                                fg="white")
    createMemberIDLabel.place(x=0, y=300, width=300, height=100)
    entryMemberID = Entry(createBookReservation, font=("Arial, 10"))
    entryMemberID.place(x=300, y=360, width=450, height=40)

    ## Reserve Date input field   
    createDateLabel = Label(createBookReservation,
                                text="Reserve date",
                                font=("Arial, 10"),
                                bg="DodgerBlue1",
                                fg="white")
    createDateLabel.place(x=0, y=400, width=300, height=100)
    entryDate = Entry(createBookReservation, font=("Arial, 10"))
    entryDate.place(x=300, y=460, width=450, height=40)    

    ## Make Book Reservation Button
    makeBookReservation = Button(createBookReservation,
                        text="Reserve Book",
                        font=("Arial, 18"),
                        bg="aquamarine",
                        command=confirmReservationDetailsPopUpWindow)
    makeBookReservation.place(x=80, y=710, width=250, height=80)

    ## Back to Reservations Menu Button
    backToReservation = Button(createBookReservation,
                        text="Back to Reservations Menu",
                        font=("Arial, 18"),
                        bg="aquamarine",
                        wraplength=230,
                        command=goReservationsMenuFromMakeReservation)
    backToReservation.place(x=420, y=710, width=250, height=80)


## Confirm Details
def confirmReservationDetailsPopUpWindow():
    global confirmReservationDetails
    confirmReservationDetails = Toplevel()
    confirmReservationDetails.geometry("450x400")
    confirmReservationDetails.configure(bg="chartreuse2")

    ## Title Label
    titleLabel = Label(confirmReservationDetails,
                        text="Please Confirm Details to Be Correct",
                        font=("Arial", 20, "bold"),
                        bg="chartreuse2",
                        wraplength=440)
    titleLabel.place(x=0, y=0, width=450, height=140)

     ## Membership Id Field
    memberIdLabel = Label(confirmReservationDetails,
                          text = "Membership ID (placeholder)",
                          font=("Arial, 14"),
                          bg="chartreuse2",
                          anchor="w")
    memberIdLabel.place(x=50, y=100, width=380, height=40);
    ## Membership Name Field
    nameLabel = Label(confirmReservationDetails,
                      text = "Name (placeholder)",
                      font=("Arial, 14"),
                      bg="chartreuse2",
                      anchor="w")
    nameLabel.place(x=50, y=140, width=380, height=40);
    ## Membership Faculty Input Field
    facLabel = Label(confirmReservationDetails,
                     text = "Faculty (placeholder)",
                     font=("Arial, 14"),
                     bg="chartreuse2",
                     anchor="w")
    facLabel.place(x=50, y=180, width=380, height=40);
    ## Membership Phone Input Field
    phoneLabel = Label(confirmReservationDetails,
                       text = "Phone (placeholder)",
                       font=("Arial, 14"),
                       bg="chartreuse2",
                       anchor="w")
    phoneLabel.place(x=50, y=220, width=380, height=40);
    ## Membership Faculty Input Field
    emailLabel = Label(confirmReservationDetails,
                       text = "Email (placeholder)",
                       font=("Arial, 14"),
                       bg="chartreuse2",
                       anchor="w")
    emailLabel.place(x=50, y=260, width=380, height=40);

    ## Confirm Reservation
    confirmReservationButton = Button(confirmReservationDetails,
                                        text="Confirm \n Reservation",
                                        font=("Arial", 12,"bold"),
                                        borderwidth=6,
                                        bg="aquamarine",
                                        command=reserveFailWindow) ##placeholder command
    confirmReservationButton.place(x=20, y=300, width=180, height=80)

    ## Return to reserve function
    returnTo = Button(confirmReservationDetails,
                      text="Back to \n Reserve \n Function",
                      font=("Arial", 12,"bold"),
                      borderwidth=6,
                      bg="aquamarine",
                      command=destroyReservationConfirmDetailsPopUp); 
    returnTo.place(x=250, y=300, width=180, height=80)

## Reserve Book Fail Popup
def reserveFailWindow():
    global reserveFail
    reserveFail = Toplevel()
    reserveFail.configure(bg="red")
    reserveFail.geometry("450x400")

    ## Error Title
    errorTitle = Label(reserveFail,
                        text = "Error!",
                        font=("Arial", 40,"bold"),
                        bg="red",
                        fg="yellow");
    errorTitle.place(x=0, y=100, width=450, height=100);

## error message needs fine amount if member has outstanding fine
    errorMsg = Label(reserveFail,
                        text = "Member currently has \n 2 books on Reservation; Member has Outstanding Fine of $X.", 
                        font=("Arial", 16,"bold"),
                        bg="red",
                        fg="yellow");
    errorMsg.place(x=0, y=200, width=450, height=100);    

    returnButton = Button(reserveFail,
                         text="Back to \n Reserve \n Function",
                         font=("Arial", 12,"bold"),
                         borderwidth=6,
                         bg="aquamarine",
                         command=destroyReserveFail);
    returnButton.place(x=125, y=300, width=200, height=80)


## Reserve Book Success Popup
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

## Main Reservation Cancellation Page
def cancelBookReservationWindow():
    global cancelBookReservation
    cancelBookReservation = Toplevel()
    cancelBookReservation.geometry("750x820")

    ## Title Label
    cancelBookReservationTitle = Label(cancelBookReservation,
                                        text="To Cancel a Reservation, Please Enter Information Below:",
                                        font=("Arial, 18"),
                                        bg="aquamarine")
    cancelBookReservationTitle.place(x=0, y=0, width=750, height=200)

    ## Accension Number input field
    cancelReservationAccensionLabel = Label(cancelBookReservation,
                                            text="Accension Number",
                                            font=("Arial, 10"),
                                            bg="DodgerBlue3",
                                            fg="white")
    cancelReservationAccensionLabel.place(x=0, y=200, width=300, height=100)
    entryAccensionNumber = Entry(cancelBookReservation, font=("Arial, 10"))
    entryAccensionNumber.place(x=300, y=260, width=450, height=40)

    ## Membership ID input field
    cancelMemberIDLabel = Label(cancelBookReservation,
                                text="Membership ID",
                                font=("Arial, 10"),
                                bg="DodgerBlue2",
                                fg="white")
    cancelMemberIDLabel.place(x=0, y=300, width=300, height=100)
    entryMemberID = Entry(cancelBookReservation, font=("Arial, 10"))
    entryMemberID.place(x=300, y=360, width=450, height=40)

    ## Reserve Date input field   
    cancelDateLabel = Label(cancelBookReservation,
                                text="Cancel date",
                                font=("Arial, 10"),
                                bg="DodgerBlue1",
                                fg="white")
    cancelDateLabel.place(x=0, y=400, width=300, height=100)
    entryDate = Entry(cancelBookReservation, font=("Arial, 10"))
    entryDate.place(x=300, y=460, width=450, height=40)    

    ## Back to Reservations Menu Button
    backToReservationButton = Button(cancelBookReservation,
                        text="Back to Reservations Menu",
                        font=("Arial, 18"),
                        bg="aquamarine",
                        wraplength=230,
                        command=goReservationsMenuFromCancelReservation)
    backToReservationButton.place(x=420, y=710, width=250, height=80)

    ## Cancel Book Reservation Button
    cancelBookReservationButton = Button(cancelBookReservation,
                        text="Cancel Reservation",
                        font=("Arial, 18"),
                        bg="aquamarine",
                        command=confirmCancellationDetailsPopUpWindow)
    cancelBookReservationButton.place(x=80, y=710, width=250, height=80)

def confirmCancellationDetailsPopUpWindow():
    global confirmCancellationDetails
    confirmCancellationDetails = Toplevel()
    confirmCancellationDetails.geometry("450x400")
    confirmCancellationDetails.configure(bg="chartreuse2")

    ## Title Label
    titleLabel = Label(confirmCancellationDetails,
                        text="Please Confirm Details to Be Correct",
                        font=("Arial", 20, "bold"),
                        bg="chartreuse2",
                        wraplength=440)
    titleLabel.place(x=0, y=0, width=450, height=140)

     ## Membership Id Field
    memberIdLabel = Label(confirmCancellationDetails,
                          text = "Membership ID (placeholder)",
                          font=("Arial, 14"),
                          bg="chartreuse2",
                          anchor="w")
    memberIdLabel.place(x=50, y=100, width=380, height=40)
    ## Membership Name Field
    nameLabel = Label(confirmCancellationDetails,
                      text = "Name (placeholder)",
                      font=("Arial, 14"),
                      bg="chartreuse2",
                      anchor="w")
    nameLabel.place(x=50, y=140, width=380, height=40)
    ## Membership Faculty Input Field
    facLabel = Label(confirmCancellationDetails,
                     text = "Faculty (placeholder)",
                     font=("Arial, 14"),
                     bg="chartreuse2",
                     anchor="w")
    facLabel.place(x=50, y=180, width=380, height=40)
    ## Membership Phone Input Field
    phoneLabel = Label(confirmCancellationDetails,
                       text = "Phone (placeholder)",
                       font=("Arial, 14"),
                       bg="chartreuse2",
                       anchor="w")
    phoneLabel.place(x=50, y=220, width=380, height=40)
    ## Membership Faculty Input Field
    emailLabel = Label(confirmCancellationDetails,
                       text = "Email (placeholder)",
                       font=("Arial, 14"),
                       bg="chartreuse2",
                       anchor="w")
    emailLabel.place(x=50, y=260, width=380, height=40)
    ## Confirm Cancellation with placeholder command
    confirmCancellationButton = Button(confirmCancellationDetails,
                                        text="Confirm \n Cancellation",
                                        font=("Arial", 12,"bold"),
                                        borderwidth=6,
                                        bg="aquamarine",
                                        command=cancelSuccessWindow) 
    confirmCancellationButton.place(x=20, y=300, width=180, height=80)
    ## Return to Cancel function
    returnToCancel = Button(confirmCancellationDetails,
                      text="Back to \n Cancellation \n Function",
                      font=("Arial", 12,"bold"),
                      borderwidth=6,
                      bg="aquamarine",
                      command=destroyCancelConfirmDetailsPopUp)
    returnToCancel.place(x=250, y=300, width=180, height=80)


## Cancel Reservation Fail Popup
def cancelFailWindow():
    global cancelFail
    cancelFail = Toplevel()
    cancelFail.configure(bg="red")
    cancelFail.geometry("450x400")

    ## Error Title
    errorTitle = Label(cancelFail,
                        text = "Error!",
                        font=("Arial", 40,"bold"),
                        bg="red",
                        fg="yellow");
    errorTitle.place(x=0, y=100, width=450, height=100);

    errorMsg = Label(cancelFail,
                        text = "Member has no such reservation.", 
                        font=("Arial", 16,"bold"),
                        bg="red",
                        fg="yellow");
    errorMsg.place(x=0, y=200, width=450, height=100);    

    returnButton = Button(cancelFail,
                         text="Back to \n Cancellation \n Function",
                         font=("Arial", 12,"bold"),
                         borderwidth=6,
                         bg="aquamarine",
                         command=destroyCancelFail);
    returnButton.place(x=125, y=300, width=200, height=80)


## Cancel Reservation Success Popup
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

## Dont delete - used to start the app
startButton = Button(window, text = "Start", command = reservationMenuWindow, fg = "lightblue",
                     bg = "black", font = ("Mincho", 20))
startButton.pack()

window.mainloop()

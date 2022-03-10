
from tkinter import *
from PIL import ImageTk, Image


window = Tk()

## Navigation stuff
def destroyFinesMenu():
    finesMenu.destroy()

def destroyFinePaymentMenu():
    finePaymentMenu.destroy()

def destroyConfirmPaymentDetails():
    confirmPaymentDetails.destroy()

def destroyPaymentSuccessPopup():
    paymentSuccess.destroy()

def destroyPaymentFailPopup():
    paymentFail.destroy()

def openFinePaymentWindow():
    finePaymentMenuWindow()
    destroyFinesMenu()
    finePaymentMenu.lift()

def openPaymentSuccessPopup():
    paymentSuccessPopup()
    destroyConfirmPaymentDetails()
    paymentSuccess.lift()

def openPaymentFailPopup():
    paymentFailPopup()
    destroyConfirmPaymentDetails()
    paymentFail.lift()


def goHome():
    window.destroy()
    import landingPage

def goToFinesMenuFromFinePayment():
    finesMenuWindow()
    destroyFinePaymentMenu()
    finesMenu.lift()


## Fine menu
def finesMenuWindow():
    global finesMenu
    finesMenu = Toplevel()
    finesMenu.geometry("1280x820")
    finesMenu.title("Fines")

    ## Title
    finesTitleLabel = Label(finesMenu,
                             text = "Select one of the Options below:",
                             font=("Arial, 20"),
                             borderwidth = 4,
                             relief = "solid",
                             bg="paleturquoise1");
    finesTitleLabel.place(x=140, y=0, width=1000, height=200);

    ## Picture Left Side
    global finesIm
    finesIm = ImageTk.PhotoImage(Image.open("fineIm.jpg").resize((400,360)))
    displayImg = Label(finesMenu, image=finesIm);
    displayImg.place(x=40, y=260, width=400, height=360);

    ## Fine Payment Button
    finePaymentButton = Button(finesMenu,
                                text="10. Payment",
                                font=("Arial, 14"),
                                bg="LightBlue",
                                fg="white",
                                command=openFinePaymentWindow)
    finePaymentButton.place(x=600, y=350, width=600, height=180)

    ## main menu button
    goMainFromMemMenu = Button(finesMenu,
                                  font=("Arial, 24"),
                                  text = "Back to Main Menu",
                                  bg="aquamarine",
                                  borderwidth = 4,
                                  relief = "solid",
                                  command=goHome)
    goMainFromMemMenu.place(x=140,y=700, width=1000, height=80);

## Fine Payment Menu

def finePaymentMenuWindow():
    global finePaymentMenu
    finePaymentMenu = Toplevel()
    finePaymentMenu.geometry("750x820")
    finePaymentMenu.title("Fine Payment")

    ## Title Label
    paymentTitleLabel = Label(finePaymentMenu,
                                text = "To Pay a Fine, Please Enter Information Below:",
                                font=("Arial, 18"),
                                bg="aquamarine");
    paymentTitleLabel.place(x=0, y=0, width=750, height=200);

    ## Membership Id Input Field
    paymentMemberIdLabel = Label(finePaymentMenu,
                                   text = "Membership ID",
                                   font=("Arial, 10"),
                                   bg="DodgerBlue3",
                                   fg="white")
    paymentMemberIdLabel.place(x=0, y=200, width=300, height=100);
    entryMemberId = Entry(finePaymentMenu,font=('Arial',10,'normal'))
    entryMemberId.place(x=300, y=260, width=450, height=40);

    ## Payment Date Input Field
    paymentDateLabel = Label(finePaymentMenu,
                               text = "Payment Date",
                               font=("Arial, 10"),
                               bg="DodgerBlue2",
                               fg="white")
    paymentDateLabel.place(x=0, y=300, width=300, height=100);
    entryDate = Entry(finePaymentMenu, font=('Arial',10,'normal'))
    entryDate.place(x=300, y=360, width=450, height=40);


    ## Payment Amount Input Field
    paymentAmountLabel = Label(finePaymentMenu,
                              text = "Payment Amount",
                              font=("Arial, 10"),
                              bg="SkyBlue2",
                              fg="white")
    paymentAmountLabel.place(x=0, y=400, width=300, height=100);
    entryPayment = Entry(finePaymentMenu, font=('Arial',10,'normal'))
    entryPayment.place(x=300, y=460, width=450, height=40);

    ## Membership Creation Button
    payFineButton = Button(finePaymentMenu,
                                   text = "Pay Fine",
                                   font=("Arial, 18"),
                                   bg="aquamarine",
                                   command=confirmPaymentDetailsPopup)
    payFineButton.place(x=80, y=710, width=250, height=80);
    ## Return to Main Menu Button
    backButton = Button(finePaymentMenu,
                           text = "Back to Fines Menu",
                           font=("Arial, 18"),
                           bg="aquamarine",
                           command=goToFinesMenuFromFinePayment)
    backButton.place(x=420, y=710, width=250, height=80);


## Confirm Fine Payment Details Popup
def confirmPaymentDetailsPopup():
    global confirmPaymentDetails
    confirmPaymentDetails = Toplevel()
    confirmPaymentDetails.configure(bg="chartreuse2")
    confirmPaymentDetails.geometry("450x400")

    ## Title Label
    titleLabel = Label(confirmPaymentDetails,
                       text = "Please Confirm Details to \n Be Correct",
                       font=("Arial", 20, "bold"),
                       bg="chartreuse2")
    titleLabel.place(x=0, y=0, width=450, height=140);

    ## Payment Due Field
    memberIdLabel = Label(confirmPaymentDetails,
                          text = "Payment Due: (placeholder)",
                          font=("Arial, 14"),
                          bg="chartreuse2",
                          anchor="w")
    memberIdLabel.place(x=50, y=100, width=380, height=40)
    ## Member ID Field
    nameLabel = Label(confirmPaymentDetails,
                      text = "Member ID (placeholder)",
                      font=("Arial, 14"),
                      bg="chartreuse2",
                      anchor="w")
    nameLabel.place(x=50, y=140, width=380, height=40)
    ## Payment Date Field
    facLabel = Label(confirmPaymentDetails,
                     text = "Payment Date (placeholder)",
                     font=("Arial, 14"),
                     bg="chartreuse2",
                     anchor="w")
    facLabel.place(x=50, y=180, width=380, height=40)
    ## Exact Fee Only Field
    phoneLabel = Label(confirmPaymentDetails,
                       text = "Exact Fee Only",
                       font=("Arial, 14"),
                       bg="chartreuse2",
                       anchor="w")
    phoneLabel.place(x=50, y=220, width=380, height=40)

    ## Confirm Payment Button
    confirmFinePaymentButton = Button(confirmPaymentDetails,
                                        text="Confirm \n Payment",
                                        font=("Arial", 12,"bold"),
                                        borderwidth=6,
                                        bg="aquamarine",
                                        command=openPaymentSuccessPopup)
    confirmFinePaymentButton.place(x=20, y=300, width=180, height=80)
    ## Back to Payment Function
    returnToPaymentFunction = Button(confirmPaymentDetails,
                                    text="Back to \n Payment \n Function",
                                    font=("Arial", 12,"bold"),
                                    borderwidth=6,
                                    bg="aquamarine",
                                    command=destroyConfirmPaymentDetails)
    returnToPaymentFunction.place(x=250, y=300, width=180, height=80)


## Fine Payment Error Page
def paymentFailPopup():
    global paymentFail
    paymentFail = Toplevel()
    paymentFail.configure(bg="red")
    paymentFail.geometry("450x400")

    ## Successs Title Label
    successTitle = Label(paymentFail,
                        text = "Error!",
                        font=("Arial", 40,"bold"),
                        bg="red",
                        fg="yellow")
    successTitle.place(x=0, y=100, width=450, height=100)

    ## Success Message Label
    successMsg = Label(paymentFail,
                        text = "Member has no fine. \n Incorrect fine payment amount.",
                        font=("Arial", 16,"bold"),
                        bg="red",
                        fg="yellow")
    successMsg.place(x=0, y=200, width=450, height=100)

    ## Return to Payment Function
    returnToPaymentFunction = Button(paymentFail,
                                    text="Back to \n Payment \n Function",
                                    font=("Arial", 12,"bold"),
                                    borderwidth=6,
                                    bg="aquamarine",
                                    command=destroyPaymentFailPopup)
    returnToPaymentFunction.place(x=125, y=300, width=200, height=80)

## Fine Payment Success Page
def paymentSuccessPopup():
    global paymentSuccess
    paymentSuccess = Toplevel()
    paymentSuccess.configure(bg="chartreuse2")
    paymentSuccess.geometry("450x400")

    ## Successs Title Label
    successTitle = Label(paymentSuccess,
                        text = "Success!",
                        font=("Arial", 40,"bold"),
                        bg="chartreuse2",
                        fg="Black")
    successTitle.place(x=0, y=100, width=450, height=100)

    ## Success Message Label
    successMsg = Label(paymentSuccess,
                        text = "Fine has been fully paid.",
                        font=("Arial", 16,"bold"),
                        bg="chartreuse2",
                        fg="black")
    successMsg.place(x=0, y=200, width=450, height=100)

    ## Return to Payment Function
    returnToPaymentFunction = Button(paymentSuccess,
                                    text="Back to \n Payment \n Function",
                                    font=("Arial", 12,"bold"),
                                    borderwidth=6,
                                    bg="aquamarine",
                                    command=destroyPaymentSuccessPopup)
    returnToPaymentFunction.place(x=125, y=300, width=200, height=80)


## Dont delete - used to start the app
startButton = Button(window, text = "Start", command = finesMenuWindow, fg = "lightblue",
                     bg = "black", font = ("Mincho", 20))
startButton.pack()
window.mainloop()

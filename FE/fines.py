from tkinter import *
from PIL import ImageTk, Image
import backendSQL as sqlFuncs
from tkinter import messagebox
window = Tk()
########################################################################################################################################################################################################################
## Navigation stuff
def destroyfineMainMenu():
    fineMainMenu.destroy()

def goHome():
    landingPageFunc()
    destroyfineMainMenu()
    landingPage.lift()

def goTofineMainMenuFromFinePayment():
    fineMainMenuFunction()
    destroyFinePaymentMenu()
    fineMainMenu.lift()
def destroyFinePaymentMenu():
    finePaymentMenu.destroy();
def openFinePaymentWindow():
    fineMainMenu.destroy()
    finePaymentMenuFunction();
########################################################################################################################################################################################################################
## Fine menu
def fineMainMenuFunction():
    global fineMainMenu
    fineMainMenu = Toplevel()
    fineMainMenu.geometry("1280x820")
    fineMainMenu.title("Fines")

    ## Title
    finesTitleLabel = Label(fineMainMenu,
                             text = "Select one of the Options below:",
                             font=("Arial, 20"),
                             borderwidth = 4,
                             relief = "solid",
                             bg="paleturquoise1");
    finesTitleLabel.place(x=140, y=0, width=1000, height=200);

    ## Picture Left Side
    global finesIm
    finesIm = ImageTk.PhotoImage(Image.open("fineIm.jpg").resize((400,360)))
    displayImg = Label(fineMainMenu, image=finesIm);
    displayImg.place(x=40, y=260, width=400, height=360);

    ## Fine Payment Button
    finePaymentButton = Button(fineMainMenu,
                                text="10. Payment",
                                font=("Arial, 14"),
                                bg="LightBlue",
                                fg="white",
                                command=openFinePaymentWindow)
    finePaymentButton.place(x=600, y=350, width=600, height=180)

    ## main menu button
    goMainFromMemMenu = Button(fineMainMenu,
                                  font=("Arial, 24"),
                                  text = "Back to Main Menu",
                                  bg="aquamarine",
                                  borderwidth = 4,
                                  relief = "solid",
                                  command=goHome)
    goMainFromMemMenu.place(x=140,y=700, width=1000, height=80);
    
########################################################################################################################################################################################################################
### Fines 1 - Payment Menu ############################################################################################################################################################################################################
def finePaymentMenuFunction():    
    global finePaymentMenu
    finePaymentMenu = Toplevel()
    finePaymentMenu.grab_set()
    finePaymentMenu.title("Member Fine Payment Menu")
    finePaymentMenu.geometry("1280x720")

###################################################################################################################################################################################################################  
    ### Fines 1.1 - Link Fine Payment to backend
    def closeConfirmFinePaymentDialog():
        finePaymentMenu.lift();
        paymentConfirmDialog.destroy();
    def confirmFinePmt():
        try:
            result = sqlFuncs.confirmFinePayment(entryMemberID.get(), entryDate.get())
            openPayFineDialog(result)
        except:
            messagebox.showerror("Fine Payment Error",
                                 "Fields are empty/incorrect")
###################################################################################################################################################################################################################  
    ### Fines 1.2 - Fines Confirmation Dialog
    def openPayFineDialog(sqlResult):
        global paymentConfirmDialog
        paymentConfirmDialog = Toplevel();
        paymentConfirmDialog.grab_set();
        paymentConfirmDialog.title("Confirm Fine Payment");
        paymentConfirmDialog.geometry("750x800")
        paymentConfirmDialog.configure(bg = "limegreen")

        def payFineFunction():
            try:
                sqlFuncs.payFine(sqlResult[1], sqlResult[3], int(paidAmtEntry.get()));
                openPaymentSuccessDialog();
            except Exception as excp:
                if excp.args[0]=="Member has no fine":
                    messagebox.showerror("Fine Payment Error",
                                         "Member has no fine")
                elif excp.args[0] == "Incorrect fine payment amount.":
                    messagebox.showerror("Fine Payment Error!",
                                        "Incorrect fine payment amount.")
                else:
                    messagebox.showerror("Debug")
###################################################################################################################################################################################################################  
        ## Payment confirmation dialog Design
        paymentConfirmTitleLabel = Label(paymentConfirmDialog,
                                    text="Please Confirm Details to \nBe Correct",
                                    font=("Arial",24,"bold"),
                                    bg="LightSteelBlue2")
        paymentConfirmTitleLabel.place(x=0, y=0, width=750, height=100);

        # Payment Due Field
        paymentDueLabel = Label(paymentConfirmDialog,
                                    text = "Payment Due: \n{0}".format(sqlResult[0]),
                                    font = ("calibre", 15),
                                    anchor="nw",
                                    bg = "SkyBlue2")
        paymentDueLabel.place(x=125, y=100, width=350, height=180)
        # Membership Id Field
        paymentConfirmMemIdLabel = Label(paymentConfirmDialog,
                                    text = "Member \nID: \n{0}".format(sqlResult[1]),
                                    font = ("calibre", 15),
                                    anchor="nw",
                                    bg = "SkyBlue2")
        paymentConfirmMemIdLabel.place(x=475, y=100, width=150, height=180)
        # Exact Fee Only Field
        exactFeeLabel = Label(paymentConfirmDialog,
                                    text = "{0}".format(sqlResult[2]),
                                    font = ("calibre", 15),
                                    anchor="nw",                                  
                                    bg = "SkyBlue2")
        exactFeeLabel.place(x=125, y=300, width=350, height=180)
        # Payment Date Field
        paymentConfirmLabel = Label(paymentConfirmDialog,
                                    text = "Payment \nDate: \n {0}".format(sqlResult[3]),
                                    font = ("calibre", 15),
                                    anchor="nw",
                                    bg = "SkyBlue2")
        paymentConfirmLabel.place(x=475, y=300, width=150, height=180)
        ## Confirm Payment Button
        paymentConfirmButton = Button(paymentConfirmDialog,
                                    text = "Confirm\nPayment",
                                    font = ("Arial", 20, "bold"),
                                    fg = "ghost white",
                                    bg = "magenta2",
                                    command = payFineFunction)
        paymentConfirmButton.place(x=200, y=700, width=150, height=80)
        
        ## Close Return Button
        paymentCloseButton = Button(paymentConfirmDialog,
                                    text = "Back to\nPayment\nFunction",
                                    font = ("Arial", 15, "bold"),
                                    fg = "ghost white",
                                    bg = "magenta2",
                                    command = closeConfirmFinePaymentDialog)
        paymentCloseButton.place(x=400, y=700, width=150, height=80)
###################################################################################################################################################################################################################  
    ## Fine 1.3 - Payment Success Popup
    def closePaymentSuccessDialog():
        finePaymentMenu.lift();
        paymentSuccessDialog.destroy();
    def openPaymentSuccessDialog():
        paymentConfirmDialog.destroy();
        global paymentSuccessDialog
        paymentSuccessDialog = Toplevel();
        paymentSuccessDialog.grab_set() ## Make sure only top level window is editable
        paymentSuccessDialog.configure(bg="limegreen")
        paymentSuccessDialog.geometry("450x400")
        ## Error Title Label
        errorTitle = Label(paymentSuccessDialog,
                            text = "Success! \n\n Fine Paid!",
                            font=("Arial", 18,"bold"),
                            bg="limegreen",
                            fg="Black");
        errorTitle.place(x=0, y=100, width=450, height=100);
        ## return Button
        returnButton = Button(paymentSuccessDialog,
                            text="Back to \n Fine \n Payment",
                            font=("Arial", 12,"bold"),
                            borderwidth=8,
                            bg="aquamarine",
                            command=closePaymentSuccessDialog);
        returnButton.place(x=125, y=300, width=200, height=80)
###################################################################################################################################################################################################################  
    ### Fines 1.4 - Design and Placement
    ## Title Label
    finePaymentTitle = Label(finePaymentMenu,
                                        text="To Pay a Fine, Please Enter Information Below:",
                                        font=("Arial, 18"),
                                        bg="aquamarine")
    finePaymentTitle.place(x=0, y=0, width=1280, height=150)
    ## Membership ID input field
    finePaymentMemberIDLabel = Label(finePaymentMenu,
                                text="Membership ID",
                                font=("calibre", 14, "bold"),
                                bg="DodgerBlue3",
                                fg="white")
    finePaymentMemberIDLabel.place(x=280, y=230, width=300, height=90);
    entryMemberID = Entry(finePaymentMenu, font=("Arial", 10, "italic"))
    entryMemberID.place(x=620, y=260, width=450, height=30)
    ## Paid Date input field
    finePaymentDateLabel = Label(finePaymentMenu,
                                text="Payment Date \n(YYYY/MM/DD)",
                                font=("calibre", 14, "bold"),
                                bg="DodgerBlue2",
                                fg="white")
    finePaymentDateLabel.place(x=280, y=330, width=300, height=90);
    entryDate = Entry(finePaymentMenu, font=("Arial", 10, "italic"))
    entryDate.place(x=620, y=360, width=450, height=30)

    ## Payment Amount input field   
    finePaidAmtLabel = Label(finePaymentMenu,
                                text="Payment Amount",
                                font=("calibre", 14, "bold"),
                                bg="DodgerBlue1",
                                fg="white")
    finePaidAmtLabel.place(x=280, y=430, width=300, height=90);
    paidAmtEntry = Entry(finePaymentMenu, font=("Arial", 10, "italic"))
    paidAmtEntry.place(x=620, y=460, width=450, height=30)    

    ## Pay Fine Button
    payFineButton = Button(finePaymentMenu,
                                text="Pay Fine",
                                font=("Arial, 18"),
                                bg="aquamarine",
                                command=confirmFinePmt)
    payFineButton.place(x=355, y=610, width=250, height=80);

    ## Back to Fine Main Menu Button
    backToFineMainMenuButton = Button(finePaymentMenu,
                                text="Back to Fines Menu",
                                font=("Arial, 18"),
                                bg="aquamarine",
                                wraplength=230,
                        command=goTofineMainMenuFromFinePayment)
    backToFineMainMenuButton.place(x=675, y=610, width=250, height=80);
###################################################################################################################################################################################################################  
## Dont delete - used to start the app
startButton = Button(window, text = "Start", command = fineMainMenuFunction, fg = "lightblue",
                     bg = "black", font = ("Mincho", 20))
startButton.pack()
window.mainloop()

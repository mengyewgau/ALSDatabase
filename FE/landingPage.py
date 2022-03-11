from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import backendSQL as sqlFuncs
from datetime import datetime



## Sequence of Features:
## Membership (Line 113-759)
## Books (Line 770-1369)
## Loans (Line 1403 - 1844)
## Reservation (Lines 1849-2354)
## Fines (Lines 2363-2605)
## Reports  (Lines 2612-4398)

### LANDING PAGE FUNCTIONS ###
def destroyLandingPage(): 
    landingPage.destroy();

def landingPageFunc():
    global landingPage
    landingPage = Toplevel()
    landingPage.title("Landing Page")
    landingPage.geometry("1280x720")
    
    def openMembership():
        membershipMenu()
        destroyLandingPage()
        memMenu.lift()

    def openBooks():
        createBookMenu()
        destroyLandingPage()
        bookMenu.lift()

    def openLoans():
        loansMenuFunc()
        destroyLandingPage()
        loansMenu.lift()

    def openReserv():
        reservationMenuWindow()
        destroyLandingPage()
        reservationMenu.lift()
    
    def openFines():
        fineMainMenuFunction()
        destroyLandingPage()
        fineMainMenu.lift()

    def openReport():
        reportsMenuFunc()
        destroyLandingPage()
        reportsMenu.lift()


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
                             command=openMembership)
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
                            command=openBooks)
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
                            command=openLoans)
    buttonLoans.place(x=830, y=325, width=250, height=50)

    ## Second row, leftmost button and icon
    global reserveIm
    reserveIm = ImageTk.PhotoImage(Image.open("reserveIm.jpg").resize((250,200)))
    displayResIm = Label(landingPage, image=reserveIm);
    displayResIm.place(x=200, y=410, width=250, height=200);

    buttonReservation = Button(landingPage,
                                  text = "Reservation",
                                  font=("Arial, 18"),
                                  bg="darkseagreen",
                                  command=openReserv)
    buttonReservation.place(x=200, y=615, width=250, height=50)

    ## Second row, middle button and icon
    global fineIm
    fineIm = ImageTk.PhotoImage(Image.open("fineIm.jpg").resize((250,200)))
    displayFineIm = Label(landingPage, image=fineIm);
    displayFineIm.place(x=515, y=410, width=250, height=200);

    buttonFines = Button(landingPage,
                            text = "Fines",
                            font=("Arial, 18"),
                            bg="cadetblue",
                            command=openFines)
    buttonFines.place(x=515, y=615, width=250, height=50)


    ## Second row, rightmost button and icon
    global reportIm
    reportIm = ImageTk.PhotoImage(Image.open("reportIm.jpg").resize((250,200)))
    displayReportIm = Label(landingPage, image=reportIm);
    displayReportIm.place(x=830, y=410, width=250, height=200);

    buttonReports = Button(landingPage,
                              text = "Reports",
                              font=("Arial, 18"),
                              bg="peru",
                              command=openReport)
    buttonReports.place(x=830, y=615, width=250, height=50)

################################################
## MEMBERSHIP FUNCTIONS BELOW ##
################################################
### Naviagtion Functions #####################################################################################################################################################################################################################################
# Navigation in Membership Menu
def destroyMemMenu(): # Ensure Membership Window is destroyed
    memMenu.destroy();
def navFromMemToCreateMem(): # Go to CreateMem
    memberCreation();
    destroyMemMenu();
    createMemMenu.lift()
def navFromMemToDelMem(): # Go to deleteMem
    memberDeletion()
    destroyMemMenu();
    deleteMemMenu.lift()
def navFromMemToUpdateMem(): # Go to updateMem
    updateMemMenu();
    destroyMemMenu();
    updateInputId.lift()
def navReturnToMain(): # Return to Main Menu
    landingPageFunc()
    destroyMemMenu()
    landingPage.lift()


# Navigation in Create Menus
def destroyCreateMenu():
    createMemMenu.destroy();
def navFromCreateToMemMenu(): # Return to Main Menu
    membershipMenu();
    destroyCreateMenu()
    memMenu.lift()
 
# Navigation in Delete Menus
def destroyDeleteMenu():
    deleteMemMenu.destroy();
def navFromDeleteToMemMenu(): # Return to Membership Menu
    membershipMenu();
    destroyDeleteMenu();
    memMenu.lift()
    
# Navigation in Update Menus
def destroyUpdateLandingMenu():
    updateInputId.destroy();
def navReturnToMemMenuFromUpdateLanding(): # Return to Membership Menu
    membershipMenu();
    destroyUpdateLandingMenu();
    memMenu.lift()
#####################################################################################################################################################################################################################################
### Main Membership Menu ############################################################################################################################################################################################################
def membershipMenu(): 
    global memMenu
    memMenu = Toplevel();
    memMenu.grab_set();
    memMenu.geometry("1280x820")

    ## Title Label
    memTitleLabel = Label(memMenu,
                          text = "Select one of the Options below:",
                          font=("Arial, 20"),
                          borderwidth = 4,
                          relief = "solid",
                          bg="paleturquoise1");
    memTitleLabel.place(x=140, y=0, width=1000, height=200);

    ## Picture Left Side
    global createIm
    createIm = ImageTk.PhotoImage(Image.open("als.jpg").resize((400,360)))
    displayImg = Label(memMenu, image=createIm);
    displayImg.place(x=40, y=260, width=400, height=360);
    ## Go to member creation menu
    memCreationButton = Button(memMenu,
                               text = "1. Creation",
                               font=("Arial, 14"),
                               bg="LightBlue",
                               fg="white",
                               command=navFromMemToCreateMem)
    memCreationButton.place(x=480, y=200, width=180, height=160);
    memCreationLabel = Label(memMenu,
                                text="Membership creation",
                                anchor = "w",
                                font=('Times',14,'normal'))
    memCreationLabel.place(x=680, y=200, width=600, height=180);
    ## Go to member deletion menu
    memDeletionButton = Button(memMenu,
                                  text = "2. Deletion",
                                  font=("Arial, 14"),
                                  bg="royalblue",
                                  fg="white",
                                  command=navFromMemToDelMem)
    memDeletionButton.place(x=480, y=360, width=180, height=160);
    memDeletionLabel = Label(memMenu,
                                text="Membership deletion",
                                anchor = "w",
                                font=('Times',14,'normal'))
    memDeletionLabel.place(x=680, y=360, width=600, height=160);
    ## Go to member update menu
    memUpdateButton = Button(memMenu,
                             text = "3. Update",
                             font=("Arial, 14"),
                             bg="SlateBlue",
                             fg="white",
                             command=navFromMemToUpdateMem)
    memUpdateButton.place(x=480, y=520, width=180, height=160);
    memUpdateLabel = Label(memMenu,
                              text="Membership update",
                              anchor = "w",
                              font=('Times',14,'normal'))
    memUpdateLabel.place(x=680, y=520, width=600, height=160);

    goMainFromMemMenu = Button(memMenu,
                                  font=("Arial, 24"),
                                  text = "Back to Main Menu",
                                  bg="aquamarine",
                                  borderwidth = 4,
                                  relief = "solid",
                                  command=navReturnToMain)
    goMainFromMemMenu.place(x=140,y=700, width=1000, height=80);
### Membership 1 - Creation ############################################################################################################################################################################################################
def memberCreation(): 
    global createMemMenu
    createMemMenu = Toplevel()
    createMemMenu.title("Create a Member")
    createMemMenu.geometry("1280x720")

    ###################################################################################################################
    ## Membership 1.1 - Create Confirmation and Error Handling
    def closeCreateMemSuccessDialog():
        createMemMenu.lift()
        createMemSuccessDialog.destroy()
    def createMemberFunc():
##        try:
        sqlFuncs.createMember(entryMemberId.get(),
                                entryName.get(),
                                entryFac.get(),
                                entryPhone.get(),
                                entryEmail.get());
        openCreateMemberSuccessDialog();
##        except Exception as excp:
##            messagebox.showerror("Member Creation Error",
##                                 "Member already exist; Missing or\n Incomplete fields.")
    ###################################################################################################################
    ## Membership 1.2 - Creation Windows and Popups
    def openCreateMemberSuccessDialog():
        global createMemSuccessDialog
        createMemSuccessDialog = Toplevel();
        createMemSuccessDialog.grab_set() ## Make sure only top level window is editable
        createMemSuccessDialog.configure(bg="limegreen")
        createMemSuccessDialog.geometry("450x400")
        ## Error Title Label
        errorTitle = Label(createMemSuccessDialog,
                            text = "Success! \n\n ALS Membership created.",
                            font=("Arial", 18,"bold"),
                            bg="limegreen",
                            fg="Black");
        errorTitle.place(x=0, y=100, width=450, height=100);
        ## return Button
        returnButton = Button(createMemSuccessDialog,
                             text="Back to \n Create \n Function",
                             font=("Arial", 12,"bold"),
                             borderwidth=8,
                             bg="aquamarine",
                             command=closeCreateMemSuccessDialog);
        returnButton.place(x=125, y=300, width=200, height=80)
    ###################################################################################################################  
    ## Membership 1.3 - Design and Placement
    # Title Label
    createTitleLabel = Label(createMemMenu,
                             text = "To Create Member, Please Enter Requested Information Below:",
                             font=("Arial", 18, "bold"),
                             relief="solid",
                             borderwidth=3,
                             bg="aquamarine");
    createTitleLabel.place(x=0, y=0, width=1280, height=150);
    # Membership Id Input Field
    createMemberIdLabel = Label(createMemMenu,
                               text = "Membership ID",
                               font=("calibre", 14, "bold"),
                               bg="DodgerBlue4",
                               fg="ghost white")
    createMemberIdLabel.place(x=280, y=150, width=300, height=90);
    entryMemberId = Entry(createMemMenu,font=('Arial',10,'italic'))
    entryMemberId.place(x=620, y=180, width=450, height=30);
    # Membership Name Input Field
    createNameLabel = Label(createMemMenu,
                           text = "Name",
                           font=("calibre", 14, "bold"),
                           bg="royalblue4",
                           fg="white")
    createNameLabel.place(x=280, y=240, width=300, height=90);
    entryName = Entry(createMemMenu, font=('Arial',10,'italic'))
    entryName.place(x=620, y=270, width=450, height=30);
    # Membership Faculty Input Field
    createFacLabel = Label(createMemMenu,
                           text = "Faculty",
                           font=("calibre", 14, "bold"),
                           bg="royalblue3",
                           fg="white")
    createFacLabel.place(x=280, y=330, width=300, height=90);
    entryFac = Entry(createMemMenu, font=('Arial',10,'italic'))
    entryFac.place(x=620, y=360, width=450, height=30);
    # Membership Phone Input Field
    createPhoneLabel = Label(createMemMenu,
                             text = "Phone Number",
                             font=("calibre", 14, "bold"),
                             bg="royalblue2",
                             fg="white")
    createPhoneLabel.place(x=280, y=420, width=300, height=90);
    entryPhone = Entry(createMemMenu, font=('Arial',10,'italic'))
    entryPhone.place(x=620, y=450, width=450, height=30);
    # Membership Email Input Field
    createEmailLabel = Label(createMemMenu,
                             text = "Email Address",
                             font=("calibre", 14, "bold"),
                             bg="royalblue1",
                             fg="white")
    createEmailLabel.place(x=280, y=510, width=300, height=90);
    entryEmail = Entry(createMemMenu, font=('Arial',10,'italic'))
    entryEmail.place(x=620, y=540, width=450, height=30);
    # Membership Creation Button
    createRecordButton = Button(createMemMenu,
                                text = "Create Member",
                                font=("Arial, 18"),
                                bg="aquamarine",
                                command=createMemberFunc)
    createRecordButton.place(x=355, y=610, width=250, height=80);
    # Return to Main Menu Button
    backButton = Button(createMemMenu,
                        text = "Back to Main Menu",
                        font=("Arial, 18"),
                        bg="aquamarine",
                        command=navFromCreateToMemMenu)
    backButton.place(x=675, y=610, width=250, height=80);
### Membership 2 - Deletion Menu ############################################################################################################################################################################################################
def memberDeletion():    
    global deleteMemMenu
    deleteMemMenu = Toplevel()
    deleteMemMenu.grab_set()
    deleteMemMenu.title("Member Deletion Menu")
    deleteMemMenu.geometry("1280x720")

    ###################################################################################################################
    ### Membership 2.1 - Link Deletion to backend
    def closeConfirmDeletionMemDialog():
        deleteMemMenu.lift();
        deleteConfirmDialog.destroy();
    def deleteMem():
        try:
            result = sqlFuncs.confirmDeletion(entryMemberId.get())
        except:
            messagebox.showerror("Member Deletion Failed", "Member does not exist");
        finally:
            result = sqlFuncs.confirmDeletion(entryMemberId.get())
            openDeleteMemDialog(result)
    ###################################################################################################################
    ### Membership 2.2 - Deletion Confirmation Dialog
    def openDeleteMemDialog(sqlResult):
        global deleteConfirmDialog
        deleteConfirmDialog = Toplevel();
        deleteConfirmDialog.grab_set();
        deleteConfirmDialog.title("Confirm Deletion of Member");
        deleteConfirmDialog.geometry("750x800")
        deleteConfirmDialog.configure(bg = "limegreen")

        def confirmDeleteMem():
            try:
                sqlFuncs.deleteMember(sqlResult[0]);
                openDeleteMemberSuccessDialog();
            except Exception as excp:
                messagebox.showerror("Member Deletion Failed", "Member has loans,\n reservations or outstanding fines.")
        ## Deletion confirmation dialog Design
        deleteConfirmTitleLabel = Label(deleteConfirmDialog,
                                    text="Please Confirm Details to \nBe Correct",
                                    font=("Arial",24,"bold"),
                                    bg="LightSteelBlue2")
        deleteConfirmTitleLabel.place(x=0, y=0, width=750, height=100);
        # Membership Id Field
        deleteConfirmMemIdLabel = Label(deleteConfirmDialog,
                                    text = "Membership ID: {0}".format(sqlResult[0]),
                                    font = ("calibre", 15),
                                    bg = "SkyBlue2")
        deleteConfirmMemIdLabel.place(x=100, y=100, width=550, height=80)
        # Member Name Field
        deleteConfirmMemNameLabel = Label(deleteConfirmDialog,
                                    text = "Name: {0}".format(sqlResult[1]),
                                    font = ("calibre", 15),
                                    bg = "SkyBlue2")
        deleteConfirmMemNameLabel.place(x=100, y=200, width=550, height=80)
        # Member Faculty Field
        deleteConfirmMemFacLabel = Label(deleteConfirmDialog,
                                    text = "Faculty: {0}".format(sqlResult[2]),
                                    font = ("calibre", 15),
                                    bg = "SkyBlue2")
        deleteConfirmMemFacLabel.place(x=100, y=300, width=550, height=80)
        # Member Phone Field
        deleteConfirmMemPhoneLabel = Label(deleteConfirmDialog,
                                    text = "Phone: {0}".format(sqlResult[3]),
                                    font = ("calibre", 15),
                                    bg = "SkyBlue2")
        deleteConfirmMemPhoneLabel.place(x=100, y=400, width=550, height=80)
        # Member Faculty Field
        deleteConfirmMemEmailLabel = Label(deleteConfirmDialog,
                                    text = "Email: {0}".format(sqlResult[4]),
                                    font = ("calibre", 15),
                                    bg = "SkyBlue2")
        deleteConfirmMemEmailLabel.place(x=100, y=500, width=550, height=80)
        ## Confirm Deletion Button
        deleteMemConfirmButton = Button(deleteConfirmDialog,
                                    text = "Confirm\nDeletion",
                                    font = ("Arial", 20, "bold"),
                                    fg = "ghost white",
                                    bg = "magenta2",
                                    command = confirmDeleteMem)
        deleteMemConfirmButton.place(x=200, y=700, width=150, height=80)
        
        ## Close Return Button
        deleteMemCloseButton = Button(deleteConfirmDialog,
                                    text = "Exit",
                                    font = ("Arial", 20, "bold"),
                                    fg = "ghost white",
                                    bg = "magenta2",
                                    command = closeConfirmDeletionMemDialog)
        deleteMemCloseButton.place(x=400, y=700, width=150, height=80)
    ################################################################################################################### 
    ## Membership 2.3 - Deletion Success Popup
    def closeDeletionMemSuccessDialog():
        deleteMemMenu.lift();
        deleteMemSuccessDialog.destroy();
    def openDeleteMemberSuccessDialog():
        deleteConfirmDialog.destroy();
        global deleteMemSuccessDialog
        deleteMemSuccessDialog = Toplevel();
        deleteMemSuccessDialog.grab_set() ## Make sure only top level window is editable
        deleteMemSuccessDialog.configure(bg="limegreen")
        deleteMemSuccessDialog.geometry("450x400")
        ## Error Title Label
        errorTitle = Label(deleteMemSuccessDialog,
                            text = "Success! \n\n ALS Membership deleted.",
                            font=("Arial", 18,"bold"),
                            bg="limegreen",
                            fg="Black");
        errorTitle.place(x=0, y=100, width=450, height=100);
        ## return Button
        returnButton = Button(deleteMemSuccessDialog,
                            text="Back to \n Delete \n Function",
                            font=("Arial", 12,"bold"),
                            borderwidth=8,
                            bg="aquamarine",
                            command=closeDeletionMemSuccessDialog);
        returnButton.place(x=125, y=300, width=200, height=80)
    ###################################################################################################################  
    ### Membership 2.4 - Design and Placement
    # Title
    deleteTitleLabel = Label(deleteMemMenu,
                            text = "To Delete Member, Please Enter Membership ID:",
                            font=("Arial",24,"bold"),
                            bg="aquamarine");
    deleteTitleLabel.place(x=0, y=0, width=1280, height=180);

    # Membership Id Input Field
    deleteMemberIdLabel = Label(deleteMemMenu,
                            text = "Membership ID",
                            font=("calibre", 14, "bold"),
                            bg="DodgerBlue4",
                            fg="white")
    deleteMemberIdLabel.place(x=280, y=330, width=300, height=90);
    entryMemberId = Entry(deleteMemMenu, font=('Arial',10,'italic'))
    entryMemberId.place(x=620, y=360, width=450, height=30);

    # Membership Deletion Button
    deleteRecordButton = Button(deleteMemMenu,
                            text = "Delete Member",
                            font=("Arial, 18"),
                            bg="aquamarine",
                            command=deleteMem)
    deleteRecordButton.place(x=355, y=610, width=250, height=80);

    # Return to Main Menu Button
    backButton = Button(deleteMemMenu,
                            text = "Back to Main Menu",
                            font=("Arial, 18"),
                            bg="aquamarine",
                            command=navFromDeleteToMemMenu)
    backButton.place(x=675, y=610, width=250, height=80);

### Membership 3 - Update Landing Window ########################################################################################################################################################################################################################################
def updateMemMenu():
    global updateInputId
    updateInputId = Toplevel()
    updateInputId.geometry("1280x720")
    ###################################################################################################################  
    ### Membership 3.1 - Close update landing menu
    def destroyUpdateMenu():
        updateDetailMenu.destroy();
    def navReturnToMemMenuFromUpdateDetails(): # Return to Membership Menu
        membershipMenu();
        destroyUpdateMenu();
    def navFromUpdateToUpdateDetails(): # Go to Update Details Menu
        try:
            entryUpdateMemberId = entryMemberId.get();
            sqlFuncs.checkMemForUpdate(entryUpdateMemberId);
            ## Code runs only if there is no error
            destroyUpdateLandingMenu();
            updateDetails(entryUpdateMemberId);
            updateDetailMenu.lift();
        except:
            messagebox.showerror("Member Update Error", "Member does not exist");

    ###################################################################################################################
    ### Membership 3.2 - Go to update member details page
    def updateDetails(entryUpdateMemberId):
        global updateDetailMenu
        updateDetailMenu = Toplevel();
        updateDetailMenu.grab_set();
        updateDetailMenu.geometry("1280x720")
        ###################################################################################################################
        ### Membership 3.2.1 - Close confirm update details dialog
        def closeConfirmUpdateMemDialog():
            updateDetailMenu.lift();
            updateConfirmDialog.destroy();
        def updateMem():
            try:
                result = sqlFuncs.confirmUpdate(entryUpdateMemberId,
                                        entryName.get(),
                                        entryFac.get(),
                                        entryPhone.get(),
                                        entryEmail.get())
                #Code runs when there is no error
                openUpdateMemDialog(result)
            except:
                messagebox.showerror("Member Update Error", "Missing or \nIncomplete Fields.")
        ###################################################################################################################
        ### Membership 3.2.2 - Update member dialog
        def openUpdateMemDialog(sqlResult):
            global updateConfirmDialog
            updateConfirmDialog = Toplevel();
            updateConfirmDialog.grab_set();
            updateConfirmDialog.title("Confirm Deletion of Member");
            updateConfirmDialog.geometry("750x800")
            updateConfirmDialog.configure(bg = "limegreen")

            def confirmUpdateMemFunction():
                try:
                    sqlFuncs.updateMember(sqlResult[0],
                                        sqlResult[1],
                                        sqlResult[2],
                                        sqlResult[3],
                                        sqlResult[4]);
                    openUpdateMemberSuccessDialog(); ##MEMBERSHIP 3.2.3 NEED TO ADD
                except Exception as excp:
                    messagebox.showerror("Member Update Failed", "Missing or \n Incomplete fields.")
            
            ## Deletion confirmation dialog Design
            deleteConfirmTitleLabel = Label(updateConfirmDialog,
                                        text="Please Confirm Updated Details to \nBe Correct",
                                        font=("Arial",24,"bold"),
                                        bg="LightSteelBlue2")
            deleteConfirmTitleLabel.place(x=0, y=0, width=750, height=100);
            # Membership Id Field
            deleteConfirmMemIdLabel = Label(updateConfirmDialog,
                                        text = "Membership ID: {0}".format(sqlResult[0]),
                                        font = ("calibre", 15),
                                        bg = "SkyBlue2")
            deleteConfirmMemIdLabel.place(x=100, y=100, width=550, height=80)
            # Member Name Field
            deleteConfirmMemNameLabel = Label(updateConfirmDialog,
                                        text = "Name: {0}".format(sqlResult[1]),
                                        font = ("calibre", 15),
                                        bg = "SkyBlue2")
            deleteConfirmMemNameLabel.place(x=100, y=200, width=550, height=80)
            # Member Faculty Field
            deleteConfirmMemFacLabel = Label(updateConfirmDialog,
                                        text = "Faculty: {0}".format(sqlResult[2]),
                                        font = ("calibre", 15),
                                        bg = "SkyBlue2")
            deleteConfirmMemFacLabel.place(x=100, y=300, width=550, height=80)
            # Member Phone Field
            deleteConfirmMemPhoneLabel = Label(updateConfirmDialog,
                                        text = "Phone: {0}".format(sqlResult[3]),
                                        font = ("calibre", 15),
                                        bg = "SkyBlue2")
            deleteConfirmMemPhoneLabel.place(x=100, y=400, width=550, height=80)
            # Member Faculty Field
            deleteConfirmMemEmailLabel = Label(updateConfirmDialog,
                                        text = "Email: {0}".format(sqlResult[4]),
                                        font = ("calibre", 15),
                                        bg = "SkyBlue2")
            deleteConfirmMemEmailLabel.place(x=100, y=500, width=550, height=80)
            ## Confirm Deletion Button
            deleteMemConfirmButton = Button(updateConfirmDialog,
                                        text = "Confirm\nUpdate",
                                        font = ("Arial", 20, "bold"),
                                        fg = "ghost white",
                                        bg = "magenta2",
                                        command = confirmUpdateMemFunction)
            deleteMemConfirmButton.place(x=200, y=700, width=150, height=80)
            
            ## Close Return Button
            deleteMemCloseButton = Button(updateConfirmDialog,
                                        text = "Exit",
                                        font = ("Arial", 20, "bold"),
                                        fg = "ghost white",
                                        bg = "magenta2",
                                        command = closeConfirmUpdateMemDialog)
            deleteMemCloseButton.place(x=400, y=700, width=150, height=80)
        ###################################################################################################################
        ## Membership 3.2.3 - Update Success Dialog
        def closeUpdateMemberSuccessDialog():
            updateDetailMenu.lift();
            updateMemSuccessDialog.destroy();
        def openUpdateMemberSuccessDialog():
            updateConfirmDialog.destroy();
            global updateMemSuccessDialog
            updateMemSuccessDialog = Toplevel();
            updateMemSuccessDialog.grab_set() ## Make sure only top level window is editable
            updateMemSuccessDialog.configure(bg="limegreen")
            updateMemSuccessDialog.geometry("450x400")
            ## Error Title Label
            errorTitle = Label(updateMemSuccessDialog,
                                text = "Success! \n\n ALS Membership updated.",
                                font=("Arial", 18,"bold"),
                                bg="limegreen",
                                fg="Black");
            errorTitle.place(x=0, y=100, width=450, height=100);
            ## return Button
            returnButton = Button(updateMemSuccessDialog,
                                text="Back to \n Update \n Function",
                                font=("Arial", 12,"bold"),
                                borderwidth=8,
                                bg="aquamarine",
                                command=closeUpdateMemberSuccessDialog);
            returnButton.place(x=125, y=300, width=200, height=80)
        ###################################################################################################################
        ### Membership 3.2.4 - Update Details Menu Design
        ## Title Label
        updateTitleLabel = Label(updateDetailMenu,
                            text = "Please Enter Requested Information Below:",
                            font=("Arial, 18"),
                            bg="aquamarine");
        updateTitleLabel.place(x=0, y=0, width=1280, height=150);

        # Membership Id Input Field
        updateMemberIdLabel = Label(updateDetailMenu,
                            text = "Membership ID",
                            borderwidth=2,
                            relief="solid",
                            font=("calibre", 14, "bold"),
                            bg="DodgerBlue4")
        updateMemberIdLabel.place(x=280, y=150, width=300, height=90);
        
        enteredMemberId = Label(updateDetailMenu,
                            text = entryUpdateMemberId,
                            borderwidth=2,
                            relief="solid",
                            font=("Arial, 12"))
        enteredMemberId.place(x=620, y=180, width=450, height=30);

        ## Membership Name Input Field
        updateNameLabel = Label(updateDetailMenu,
                            text = "Name",
                            font=("calibre", 14, "bold"),
                            borderwidth=2,
                            relief="solid",
                            bg="royalblue4",
                            fg="white")
        updateNameLabel.place(x=280, y=240, width=300, height=90);
        entryName = Entry(updateDetailMenu, font=('Arial',10,'italic'))
        entryName.place(x=620, y=270, width=450, height=30);
        ## Membership Faculty Input Field
        updateFacLabel = Label(updateDetailMenu,
                            text = "Faculty",
                            font=("calibre", 14, "bold"),
                            borderwidth=2,
                            relief="solid",
                            bg="royalblue3",
                            fg="white")
        updateFacLabel.place(x=280, y=330, width=300, height=90);
        entryFac = Entry(updateDetailMenu, font=('Arial',10,'italic'))
        entryFac.place(x=620, y=360, width=450, height=30);
        ## Membership Phone Input Field
        updatePhoneLabel = Label(updateDetailMenu,
                            text = "Phone Number",
                            font=("calibre", 14, "bold"),
                            borderwidth=2,
                            relief="solid",
                            bg="royalblue2",
                            fg="white")
        updatePhoneLabel.place(x=280, y=420, width=300, height=90);
        entryPhone = Entry(updateDetailMenu, font=('Arial',10,'italic'))
        entryPhone.place(x=620, y=450, width=450, height=30);
        ## Membership Email Input Field
        updateEmailLabel = Label(updateDetailMenu,
                            text = "Email Address",
                            font=("calibre", 14, "bold"),
                            borderwidth=2,
                            relief="solid",
                            bg="royalblue1",
                            fg="white")
        updateEmailLabel.place(x=280, y=510, width=300, height=90);
        entryEmail = Entry(updateDetailMenu, font=('Arial',10,'italic'))
        entryEmail.place(x=620, y=540, width=450, height=30);
        ## Membership Creation Button
        updateRecordButton = Button(updateDetailMenu,
                            text = "Update Member",
                            font=("Arial, 18"),
                            bg="aquamarine",
                            command=updateMem)
        updateRecordButton.place(x=355, y=610, width=250, height=80);
        ## Return to Main Menu Button
        backButton = Button(updateDetailMenu,
                            text = "Back to Main Menu",
                            font=("Arial, 18"),
                            bg="aquamarine",
                            command=navReturnToMemMenuFromUpdateDetails)
        backButton.place(x=675, y=610, width=250, height=80);
    ###################################################################################################################  
    ### Membership 3.3 - Update Input membershipId Design
    ## Title Label
    updateTitleLabel = Label(updateInputId,
                            text = "To Update a Member, Please Enter Membership ID:",
                            font=("Arial",24, "bold"),
                            bg="aquamarine");
    updateTitleLabel.place(x=0, y=0, width=1280, height=180);
    ## Membership Id Input Field
    updateMemberIdLabel = Label(updateInputId,
                            text = "Membership ID",
                            font=("calibre", 14, "bold"),
                            bg="DodgerBlue4",
                            fg="white")
    updateMemberIdLabel.place(x=280, y=300, width=300, height=100);
    entryMemberId = Entry(updateInputId, font=('Arial',10,'italic'))
    entryMemberId.place(x=620, y=360, width=450, height=30);
    ## Membership Update Button
    updateRecordButton = Button(updateInputId,
                            text = "Update Member",
                            font=("Arial, 18"),
                            bg="aquamarine",
                            command=navFromUpdateToUpdateDetails)
    updateRecordButton.place(x=355, y=610, width=250, height=80);
    ## Return to Main Menu Button
    backButton = Button(updateInputId,
                            text = "Back to Main Menu",
                            font=("Arial, 18"),
                            bg="aquamarine",
                            command=navReturnToMemMenuFromUpdateLanding)
    backButton.place(x=675, y=610, width=250, height=80);
#####################################################################################################################################################################################################################################


################################################
## BOOK FUNCTIONS BELOW ##
################################################

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
    
def confirmWithDialogFunc():

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
        confirmWithDialog.grab_set()
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
        command = confirmWithDialogFunc)
    buttonSubmitWith.place(x=460, y=450, width=400, height=100)

    ## Back Button
    buttonWithBack = Button(bookWith,
        text = "Back",
        font = ("calibre", 15, "bold"),
        fg = "grey39",
        bg = "snow3",
        command = navFromBookWithToBook)

    buttonWithBack.place(x=1100, y=600, width=140, height=40)
################################################################################################################################################################









################################################
## LOANS FUNCTIONS BELOW ##
################################################
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
    landingPageFunc()
    destroyLoansMenu()
    landingPage.lift()

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

    def closeConfirmBorrowDialog():
        loansBorrowMenu.lift()
        borrowConfirmDialog.destroy()

    def borrowBook():
        try:
            result = sqlFuncs.confirmLoan(loansBorrowMemberIdEntry.get(),
                                          loansBorrowAccNumEntry.get(),
                                          datetime.today().strftime('%Y/%m/%d'))
            openConfirmBookDialog(result)
        except:
            messagebox.showerror("Book Borrow Error", "Accession Number/Membership ID does not exist")
        
    ############################################
    ## Loans 2.1 - Borrow Confirmation 
    ############################################
    def openConfirmBookDialog(sqlResult):
        global borrowConfirmDialog
        borrowConfirmDialog = Toplevel()
        borrowConfirmDialog.grab_set()
        borrowConfirmDialog.geometry("750x800")
        borrowConfirmDialog.configure(bg = "limegreen")

        def confirmBorrowBook():
            try:
                sqlFuncs.loanBook(sqlResult[2][0],
                                   sqlResult[0][0],
                                   sqlResult[1])
                closeConfirmBorrowDialog()
            except Exception as excp:
                if excp.args[0] == "Loan Quota Exceeded":
                    messagebox.showerror(
                        "Book Borrow Error",
                        "Error: Member loan quota exceeded")
                
                elif excp.args[0] == "Outstanding Fines":
                    messagebox.showerror(
                        "Book Borrow Error",
                        "Error: Member has outstanding fines")
                else:
                    messagebox.showerror(
                        "Book Borrow Error",
                        "Error: {0}".format(excp.args[0]))
 

        ## Information Header
        borrowConfirmTitleLabel = Label(borrowConfirmDialog,
                           text = "Confirm Loan Details",
                           font =("calibre", 32, "bold"),
                           bg = "LightSteelBlue2")
        borrowConfirmTitleLabel.place(x=0, y=0, width=750, height=100);

        ## Accession Number Field
        borrowConfirmAccInputLabel = Label(borrowConfirmDialog,
                                  text = "Accession Number: {0}"
                                           .format(sqlResult[0][0]),
                                  font = ("calibre", 15),
                                  bg = "SkyBlue2")
        borrowConfirmAccInputLabel.place(x=100, y=100, width=550, height=80)   

        ## Book Title Field
        borrowConfirmBookTitleLabel = Label(borrowConfirmDialog,
                                  text = "Book Title: {0}"
                                           .format(sqlResult[0][1]),
                                  font = ("calibre", 15),
                                  bg = "SkyBlue2")
        borrowConfirmBookTitleLabel.place(x=100, y=200, width=550, height=80)

        ## Borrow Date Field
        borrowDateLabel = Label(borrowConfirmDialog,
                                  text = "Return Date: {0}"
                                           .format(sqlResult[1]),
                                  font = ("calibre", 15),
                                  bg = "SkyBlue2")
        borrowDateLabel.place(x=100, y=300, width=550, height=80)
                             
        ## MembershipId Field
        borrowMembershipIdLabel = Label(borrowConfirmDialog,
                                  text = "Membership ID: {0}"
                                           .format(sqlResult[2][0]),
                                  font = ("calibre", 15),
                                  bg = "SkyBlue2")
        borrowMembershipIdLabel.place(x=100, y=400, width=550, height=80)

        ## Member Name Field
        borrowMemberNameLabel = Label(borrowConfirmDialog,
                                  text = "Membership ID: {0}"
                                           .format(sqlResult[2][1]),
                                  font = ("calibre", 15),
                                  bg = "SkyBlue2")
        borrowMemberNameLabel.place(x=100, y=500, width=550, height=80)

        ## Borrow Due Date Field
        borrowDueDateLabel = Label(borrowConfirmDialog,
                                  text = "Return Date: {0}"
                                           .format(sqlResult[3]),
                                  font = ("calibre", 15),
                                  bg = "SkyBlue2")
        borrowDueDateLabel.place(x=100, y=600, width=550, height=80)


        ## Confirm Borrow Button
        borrowBookConfirmButton = Button(borrowConfirmDialog,
            text = "Confirm\nBorrow",
            font = ("Arial", 20, "bold"),
            fg = "ghost white",
            bg = "magenta2",
            command = confirmBorrowBook)
        borrowBookConfirmButton.place(x=200, y=700, width=150, height=80)
        
        ## Close Return Button
        borrowBookCloseButton = Button(borrowConfirmDialog,
            text = "Exit",
            font = ("Arial", 20, "bold"),
            fg = "ghost white",
            bg = "magenta2",
            command = closeConfirmBorrowDialog)
        borrowBookCloseButton.place(x=400, y=700, width=150, height=80)

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
    loansReturnMenu.grab_set()
    loansReturnMenu.title("Return a Book")
    loansReturnMenu.geometry("1280x720")

    def closeReturnDialog():
        loansReturnMenu.lift()
        returnConfirmDialog.destroy()

    def returnBook():
        try:
            result = sqlFuncs.confirmReturn(loansReturnAccNumEntry.get(),
                                            loansReturnDateEntry.get())
            openReturnConfirmDialog(result)
        except:
            messagebox.showerror(
                    "Book Return Error",
                    "Accession Number/Return Date incorrect")

    ############################################
    ## Loans 3.1 - Return Confirmation 
    ############################################
    def openReturnConfirmDialog(sqlResult):
        global returnConfirmDialog
        returnConfirmDialog = Toplevel()
        returnConfirmDialog.grab_set()
        returnConfirmDialog.geometry("750x800")
        returnConfirmDialog.configure(bg = "limegreen")

        def confirmReturnBook():
            try:
                response = sqlFuncs.returnBook(sqlResult[0],
                                               sqlResult[4])
                if response == "Warning! Member has outstanding fines to pay":
                    messagebox.showerror(
                            "Book Return Warning",
                            "Reminder: Member has outstanding fines")
                closeReturnDialog()
            except:
                messagebox.showerror(
                        "Book Return Error",
                        "Return Date cannot be before Loan Date")

        ## Information Header
        returnConfirmTitleLabel = Label(returnConfirmDialog,
                           text = "Confirm Return Details",
                           font =("calibre", 32, "bold"),
                           bg = "LightSteelBlue2")
        returnConfirmTitleLabel.place(x=0, y=0, width=750, height=100);

        ## Accession Number Field
        returnConfirmAccInputLabel = Label(returnConfirmDialog,
                                  text = "Accession Number: {0}"
                                           .format(sqlResult[0]),
                                  font = ("calibre", 15),
                                  bg = "SkyBlue2")
        returnConfirmAccInputLabel.place(x=100, y=100, width=550, height=80)   

        ## Book Title Field
        returnConfirmBookTitleLabel = Label(returnConfirmDialog,
                                  text = "Book Title: {0}"
                                           .format(sqlResult[1]),
                                  font = ("calibre", 15),
                                  bg = "SkyBlue2")
        returnConfirmBookTitleLabel.place(x=100, y=200, width=550, height=80)
                             
        ## MembershipId Field
        returnMembershipIdLabel = Label(returnConfirmDialog,
                                  text = "Membership ID: {0}"
                                           .format(sqlResult[2]),
                                  font = ("calibre", 15),
                                  bg = "SkyBlue2")
        returnMembershipIdLabel.place(x=100, y=300, width=550, height=80)

        ## Member Name Field
        returnMemberNameLabel = Label(returnConfirmDialog,
                                  text = "Membership ID: {0}"
                                           .format(sqlResult[3]),
                                  font = ("calibre", 15),
                                  bg = "SkyBlue2")
        returnMemberNameLabel.place(x=100, y=400, width=550, height=80)

        ## Return Date Field
        returnDateLabel = Label(returnConfirmDialog,
                                  text = "Return Date: {0}"
                                           .format(sqlResult[4]),
                                  font = ("calibre", 15),
                                  bg = "SkyBlue2")
        returnDateLabel.place(x=100, y=500, width=550, height=80)

        ## Return Fine Field
        returnFineLabel = Label(returnConfirmDialog,
                                  text = "Fine: ${0}"
                                           .format(sqlResult[5]),
                                  font = ("calibre", 15),
                                  bg = "SkyBlue2")
        returnFineLabel.place(x=100, y=600, width=550, height=80)


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
                              text = "Return Date\n(ensure the format\nis YYYY/MM/DD)",
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

################################################################################################################################################################




################################################
## RESERVATIONS FUNCTIONS BELOW ##
################################################
####################################################################################################################################################################################
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

################################################################################################################################################################









################################################
## FINES FUNCTIONS BELOW ##
################################################
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

################################################################################################################################################################






################################################
## REPORTS FUNCTIONS BELOW ##
################################################
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
################################################################################################################################################################












########### Dont delete - used to start the app
window = Tk()

startButton = Button(window, text = "Start", command = landingPageFunc, fg = "lightblue",
                     bg = "black", font = ("Mincho", 20))
startButton.pack()

window.mainloop()


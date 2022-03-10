from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
import backendSQL as sqlFuncs

window = Tk()


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
    memberUpdateLandingMenu();
    destroyMemMenu();
    updateInputId.lift()
def navReturnToMain(): # Return to Main Menu
    window.destroy()
    import landingPage

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
def navFromUpdateToUpdateDetails(): # Go to Update Details Menu
    destroyUpdateLandingMenu();
    updateMenu();
    updateMemMenu.lift();
def destroyUpdateLandingMenu():
    updateInputId.destroy();
def navReturnToMemMenuFromUpdateLanding(): # Return to Membership Menu
    membershipMenu();
    destroyUpdateLandingMenu();
    memMenu.lift()
def destroyUpdateMenu():
    updateMemMenu.destroy();
def navReturnToMemMenuFromUpdateDetails(): # Return to Membership Menu
    membershipMenu();
    destroyUpdateMenu();
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
#####################################################################################################################################################################################################################################
### Membership 1 - Creation ############################################################################################################################################################################################################

def memberCreation(): 
    global createMemMenu
    createMemMenu = Toplevel()
    createMemMenu.title("Create a Member")
    createMemMenu.geometry("1280x720")

    ###################################################################################################################
    ## Create Member Confirmation and Error Handling
    def closeCreateMemSuccessDialog():
        createMemMenu.lift()
        createMemSuccessDialog.destroy()
    def createMemberFunc():
        try:
            sqlFuncs.createMember(entryMemberId.get(),
                                  entryName.get(),
                                  entryFac.get(),
                                  entryPhone.get(),
                                  entryEmail.get());
            openCreateMemberSuccessDialog();
        except Exception as excp:
            messagebox.showerror("Member Creation Error",
                                 "Member already exist; Missing or\n Incomplete fields.")
    ###################################################################################################################
    ## Member Creation Windows and Popups
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
    ## Window Design and Placement
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
    entryMemberId.place(x=620, y=160, width=450, height=30);
    # Membership Name Input Field
    createNameLabel = Label(createMemMenu,
                           text = "Name",
                           font=("calibre", 14, "bold"),
                           bg="royalblue4",
                           fg="white")
    createNameLabel.place(x=280, y=240, width=300, height=90);
    entryName = Entry(createMemMenu, font=('Arial',10,'italic'))
    entryName.place(x=620, y=260, width=450, height=30);
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
    entryPhone.place(x=620, y=460, width=450, height=30);
    # Membership Email Input Field
    createEmailLabel = Label(createMemMenu,
                             text = "Email Address",
                             font=("calibre", 14, "bold"),
                             bg="royalblue1",
                             fg="white")
    createEmailLabel.place(x=280, y=510, width=300, height=90);
    entryEmail = Entry(createMemMenu, font=('Arial',10,'italic'))
    entryEmail.place(x=620, y=560, width=450, height=30);
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
### Member Deletion Menu ############################################################################################################################################################################################################
def memberDeletion():    
    global deleteMemMenu
    deleteMemMenu = Toplevel()
    deleteMemMenu.grab_set()
    deleteMemMenu.title("Member Deletion Menu")
    deleteMemMenu.geometry("1280x720")

    ###################################################################################################################
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
    ### Membership 2.2 - Deletion Confirmation
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
    ## Member Deletion Windows and Popups
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
    ## Window Design and Placement
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
    deleteMemberIdLabel.place(x=280, y=300, width=300, height=100);
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

### Update Landing Window ########################################################################################################################################################################################################################################
def memberUpdateLandingMenu():
    global updateInputId
    updateInputId = Toplevel()
    updateInputId.geometry("750x420")

    ## Title Label
    updateTitleLabel = Label(updateInputId,
                                text = "To Update a Member, Please Enter Membership ID:",
                                font=("Arial, 18"),
                                bg="aquamarine");
    updateTitleLabel.place(x=0, y=0, width=750, height=180);
    ## Membership Id Input Field
    updateMemberIdLabel = Label(updateInputId,
                                   text = "Membership ID",
                                   font=("Arial, 10"),
                                   bg="DodgerBlue3",
                                   fg="white")
    updateMemberIdLabel.place(x=0, y=200, width=300, height=100);
    entryMemberId = Entry(updateInputId, font=('Arial',10,'normal'))
    entryMemberId.place(x=300, y=260, width=450, height=40);
    ## Membership Update Button
    updateRecordButton = Button(updateInputId,
                                   text = "Update Member",
                                   font=("Arial, 18"),
                                   bg="aquamarine",
                                   command=navFromUpdateToUpdateDetails)
    updateRecordButton.place(x=80, y=320, width=250, height=80);
    ## Return to Main Menu Button
    backButton = Button(updateInputId,
                           text = "Back to Main Menu",
                           font=("Arial, 18"),
                           bg="aquamarine",
                           command=navReturnToMemMenuFromUpdateLanding)
    backButton.place(x=420, y=320, width=250, height=80);

### Update Member Details Window ########################################################################################################################################################################################################################################
def updateMenu():
    # To add:
    # If-Else for Success/Error messages
    # SQLAlchemy retrieval
    
    updateInputId.destroy();
    
    global updateMemMenu
    updateMemMenu = Toplevel()
    updateMemMenu.geometry("750x820")

    ## Title Label
    updateTitleLabel = Label(updateMemMenu,
                             text = "Please Enter Requested Information Below:",
                             font=("Arial, 18"),
                             bg="aquamarine");
    updateTitleLabel.place(x=0, y=0, width=750, height=200);

    # Membership Id Input Field
    updateMemberIdLabel = Label(updateMemMenu,
                                text = "Membership ID",
                                borderwidth=2,
                                relief="solid",
                                font=("Arial, 10"),
                                bg="SlateBlue")
    updateMemberIdLabel.place(x=0, y=200, width=300, height=100);
    
    enteredMemberId = Label(updateMemMenu,
                            text = "A01234567B",
                            borderwidth=2,
                            relief="solid",
                            font=("Arial, 12"))
    enteredMemberId.place(x=300, y=260, width=450, height=40);

    ## Membership Name Input Field
    updateNameLabel = Label(updateMemMenu,
                            text = "Name",
                            font=("Arial, 10"),
                            borderwidth=2,
                            relief="solid",
                            bg="SlateBlue",
                            fg="white")
    updateNameLabel.place(x=0, y=300, width=300, height=100);

    entryName = Entry(updateMemMenu,
                         font=('Arial',10,'normal'))
    entryName.place(x=300, y=360, width=450, height=40);

    ## Membership Faculty Input Field
    updateFacLabel = Label(updateMemMenu,
                           text = "Faculty",
                           font=("Arial, 10"),
                           borderwidth=2,
                           relief="solid",
                           bg="SlateBlue",
                           fg="white")
    updateFacLabel.place(x=0, y=400, width=300, height=100);
    entryFac = Entry(updateMemMenu, font=('Arial',10,'normal'))
    entryFac.place(x=300, y=460, width=450, height=40);


    ## Membership Phone Input Field
    updatePhoneLabel = Label(updateMemMenu,
                                text = "Phone Number",
                                font=("Arial, 10"),
                                borderwidth=2,
                                relief="solid",
                                bg="SlateBlue",
                                fg="white")
    updatePhoneLabel.place(x=0, y=500, width=300, height=100);
    
    entryPhone = Entry(updateMemMenu,
                          font=('Arial',10,'normal'))
    entryPhone.place(x=300, y=560, width=450, height=40);

    ## Membership Email Input Field
    updateEmailLabel = Label(updateMemMenu,
                                text = "Email Address",
                                font=("Arial, 10"),
                                borderwidth=2,
                                relief="solid",
                                bg="SlateBlue",
                                fg="white")
    updateEmailLabel.place(x=0, y=600, width=300, height=100);

    entryEmail = Entry(updateMemMenu,
                          font=('Arial',10,'normal'))
    entryEmail.place(x=300, y=660, width=450, height=40);

    ## Membership Creation Button
    updateRecordButton = Button(updateMemMenu,
                                   text = "Update Member",
                                   font=("Arial, 18"),
                                   bg="aquamarine")
    updateRecordButton.place(x=80, y=710, width=250, height=80);

    ## Return to Main Menu Button
    backButton = Button(updateMemMenu,
                           text = "Back to Main Menu",
                           font=("Arial, 18"),
                           bg="aquamarine",
                           command=navReturnToMemMenuFromUpdateDetails)
    backButton.place(x=420, y=710, width=250, height=80);

#####################################################################################################################################################################################################################################
## Dont delete - used to start the app
startButton = Button(window, text = "Start", command = membershipMenu, fg = "lightblue",
                     bg = "black", font = ("Mincho", 20))
startButton.pack()
window.mainloop()


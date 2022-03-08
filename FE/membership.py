from tkinter import *
from PIL import ImageTk, Image
import sqlalchemy as db

##engine = db.create_engine("")

# Not added/To be fixed
# 2. Check which entry box looks nicer - either in deletion or creation
# 3. Complete SQLAlchemy functions
# 4. Flow control for various errors

window = Tk()

### Membership Landing Page ###

def destroyMemMenu():
    memMenu.destroy();
def openCreate():
    memberCreation();
    destroyMemMenu();
    createMemMenu.lift()
def openDelete():
    memberDeletion()
    destroyMemMenu();
    deleteMemMenu.lift()
def openUpdate():
    memberUpdateLanding();
    destroyMemMenu();
    updateInputId.lift()
def goHome():
    window.destroy()
    import landingPage

def membershipMenu():
    global memMenu
    memMenu = Toplevel();
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
                                  command=openCreate)
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
                                  command=openDelete)
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
                                command=openUpdate)
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
                                  command=goHome)
    goMainFromMemMenu.place(x=140,y=700, width=1000, height=80);


### Member Creation Window ###
##  Member Creation Success Popup
def destroyCreateSc():
    createSuc.destroy();
    
def creationSuccess():
    global createSuc
    createSuc = Toplevel();
    createSuc.configure(bg="chartreuse2")
    createSuc.geometry("450x400")
    ## Error Title Label
    errorTitle = Label(createSuc,
                        text = "Error!",
                        font=("Arial", 40,"bold"),
                        bg="chartreuse2",
                        fg="Black");
    errorTitle.place(x=0, y=100, width=450, height=100);
    ## Error Message Label
    errorMsg = Label(createSuc,
                        text = "ALS Membership created.",
                        font=("Arial", 16,"bold"),
                        bg="chartreuse2",
                        fg="black");
    errorMsg.place(x=0, y=200, width=450, height=100);
    ## Return to
    errorMsg = Button(createSuc,
                         text="Back to \n Create \n Function",
                         font=("Arial", 12,"bold"),
                         borderwidth=8,
                         bg="aquamarine",
                         command=destroyCreateSc);
    errorMsg.place(x=125, y=300, width=200, height=80)
##  Member Creation Failed Popup
def destroyCreateFail():
    createFail.destroy();
def creationFail():
    global createFail
    createFail = Toplevel();
    createFail.configure(bg="red")
    createFail.geometry("450x400")

    ## Error Title Label
    errorTitle = Label(createFail,
                        text = "Error!",
                        font=("Arial", 40,"bold"),
                        bg="red",
                        fg="yellow");
    errorTitle.place(x=0, y=100, width=450, height=100);

    ## Error Message Label
    errorMsg = Label(createFail,
                        text = "Member already exist; Missing or\n Incomplete fields.",
                        font=("Arial", 16,"bold"),
                        bg="red",
                        fg="yellow");
    errorMsg.place(x=0, y=200, width=450, height=100);

    ## Return to
    errorMsg = Button(createFail,
                         text="Back to \n Create \n Function",
                         font=("Arial", 12,"bold"),
                         borderwidth=6,
                         bg="aquamarine",
                         command=destroyCreateFail);
    errorMsg.place(x=125, y=300, width=200, height=80)
## Main Creation Menu
def destroyCreateMenu():
    createMemMenu.destroy();
def goToMemMenuFromCreate():
    membershipMenu();
    destroyCreateMenu()
    memMenu.lift()
def memberCreation():

    # To add:
    # If-Else for Success/Error messages
    # SQL retrieval of fields
    # SQL incomplete fields
    # SQL Member Already Exists
    
    global createMemMenu
    createMemMenu = Toplevel()
    createMemMenu.geometry("750x820")

    ## Title Label
    createTitleLabel = Label(createMemMenu,
                                text = "To Create Member, Please Enter Requested Information Below:",
                                font=("Arial, 18"),
                                bg="aquamarine");
    createTitleLabel.place(x=0, y=0, width=750, height=200);
    ## Membership Id Input Field
    createMemberIdLabel = Label(createMemMenu,
                                   text = "Membership ID",
                                   font=("Arial, 10"),
                                   bg="DodgerBlue3",
                                   fg="white")
    createMemberIdLabel.place(x=0, y=200, width=300, height=100);
    entryMemberId = Entry(createMemMenu,font=('Arial',10,'normal'))
    entryMemberId.place(x=300, y=260, width=450, height=40);
    ## Membership Name Input Field
    createNameLabel = Label(createMemMenu,
                               text = "Name",
                               font=("Arial, 10"),
                               bg="DodgerBlue2",
                               fg="white")
    createNameLabel.place(x=0, y=300, width=300, height=100);
    entryName = Entry(createMemMenu, font=('Arial',10,'normal'))
    entryName.place(x=300, y=360, width=450, height=40);
    ## Membership Faculty Input Field
    createFacLabel = Label(createMemMenu,
                              text = "Faculty",
                              font=("Arial, 10"),
                              bg="SkyBlue2",
                              fg="white")
    createFacLabel.place(x=0, y=400, width=300, height=100);
    entryFac = Entry(createMemMenu, font=('Arial',10,'normal'))
    entryFac.place(x=300, y=460, width=450, height=40);
    ## Membership Phone Input Field
    createPhoneLabel = Label(createMemMenu,
                                text = "Phone Number",
                                font=("Arial, 10"),
                                bg="LightSkyBlue1",
                                fg="white")
    createPhoneLabel.place(x=0, y=500, width=300, height=100);
    entryPhone = Entry(createMemMenu, font=('Arial',10,'normal'))
    entryPhone.place(x=300, y=560, width=450, height=40);
    ## Membership Email Input Field
    createEmailLabel = Label(createMemMenu,
                                text = "Email Address",
                                font=("Arial, 10"),
                                bg="LightBlue1",
                                fg="white")
    createEmailLabel.place(x=0, y=600, width=300, height=100);
    entryEmail = Entry(createMemMenu, font=('Arial',10,'normal'))
    entryEmail.place(x=300, y=660, width=450, height=40);
    ## Membership Creation Button
    createRecordButton = Button(createMemMenu,
                                   text = "Create Member",
                                   font=("Arial, 18"),
                                   bg="aquamarine")
    createRecordButton.place(x=80, y=710, width=250, height=80);
    ## Return to Main Menu Button
    backButton = Button(createMemMenu,
                           text = "Back to Main Menu",
                           font=("Arial, 18"),
                           bg="aquamarine",
                           command=goToMemMenuFromCreate)
    backButton.place(x=420, y=710, width=250, height=80);

### Membership Deletion Window ###
## Member Deletion Success Window
def destroyDelSc():
    delSc.destroy();
def delSuccess():
    global delSc
    delSc = Toplevel();
    delSc.configure(bg="chartreuse2")
    delSc.geometry("450x400")

    # ## Title Label
    titleLabel = Label(delSc,
                       text = "Please Confirm Details to \n Be Correct",
                       font=("Arial", 20, "bold"),
                       bg="chartreuse2");
    titleLabel.place(x=0, y=0, width=450, height=140);

    ## Membership Id Field
    memberIdLabel = Label(delSc,
                          text = "Membership ID (placeholder)",
                          font=("Arial, 14"),
                          bg="chartreuse2",
                          anchor="w")
    memberIdLabel.place(x=50, y=100, width=380, height=40);
    ## Membership Name Field
    nameLabel = Label(delSc,
                      text = "Name (placeholder)",
                      font=("Arial, 14"),
                      bg="chartreuse2",
                      anchor="w")
    nameLabel.place(x=50, y=140, width=380, height=40);
    ## Membership Faculty Input Field
    facLabel = Label(delSc,
                     text = "Faculty (placeholder)",
                     font=("Arial, 14"),
                     bg="chartreuse2",
                     anchor="w")
    facLabel.place(x=50, y=180, width=380, height=40);
    ## Membership Phone Input Field
    phoneLabel = Label(delSc,
                       text = "Phone (placeholder)",
                       font=("Arial, 14"),
                       bg="chartreuse2",
                       anchor="w")
    phoneLabel.place(x=50, y=220, width=380, height=40);
        ## Membership Faculty Input Field
    emailLabel = Label(delSc,
                       text = "Email (placeholder)",
                       font=("Arial, 14"),
                       bg="chartreuse2",
                       anchor="w")
    emailLabel.place(x=50, y=260, width=380, height=40);
    ## TO IMPLEMENT SQL FUNCTION FOR CONFIRM DELETION
    confirm = Button(delSc,
                     text="Confirm \n Deletion",
                     font=("Arial", 12,"bold"),
                     borderwidth=6,
                     bg="aquamarine",
                     command=destroyDelSc);
    confirm.place(x=20, y=300, width=180, height=80)
    ## Return to
    returnTo = Button(delSc,
                      text="Back to \n Delete \n Function",
                      font=("Arial", 12,"bold"),
                      borderwidth=6,
                      bg="aquamarine",
                      command=destroyDelSc);
    returnTo.place(x=250, y=300, width=180, height=80)
## Member Deletion Failed Window
def destroyDelFail():
    delFail.destroy();
def delFail():
    global delFail
    delFail = Toplevel();
    delFail.configure(bg="red")
    delFail.geometry("450x400")

    ## Error Title Label
    errorTitle = Label(delFail,
                        text = "Error!",
                        font=("Arial", 40,"bold"),
                        bg="red",
                        fg="yellow");
    errorTitle.place(x=0, y=100, width=450, height=100);

    ## Error Message Label
    errorMsg = Label(delFail,
                        text = "Member has loans,\n reservations or outstanding fines.",
                        font=("Arial", 16,"bold"),
                        bg="red",
                        fg="yellow");
    errorMsg.place(x=0, y=200, width=450, height=100);

    ## Return to
    errorMsg = Button(delFail,
                         text="Back to \n Delete \n Function",
                         font=("Arial", 12,"bold"),
                         borderwidth=6,
                         bg="aquamarine",
                         command=destroyDelFail);
    errorMsg.place(x=125, y=300, width=200, height=80)

## Member Deletion Menu
def goToMemMenuFromDelete():
    membershipMenu();
    destroyDeleteMenu();
    memMenu.lift()

def destroyDeleteMenu():
    deleteMemMenu.destroy();

def memberDeletion():    
    global deleteMemMenu
    deleteMemMenu = Toplevel()
    deleteMemMenu.geometry("750x420")

    ## Title Label
    deleteTitleLabel = Label(deleteMemMenu,
                                text = "To Delete Member, Please Enter Membership ID:",
                                font=("Arial, 18"),
                                bg="aquamarine");
    deleteTitleLabel.place(x=0, y=0, width=750, height=180);

    ## Membership Id Input Field
    deleteMemberIdLabel = Label(deleteMemMenu,
                                   text = "Membership ID",
                                   font=("Arial, 10"),
                                   bg="DodgerBlue3",
                                   fg="white")
    deleteMemberIdLabel.place(x=0, y=200, width=300, height=100);
    
    entryMemberId = Entry(deleteMemMenu,
                             font=('Arial',10,'normal'))
    entryMemberId.place(x=300, y=260, width=450, height=40);

    ## Membership Deletion Button
    deleteRecordButton = Button(deleteMemMenu,
                                   text = "Delete Member",
                                   font=("Arial, 18"),
                                   bg="aquamarine")
    deleteRecordButton.place(x=80, y=320, width=250, height=80);

    ## Return to Main Menu Button
    backButton = Button(deleteMemMenu,
                           text = "Back to Main Menu",
                           font=("Arial, 18"),
                           bg="aquamarine",
                           command=goToMemMenuFromDelete)
    backButton.place(x=420, y=320, width=250, height=80);

### Update Landing Window ###
def goToMemMenuFromUpdateLanding():
    membershipMenu();
    destroyUpdateLandingMenu();
    memMenu.lift()
def destroyUpdateLandingMenu():
    updateInputId.destroy();
def openUpdateMenu():
    destroyUpdateLandingMenu();
    updateMenu();
    updateMemMenu.lift();

def memberUpdateLanding():
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
                                   command=openUpdateMenu)
    updateRecordButton.place(x=80, y=320, width=250, height=80);
    ## Return to Main Menu Button
    backButton = Button(updateInputId,
                           text = "Back to Main Menu",
                           font=("Arial, 18"),
                           bg="aquamarine",
                           command=goToMemMenuFromUpdateLanding)
    backButton.place(x=420, y=320, width=250, height=80);

### Update Member Details Window ###
def goToMemMenuFromUpdate():
    membershipMenu();
    destroyUpdateMenu();
    memMenu.lift()
def destroyUpdateMenu():
    updateMemMenu.destroy();
    
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
                           command=goToMemMenuFromUpdate)
    backButton.place(x=420, y=710, width=250, height=80);


## Dont delete - used to start the app
startButton = Button(window, text = "Start", command = membershipMenu, fg = "lightblue",
                     bg = "black", font = ("Mincho", 20))
startButton.pack()
window.mainloop()


import tkinter as tk
from tkinter import filedialog
from PIL import ImageTk, Image

# Not added/To be fixed
# 1. Picture in membership Menu not showing up
# 2. Check which entry box looks nicer - either in deletion or creation
# 3. Complete SQLAlchemy functions
# 4. Flow control for various errors

### Membership Landing Window ###
def destroyMemMenu():
    memMenu.destroy();

def membershipMenu():
    global memMenu
    memMenu = tk.Toplevel();
    memMenu.geometry("1280x820")

    ## Title Label
    memTitleLabel = tk.Label(memMenu,
                             text = "Select one of the Options below:",
                             font=("Arial, 20"),
                             borderwidth = 4,
                             relief = "solid",
                             bg="paleturquoise1");
    memTitleLabel.place(x=140, y=0, width=1000, height=200);

    ## Picture Left Side

    # Not sure why pic is not showing but i rly want to fuking die
    im = ImageTk.PhotoImage(Image.open("als.jpg"))
    displayImg = tk.Label(memMenu, image=im);
    displayImg.place(x=0, y=220, width=400, height=180);

    ## Go to member creation menu
    memCreationButton = tk.Button(memMenu,
                                  text = "1. Creation",
                                  font=("Arial, 14"),
                                  bg="LightBlue",
                                  fg="white",
                                  command=memberCreation)
    memCreationButton.place(x=480, y=200, width=180, height=160);
    memCreationLabel = tk.Label(memMenu,
                                text="Membership creation",
                                anchor = "w",
                                font=('Times',14,'normal'))
    memCreationLabel.place(x=680, y=200, width=600, height=180);

    ## Go to member deletion menu
    memDeletionButton = tk.Button(memMenu,
                                  text = "2. Deletion",
                                  font=("Arial, 14"),
                                  bg="royalblue",
                                  fg="white",
                                  command=memberDeletion)
    memDeletionButton.place(x=480, y=360, width=180, height=160);
    memDeletionLabel = tk.Label(memMenu,
                                text="Membership deletion",
                                anchor = "w",
                                font=('Times',14,'normal'))
    memDeletionLabel.place(x=680, y=360, width=600, height=160);

    ## Go to member update menu
    memUpdateButton = tk.Button(memMenu,
                                text = "3. Update",
                                font=("Arial, 14"),
                                bg="SlateBlue",
                                fg="white",
                                command=memberUpdateLanding)
    memUpdateButton.place(x=480, y=520, width=180, height=160);
    memUpdateLabel = tk.Label(memMenu,
                              text="Membership update",
                              anchor = "w",
                              font=('Times',14,'normal'))
    memUpdateLabel.place(x=680, y=520, width=600, height=160);

    goMainFromMemMenu = tk.Button(memMenu,
                                  font=("Arial, 24"),
                                  text = "Back to Main Menu",
                                  bg="aquamarine",
                                  borderwidth = 4,
                                  relief = "solid",
                                  command=destroyMemMenu)
    goMainFromMemMenu.place(x=140,y=700, width=1000, height=80);


### Member Creation Window ###

def destroyCreateMenu():
    createMemMenu.destroy();

def memberCreation():

    # To add:
    # If-Else for Success/Error messages
    # SQLAlchemy retrieval
    
    global createMemMenu
    createMemMenu = tk.Toplevel()
    createMemMenu.geometry("750x820")

    ## Title Label
    createTitleLabel = tk.Label(createMemMenu,
                                text = "To Create Member, Please Enter Requested Information Below:",
                                font=("Arial, 18"),
                                bg="aquamarine");
    createTitleLabel.place(x=0, y=0, width=750, height=200);

    ## Membership Id Input Field
    createMemberIdLabel = tk.Label(createMemMenu,
                                   text = "Membership ID",
                                   font=("Arial, 10"),
                                   bg="DodgerBlue3",
                                   fg="white")
    createMemberIdLabel.place(x=0, y=200, width=300, height=100);
    
    entryMemberId = tk.Entry(createMemMenu,
                             font=('Arial',10,'normal'))
    entryMemberId.place(x=300, y=260, width=450, height=40);

    ## Membership Name Input Field
    createNameLabel = tk.Label(createMemMenu,
                               text = "Name",
                               font=("Arial, 10"),
                               bg="DodgerBlue2",
                               fg="white")
    createNameLabel.place(x=0, y=300, width=300, height=100);

    entryName = tk.Entry(createMemMenu,
                         font=('Arial',10,'normal'))
    entryName.place(x=300, y=360, width=450, height=40);

    ## Membership Faculty Input Field
    createFacLabel = tk.Label(createMemMenu,
                              text = "Faculty",
                              font=("Arial, 10"),
                              bg="SkyBlue2",
                              fg="white")
    createFacLabel.place(x=0, y=400, width=300, height=100);

    entryFac = tk.Entry(createMemMenu,
                        font=('Arial',10,'normal'))
    entryFac.place(x=300, y=460, width=450, height=40);


    ## Membership Phone Input Field
    createPhoneLabel = tk.Label(createMemMenu,
                                text = "Phone Number",
                                font=("Arial, 10"),
                                bg="LightSkyBlue1",
                                fg="white")
    createPhoneLabel.place(x=0, y=500, width=300, height=100);
    
    entryPhone = tk.Entry(createMemMenu,
                          font=('Arial',10,'normal'))
    entryPhone.place(x=300, y=560, width=450, height=40);

    ## Membership Email Input Field
    createEmailLabel = tk.Label(createMemMenu,
                                text = "Email Address",
                                font=("Arial, 10"),
                                bg="LightBlue1",
                                fg="white")
    createEmailLabel.place(x=0, y=600, width=300, height=100);

    entryEmail = tk.Entry(createMemMenu,
                          font=('Arial',10,'normal'))
    entryEmail.place(x=300, y=660, width=450, height=40);

    ## Membership Creation Button
    createRecordButton = tk.Button(createMemMenu,
                                   text = "Create Member",
                                   font=("Arial, 18"),
                                   bg="aquamarine")
    createRecordButton.place(x=80, y=710, width=250, height=80);

    ## Return to Main Menu Button
    backButton = tk.Button(createMemMenu,
                           text = "Back to Main Menu",
                           font=("Arial, 18"),
                           bg="aquamarine",
                           command=destroyCreateMenu)
    backButton.place(x=420, y=710, width=250, height=80);

### Membership Deletion Window ###

def destroyDeleteMenu():
    deleteMemMenu.destroy();

def memberDeletion():
    # To add:
    # If-Else for Success/Error messages
    # SQLAlchemy retrieval
    
    global deleteMemMenu
    deleteMemMenu = tk.Toplevel()
    deleteMemMenu.geometry("750x420")

    ## Title Label
    deleteTitleLabel = tk.Label(deleteMemMenu,
                                text = "To Delete Member, Please Enter Membership ID:",
                                font=("Arial, 18"),
                                bg="aquamarine");
    deleteTitleLabel.place(x=0, y=0, width=750, height=180);

    ## Membership Id Input Field
    deleteMemberIdLabel = tk.Label(deleteMemMenu,
                                   text = "Membership ID",
                                   font=("Arial, 10"),
                                   bg="DodgerBlue3",
                                   fg="white")
    deleteMemberIdLabel.place(x=0, y=200, width=300, height=100);
    
    entryMemberId = tk.Entry(deleteMemMenu,
                             font=('Arial',10,'normal'))
    entryMemberId.place(x=300, y=260, width=450, height=40);

    ## Membership Deletion Button
    deleteRecordButton = tk.Button(deleteMemMenu,
                                   text = "Delete Member",
                                   font=("Arial, 18"),
                                   bg="aquamarine")
    deleteRecordButton.place(x=80, y=320, width=250, height=80);

    ## Return to Main Menu Button
    backButton = tk.Button(deleteMemMenu,
                           text = "Back to Main Menu",
                           font=("Arial, 18"),
                           bg="aquamarine",
                           command=destroyDeleteMenu)
    backButton.place(x=420, y=320, width=250, height=80);

### Update Landing Window ###
def destroyUpdateLandingMenu():
    updateInputId.destroy();
    
def memberUpdateLanding():
    global updateInputId
    updateInputId = tk.Toplevel()
    updateInputId.geometry("750x420")

    ## Title Label
    updateTitleLabel = tk.Label(updateInputId,
                                text = "To Update a Member, Please Enter Membership ID:",
                                font=("Arial, 18"),
                                bg="aquamarine");
    updateTitleLabel.place(x=0, y=0, width=750, height=180);

    ## Membership Id Input Field
    updateMemberIdLabel = tk.Label(updateInputId,
                                   text = "Membership ID",
                                   font=("Arial, 10"),
                                   bg="DodgerBlue3",
                                   fg="white")
    updateMemberIdLabel.place(x=0, y=200, width=300, height=100);
    
    entryMemberId = tk.Entry(updateInputId,
                             font=('Arial',10,'normal'))
    entryMemberId.place(x=300, y=260, width=450, height=40);

    ## Membership Update Button
    updateRecordButton = tk.Button(updateInputId,
                                   text = "Update Member",
                                   font=("Arial, 18"),
                                   bg="aquamarine",
                                   command=updateMenu)
    updateRecordButton.place(x=80, y=320, width=250, height=80);

    ## Return to Main Menu Button
    backButton = tk.Button(updateInputId,
                           text = "Back to Main Menu",
                           font=("Arial, 18"),
                           bg="aquamarine",
                           command=destroyUpdateLandingMenu)
    backButton.place(x=420, y=320, width=250, height=80);

### Update Member Details Window ###
    
def destroyUpdateMenu():
    updateMemMenu.destroy();
    
def updateMenu():
    # To add:
    # If-Else for Success/Error messages
    # SQLAlchemy retrieval
    
    updateInputId.destroy();
    
    global updateMemMenu
    updateMemMenu = tk.Toplevel()
    updateMemMenu.geometry("750x820")

    ## Title Label
    updateTitleLabel = tk.Label(updateMemMenu,
                                text = "Please Enter Requested Information Below:",
                                font=("Arial, 18"),                                
                                bg="aquamarine");
    updateTitleLabel.place(x=0, y=0, width=750, height=200);

    ## Membership Id Input Field
    updateMemberIdLabel = tk.Label(updateMemMenu,
                                   text = "Membership ID",
                                   borderwidth=2,
                                   relief="solid",
                                   font=("Arial, 10"),
                                   bg="SlateBlue")
    updateMemberIdLabel.place(x=0, y=200, width=300, height=100);
    
    enteredMemberId = tk.Label(updateMemMenu,
                                   text = "A01234567B",
                                   borderwidth=2,
                                   relief="solid",
                                   font=("Arial, 12"))
    enteredMemberId.place(x=300, y=260, width=450, height=40);

    ## Membership Name Input Field
    updateNameLabel = tk.Label(updateMemMenu,
                               text = "Name",
                               font=("Arial, 10"),
                               borderwidth=2,
                               relief="solid",
                               bg="SlateBlue",
                               fg="white")
    updateNameLabel.place(x=0, y=300, width=300, height=100);

    entryName = tk.Entry(updateMemMenu,
                         font=('Arial',10,'normal'))
    entryName.place(x=300, y=360, width=450, height=40);

    ## Membership Faculty Input Field
    updateFacLabel = tk.Label(updateMemMenu,
                              text = "Faculty",
                              font=("Arial, 10"),
                              borderwidth=2,
                              relief="solid",
                              bg="SlateBlue",
                              fg="white")
    updateFacLabel.place(x=0, y=400, width=300, height=100);

    entryFac = tk.Entry(updateMemMenu,
                        font=('Arial',10,'normal'))
    entryFac.place(x=300, y=460, width=450, height=40);


    ## Membership Phone Input Field
    updatePhoneLabel = tk.Label(updateMemMenu,
                                text = "Phone Number",
                                font=("Arial, 10"),
                                borderwidth=2,
                                relief="solid",
                                bg="SlateBlue",
                                fg="white")
    updatePhoneLabel.place(x=0, y=500, width=300, height=100);
    
    entryPhone = tk.Entry(updateMemMenu,
                          font=('Arial',10,'normal'))
    entryPhone.place(x=300, y=560, width=450, height=40);

    ## Membership Email Input Field
    updateEmailLabel = tk.Label(updateMemMenu,
                                text = "Email Address",
                                font=("Arial, 10"),
                                borderwidth=2,
                                relief="solid",
                                bg="SlateBlue",
                                fg="white")
    updateEmailLabel.place(x=0, y=600, width=300, height=100);

    entryEmail = tk.Entry(updateMemMenu,
                          font=('Arial',10,'normal'))
    entryEmail.place(x=300, y=660, width=450, height=40);

    ## Membership Creation Button
    updateRecordButton = tk.Button(updateMemMenu,
                                   text = "Update Member",
                                   font=("Arial, 18"),
                                   bg="aquamarine")
    updateRecordButton.place(x=80, y=710, width=250, height=80);

    ## Return to Main Menu Button
    backButton = tk.Button(updateMemMenu,
                           text = "Back to Main Menu",
                           font=("Arial, 18"),
                           bg="aquamarine",
                           command=destroyUpdateMenu)
    backButton.place(x=420, y=710, width=250, height=80);




### LANDING PAGE WINDOW ###
window = tk.Tk()


# Delete openLoans and openBooks
def openLoans():
    window.destroy()
    import loans
    
def openBooks():
    window.destroy()
    import books
    
buttonMember = tk.Button(window,
                         text = "Membership",
                         width=25,
                         height=5,
                         bg="indianred",
                         command=membershipMenu)

buttonBooks = tk.Button(window,
                        text = "Books",
                        width=25,
                        height=5,
                        bg="aquamarine",
                        command=openBooks)

buttonLoans = tk.Button(window,
                        text = "Loans",
                        width=25,
                        height=5,
                        bg="darksalmon",
                        command=openLoans)

buttonReservation = tk.Button(window,
                              text = "Reservation",
                              width=25,
                              height=5,
                              bg="darkseagreen")

buttonFines = tk.Button(window,
                        text = "Fines",
                        width=25,
                        height=5,
                        bg="cadetblue")

buttonReports = tk.Button(window,
                          text = "Reports",
                          width=25,
                          height=5,
                          bg="peru")

buttonMember.grid(row=0, column=0);
buttonBooks.grid(row=1, column=0);
buttonLoans.grid(row=2, column=0);
buttonReservation.grid(row=0, column=1);
buttonFines.grid(row=1, column=1);
buttonReports.grid(row=2, column=1);






window.mainloop()


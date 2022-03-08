import tkinter as tk
from PIL import ImageTk, Image
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
   
def destroyDelSc():
    delSc.destroy();
    
def delSuccess():
    global delSc
    delSc = tk.Toplevel();
    delSc.configure(bg="chartreuse2")
    delSc.geometry("450x400")

    # ## Title Label
    titleLabel = tk.Label(delSc,
                                text = "Please Confirm Details to \n Be Correct",
                                font=("Arial", 20, "bold"),
                                bg="chartreuse2");
    titleLabel.place(x=0, y=0, width=450, height=140);

    ## Membership Id Field
    memberIdLabel = tk.Label(delSc,
                             text = "Membership ID (placeholder)",
                             font=("Arial, 14"),
                             bg="chartreuse2",
                             anchor="w")
    memberIdLabel.place(x=50, y=100, width=380, height=40);
    ## Membership Name Field
    nameLabel = tk.Label(delSc,
                         text = "Name (placeholder)",
                         font=("Arial, 14"),
                         bg="chartreuse2",
                         anchor="w")
    nameLabel.place(x=50, y=140, width=380, height=40);
    ## Membership Faculty Input Field
    facLabel = tk.Label(delSc,
                        text = "Faculty (placeholder)",
                        font=("Arial, 14"),
                        bg="chartreuse2",
                        anchor="w")
    facLabel.place(x=50, y=180, width=380, height=40);
    ## Membership Phone Input Field
    phoneLabel = tk.Label(delSc,
                          text = "Phone (placeholder)",
                          font=("Arial, 14"),
                          bg="chartreuse2",
                          anchor="w")
    phoneLabel.place(x=50, y=220, width=380, height=40);
        ## Membership Faculty Input Field
    emailLabel = tk.Label(delSc,
                          text = "Email (placeholder)",
                          font=("Arial, 14"),
                          bg="chartreuse2",
                          anchor="w")
    emailLabel.place(x=50, y=260, width=380, height=40);
    ## TO IMPLEMENT SQL FUNCTION FOR CONFIRM DELETION
    confirm = tk.Button(delSc,
                        text="Confirm \n Deletion",
                        font=("Arial", 12,"bold"),
                        borderwidth=6,
                        bg="aquamarine",
                        command=destroyDelSc);
    confirm.place(x=20, y=300, width=180, height=80)
    ## Return to
    returnTo = tk.Button(delSc,
                         text="Back to \n Delete \n Function",
                         font=("Arial", 12,"bold"),
                         borderwidth=6,
                         bg="aquamarine",
                         command=destroyDelSc);
    returnTo.place(x=250, y=300, width=180, height=80)
def destroyDelFail():
    delFail.destroy();
    
def delFail():
    global delFail
    delFail = tk.Toplevel();
    delFail.configure(bg="red")
    delFail.geometry("450x400")

    ## Error Title Label
    errorTitle = tk.Label(delFail,
                        text = "Error!",
                        font=("Arial", 40,"bold"),
                        bg="red",
                        fg="yellow");
    errorTitle.place(x=0, y=100, width=450, height=100);

    ## Error Message Label
    errorMsg = tk.Label(delFail,
                        text = "Member has loans,\n reservations or outstanding fines.",
                        font=("Arial", 16,"bold"),
                        bg="red",
                        fg="yellow");
    errorMsg.place(x=0, y=200, width=450, height=100);

    ## Return to
    errorMsg = tk.Button(delFail,
                         text="Back to \n Delete \n Function",
                         font=("Arial", 12,"bold"),
                         borderwidth=6,
                         bg="aquamarine",
                         command=destroyDelFail);
    errorMsg.place(x=125, y=300, width=200, height=80)



delFail()

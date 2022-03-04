import tkinter as tk
from PIL import ImageTk, Image

def destroyButton():
    delFailWin.destroy();
    

def deletionFailWindow():
    global delFailWin
    delFailWin = tk.Toplevel();
    delFailWin.configure(bg="red")
    delFailWin.geometry("450x450")

    ## Error Title Label
    errorTitle = tk.Label(delFailWin,
                        text = "Error!",
                        font=("Arial", 40,"bold"),
                        bg="red",
                        fg="yellow");
    errorTitle.place(x=0, y=0, width=450, height=250);

    ## Error Message Label
    errorMsg = tk.Label(delFailWin,
                        text = "Book already added;\n Duplicate, Missing or\n Incomplete fields.",
                        font=("Arial", 12,"bold"),
                        bg="red",
                        fg="yellow");
    errorMsg.place(x=0, y=250, width=450, height=100);

    ## Return to
    errorMsg = tk.Button(delFailWin,
                         text="Back to Acquisition Function",
                         font=("Arial", 12,"bold"),
                         borderwidth=4,
                         bg="aquamarine",
                         command=destroyButton);
    errorMsg.place(x=75, y=350, width=300, height=80)
    

deletionFailWindow()

import tkinter as tk

window = tk.Tk()

# Functions for navigation

def backToMenu():
    window.destroy()
    import membership

def updateMem():
    window.destroy()
    import memberUpdate2

# UI Design

buttonTitle = tk.Label(text = "To Update a Member, Please Enter Membership ID:",
                       width=50,
                       height=5,
                       bg="aquamarine")

labelMember = tk.Label(text = "Membership ID",
                       width=25,
                       height=5,
                       bg="DodgerBlue3",
                       fg="white")
entryMember = tk.Entry(font=('calibre',10,'normal'))

buttonUpdate = tk.Button(text = "Update Member",
                         width=35,
                         height=5,
                         bg="aquamarine",
                         command=updateMem)

buttonBack = tk.Button(text = "Back to Main Menu",
                       width=35,
                       height=5,
                       bg="aquamarine",
                       command=backToMenu)

buttonTitle.grid(row=0, columnspan=2);

labelMember.grid(row=1, column=0);

entryMember.grid(row=1, column=1);

buttonUpdate.grid(row=2, column=0);

buttonBack.grid(row=2, column=1);



window.mainloop()

import tkinter as tk

window = tk.Tk()

# Functions for navigation

def backToMain():
    window.destroy()
    import landingPage

def createMember():
    window.destroy()
    import memberCreation

def deleteMember():
    window.destroy()
    import memberDeletion

def updateMember():
    window.destroy()
    import memberUpdate

#UI design

buttonTitle = tk.Label(text = "Select one of the Options below:", width=50, height=5, bg="aquamarine")

buttonCreate = tk.Button(text = "1. Creation",
                         width=25,
                         height=5,
                         bg="LightBlue",
                         fg="white",
                         command=createMember)
textCreate = tk.Label(text="Membership creation",
                      height=5,
                      font=('calibre',10,'normal'))

buttonDel = tk.Button(text = "2. Deletion",
                      width=25,
                      height=5,
                      bg="royalblue",
                      fg="white",
                      command=deleteMember)
textDel = tk.Label(text="Membership deletion",
                   height=5,
                   font=('calibre',10,'normal'))

buttonUpdate = tk.Button(text = "3. Update",
                         width=25,
                         height=5,
                         bg="SlateBlue",
                         fg="white",
                         command=updateMember)
textUpdate = tk.Label(text="Membership update",
                      height=5,
                      font=('calibre',10,'normal'))

##
buttonBack = tk.Button(text = "Back to Main Menu",
                       width=25,
                       height=5,
                       bg="aquamarine",
                       command=backToMain)


buttonTitle.grid(row=0, columnspan=2);

buttonCreate.grid(row=1, column=0);

buttonDel.grid(row=2, column=0);

buttonUpdate.grid(row=3, column=0);

textCreate.grid(row=1, column=1);

textDel.grid(row=2, column=1);

textUpdate.grid(row=3, column=1);

buttonBack.grid(row=4, columnspan=2);



window.mainloop()

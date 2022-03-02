import tkinter as tk

window = tk.Tk()

titleLabel = tk.Label(text = "To Delete Member, Please Enter Membership ID:", width=50, height=5, bg="aquamarine", borderwidth=7,relief="raised")

buttonMember = tk.Label(text = "Membership ID", width=25, height=5, bg="DodgerBlue3", fg="white")
entryMember = tk.Entry(font=('calibre',10,'normal'))


buttonCreate = tk.Button(text = "Delete Member", width=25, height=5, bg="aquamarine")

buttonBack = tk.Button(text = "Back to Membership Menu", width=25, height=5, bg="aquamarine")


titleLabel.grid(row=0, columnspan=2);

buttonMember.grid(row=1, column=0);

buttonCreate.grid(row=2, column=0);

entryMember.grid(row=1, column=1);

buttonBack.grid(row=2, column=1);



window.mainloop()

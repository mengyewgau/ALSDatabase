import tkinter as tk

window = tk.Tk()

buttonTitle = tk.Button(text = "To Create Member, Please Enter Requested Information Below:", width=50, height=5, bg="aquamarine")

buttonMember = tk.Label(text = "Membership ID", width=25, height=5, bg="DodgerBlue3", fg="white")
entryMember = tk.Text(height=5,font=('calibre',10,'normal'))

buttonName = tk.Label(text = "Name", width=25, height=5,bg="DodgerBlue2", fg="white")
entryName = tk.Entry(font=('calibre',10,'normal'))

buttonFac = tk.Label(text = "Faculty", width=25, height=5, bg="SkyBlue2", fg="white")
entryFac = tk.Entry(font=('calibre',10,'normal'))

buttonPhone = tk.Label(text = "Phone Number", width=25, height=5, bg="LightSkyBlue1", fg="white")
entryPhone = tk.Entry(font=('calibre',10,'normal'))

buttonEmail = tk.Label(text = "Email Address", width=25, height=5, bg="LightBlue1", fg="white")
entryEmail = tk.Entry(font=('calibre',10,'normal'))

buttonCreate = tk.Button(text = "Create Member", width=25, height=5, bg="aquamarine")

buttonBack = tk.Button(text = "Back to Main Menu", width=25, height=5, bg="aquamarine")


buttonTitle.grid(row=0, columnspan=2);

buttonMember.grid(row=1, column=0);

buttonName.grid(row=2, column=0);

buttonFac.grid(row=3, column=0);

buttonPhone.grid(row=4, column=0);

buttonEmail.grid(row=5, column=0);

buttonCreate.grid(row=6, column=0);

entryMember.grid(row=1, column=1);

entryName.grid(row=2, column=1);

entryFac.grid(row=3, column=1);

entryPhone.grid(row=4, column=1);

entryEmail.grid(row=5, column=1);

buttonBack.grid(row=6, column=1);



window.mainloop()

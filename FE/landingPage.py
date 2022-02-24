import tkinter as tk

window = tk.Tk()

buttonMember = tk.Button(text = "Membership", width=25, height=5, bg="indianred")

buttonBooks = tk.Button(text = "Books", width=25, height=5,bg="aquamarine")

buttonLoans = tk.Button(text = "Loans", width=25, height=5, bg="darksalmon")

buttonReservation = tk.Button(text = "Reservation", width=25, height=5, bg="darkseagreen")

buttonFines = tk.Button(text = "Fines", width=25, height=5, bg="cadetblue")

buttonReports = tk.Button(text = "Reports", width=25, height=5,bg="peru")



buttonMember.grid(row=0, column=0);

buttonBooks.grid(row=1, column=0);

buttonLoans.grid(row=2, column=0);

buttonReservation.grid(row=0, column=1);

buttonFines.grid(row=1, column=1);

buttonReports.grid(row=2, column=1);



window.mainloop()


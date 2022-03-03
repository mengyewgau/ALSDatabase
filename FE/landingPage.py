import tkinter as tk
from memberFull import *

## Created as template for landing page

### LANDING PAGE FUNCTIONS ###
window = tk.Tk()

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


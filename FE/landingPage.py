import tkinter as tk
from PIL import ImageTk, Image


## Created as template for landing page

### LANDING PAGE FUNCTIONS ###
window = tk.Tk()
window.geometry("1280x750");
window.configure(bg="white")

def openLoans():
    return
def openBooks():
    import books
    
def membershipMenu():
    return

## (ALS) title centred in the screen
titleLabel = tk.Label(window,
                      text = "(ALS)",
                      font=("calibre, 40"),
                      bg="white")
titleLabel.place(x=0,y=20, width=1280, height=100)

## First row, leftmost button and icon
global memIm
memIm = ImageTk.PhotoImage(Image.open("membersIm.jpg").resize((250,200)))
displayMemIm = tk.Label(window, image=memIm);
displayMemIm.place(x=200, y=120, width=250, height=200);

buttonMember = tk.Button(window,
                         text = "Membership",
                         font=("Arial, 18"),
                         bg="indianred",
                         command=membershipMenu)
buttonMember.place(x=200, y=325, width=250, height=50)

## First row, middle button and icon
global bookIm
bookIm = ImageTk.PhotoImage(Image.open("booksIm.jpg").resize((250,200)))
displayBkIm = tk.Label(window, image=bookIm);
displayBkIm.place(x=515, y=120, width=250, height=200);

buttonBooks = tk.Button(window,
                        text = "Books",
                        font=("Arial, 18"),
                        bg="aquamarine",
                        command=openBooks)
buttonBooks.place(x=515, y=325, width=250, height=50)


## First row, rightmost button and icon
global loanIm
loanIm = ImageTk.PhotoImage(Image.open("loansIm.jpg").resize((250,200)))
displayLoanIm = tk.Label(window, image=loanIm);
displayLoanIm.place(x=830, y=120, width=250, height=200);

buttonLoans = tk.Button(window,
                        text = "Loans",
                        font=("Arial, 18"),
                        bg="darksalmon",
                        command=openLoans)
buttonLoans.place(x=830, y=325, width=250, height=50)

## Second row, leftmost button and icon
global reserveIm
reserveIm = ImageTk.PhotoImage(Image.open("reserveIm.jpg").resize((250,200)))
displayResIm = tk.Label(window, image=reserveIm);
displayResIm.place(x=200, y=410, width=250, height=200);

buttonReservation = tk.Button(window,
                              text = "Reservation",
                              font=("Arial, 18"),
                              bg="darkseagreen")
buttonReservation.place(x=200, y=615, width=250, height=50)

## Second row, middle button and icon
global fineIm
fineIm = ImageTk.PhotoImage(Image.open("fineIm.jpg").resize((250,200)))
displayFineIm = tk.Label(window, image=fineIm);
displayFineIm.place(x=515, y=410, width=250, height=200);

buttonFines = tk.Button(window,
                        text = "Fines",
                        font=("Arial, 18"),
                        bg="cadetblue")
buttonFines.place(x=515, y=615, width=250, height=50)


## Second row, rightmost button and icon
global reportIm
reportIm = ImageTk.PhotoImage(Image.open("reportIm.jpg").resize((250,200)))
displayReportIm = tk.Label(window, image=reportIm);
displayReportIm.place(x=830, y=410, width=250, height=200);

buttonReports = tk.Button(window,
                          text = "Reports",
                          font=("Arial, 18"),
                          bg="peru")
buttonReports.place(x=830, y=615, width=250, height=50)


window.mainloop()


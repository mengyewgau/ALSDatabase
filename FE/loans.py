import tkinter as tk

window = tk.Tk()

def openBorrow():
    window.destroy()
    import loansBorrow

def openReturn():
    window.destroy()
    import loansReturn

def goBack():
    window.destroy()
    import landingPage

homeButton = tk.Button(text = "Back",
                         width=10,
                         height=2,
                         bg="AntiqueWhite",
                         command=goBack)

buttonBorrow = tk.Button(text = "Borrow",
                         width=25,
                         height=5,
                         bg="indianred",
                         command=openBorrow)

buttonReturn = tk.Button(text = "Return",
                         width=25,
                         height=5,
                         bg="aquamarine",
                         command=openReturn)

buttonBorrow.grid(row=0, column=0);

buttonReturn.grid(row=1, column=0);

homeButton.grid(row=2, column=0);

window.mainloop()


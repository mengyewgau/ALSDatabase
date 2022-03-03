import tkinter as tk

window = tk.Tk()

def openAcquisition():
    window.destroy()
    import bookAcquisition

def openWithdrawal():
    top = tk.Toplevel()
    top.title('Withdrawal')
    import bookWithdrawal

def goBack():
    window.destroy()
    import landingPage

buttonAcquisition = tk.Button(
    text = "Acquisition",
    width = 25,
    height = 5,
    bg = "dodgerBlue2",
    command = openAcquisition)

buttonWithdrawal = tk.Button(
    text = "Withdrawal",
    width = 25,
    height = 5,
    bg = "SteelBlue2",
    command = openWithdrawal)

buttonBack = tk.Button(
    text = "Back",
    width = 10,
    height = 3,
    bg = "AntiqueWhite",
    command = goBack)

buttonAcquisition.grid(row=0, column=0)
buttonWithdrawal.grid(row=1, column=0)
buttonBack.grid(row=2, column=0)

window.mainloop()

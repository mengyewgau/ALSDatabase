import tkinter as tk
from PIL import ImageTk, Image

def openAcquisition():
    import bookAcquisition

def openWithdrawal():
    import bookWithdrawal

def goBack():
    import landingPage

##Book Page Background
window = tk.Tk()
window.geometry("1280x750");
window.configure(bg="Slategray2")

##Book Page Header
bookLabel = tk.Label(window,
                     text = "Please select one of the following options:",
                     font=("calibre", 20, "bold"),
                     bg = "Slategray1")
bookLabel.place(x=0,y=0, width=1280, height=80)

##Book Image Leftmost Label
global bookIm
memIm = ImageTk.PhotoImage(Image.open("booksIm.jpg").resize((700,700)))
displayBookIm = tk.Label(window,
                         image=memIm);
displayBookText = tk.Label(window,
                         text = "Books",
                         font = ("calibre", 30, "italic", "bold"),
                         fg = "lavender",
                         bg = "black")
displayBookIm.place(x=40, y=160, width = 500, height = 500);
displayBookText.place(x=160, y=560, width = 250, height = 70);

##Acquisition Button
buttonAcquisition = tk.Button(
    text = "Acquisition",
    font = ("calibre", 30, "bold"),
    fg = "lavender blush",
    bg = "dodgerBlue2",
    command = openAcquisition)

buttonAcquisition.place(x=580, y=250, width=650, height=100)

##Withdrawal Button
buttonWithdrawal = tk.Button(
    text = "Withdrawal",
    font = ("calibre", 30, "bold"),
    fg = "lavender blush",
    bg = "SteelBlue2",
    command = openWithdrawal)

buttonWithdrawal.place(x=580, y=450, width=650, height=100)

##Back Button
buttonBack = tk.Button(
    text = "Back",
    font = ("calibre", 15, "bold"),
    fg = "grey39",
    bg = "snow3",
    command = goBack)

buttonBack.place(x=1090, y=650, width=140, height=40)

window.mainloop()

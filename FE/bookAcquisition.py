import tkinter as tk

window = tk.Tk()
window.title("Acquisition")

def goBack():
    window.destroy()
    import books

label = tk.Label(
    window,
    text = "Acquisition Under Construction",
    font=("lucida", 20))

buttonBack = tk.Button(
    text = "Back",
    width = 10,
    height = 3,
    bg = "AntiqueWhite",
    command = goBack)

label.pack()
buttonBack.pack()

window.mainloop()

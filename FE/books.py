import tkinter as tk

window = tk.Tk()

buttonBorrow = tk.Button(text = "Borrow", width=25, height=5, bg="indianred")

buttonReturn = tk.Button(text = "Return", width=25, height=5,bg="aquamarine")


buttonBorrow.grid(row=0, column=0);

buttonReturn.grid(row=1, column=0);

window.mainloop()


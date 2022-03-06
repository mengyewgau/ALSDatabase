import tkinter as tk

window = tk.Tk()
window.title("Reservations")

def openBookReservation():
    window.destroy()

def openReservationCancellation():
    window.destroy()

def goHome():
    window.destroy()
    import landingPage

buttonBookReservation = tk.Button(window, text="Reserve a Book", width=25, height=5, bg="aquamarine", command=openBookReservation)

buttonReservationCancellation = tk.Button(window, text="Cancel Reservation", width=25, height=5, bg="indianred", command=openReservationCancellation)

buttonHome = tk.Button(window, text = "Home", width=10, height=2, bg="antiquewhite", command=goHome)

buttonBookReservation.grid(row=0, column=0)

buttonReservationCancellation.grid(row=1, column=0)

buttonHome.grid(row=2, column=0)

window.mainloop()

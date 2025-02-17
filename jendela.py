from tkinter import *

window= Tk()
lebar=500
tinggi=400
x=500
y=100

screenwidh = window.winfo_screenwidth()
screenheight = window.winfo_screenheight()

newx = int((screenwidh/2) - (lebar/2))
newy = int((screenheight/2) - (tinggi/2)-100)


window.geometry(f"{lebar}x{tinggi}+{newx}+{newy}")

window.mainloop()

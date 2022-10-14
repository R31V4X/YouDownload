from tkinter import *
from tkinter.ttk import *
import pytube

window = Tk()
window.geometry("300x200")

label  = Label(window, text="Downloading.")
label.pack()

def loop(i=0):
    label["text"] = "Downloading." + str((i % 3) * ".")
    window.after(400, loop, i+1)
loop()


window.mainloop()
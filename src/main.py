from tkinter import *
from tkinter.ttk import *
import pytube
import os
from PIL import ImageTk, Image


root = Tk()

WIN_WIDTH, WIN_HEIGHT = 500, 400
WIN_X, WIN_Y = int(root.winfo_screenwidth()/2 - WIN_WIDTH/2), int(root.winfo_screenheight()/2 - WIN_HEIGHT/2)

WIN_X_MID = WIN_WIDTH/2

root.title("YouDownload")
root.iconbitmap("src/icon.ico")
root.geometry(f"{WIN_WIDTH}x{WIN_HEIGHT}+{WIN_X}+{WIN_Y}")
root.resizable(False, False)

# logo
logo_size = (100, 100)
logo = ImageTk.PhotoImage(Image.open("src/logo.png").resize(logo_size, Image.ANTIALIAS))
logo_image = Label(root, image=logo)
logo_image.place(anchor=CENTER, x=WIN_X_MID, y=75)

# YouDownloadLabel
youdl_label = Label(root, text="YouDownload", font="Poppins 20 bold")
youdl_label.place(anchor=CENTER, x = WIN_X_MID, y = 150)

# Enter link label
enter_link_label = Label(root, text="Enter the link of the video to download: ")
enter_link_label.place(x=20, y=200)



root.mainloop()


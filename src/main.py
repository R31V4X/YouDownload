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
logo = ImageTk.PhotoImage(Image.open("src/logo.png").resize(logo_size))
logo_image = Label(root, image=logo)
logo_image.place(anchor=CENTER, x=WIN_X_MID, y=75)

# YouDownloadLabel
youdl_label = Label(root, text="YouDownload", font="Poppins 20 bold")
youdl_label.place(anchor=CENTER, x = WIN_X_MID, y = 150)

# Enter link label
enter_link_label = Label(root, text="Enter the link of the video to download: ")
enter_link_label.place(x=20, y=200)

# Field for link
field = Entry(root, width=37)
field.place(x = 245, y = 199)


# Btn pressedd
state_label = Label(root, text="")
def btn_pressed():
    global state_label
    link = field.get()
    try:
        video = pytube.YouTube(link)
    except:
        state_label.config(text="Video Not Found!")
        state_label.place(anchor=CENTER, x = WIN_X_MID, y = 270)
        return None

    state_label.config(text="Video Found!")
    state_label.place(anchor=CENTER, x = WIN_X_MID, y = 270)

# Dl Button
download_btn = Button(root, text="Download", width=30, command=btn_pressed)
download_btn.place(anchor=CENTER, x = WIN_X_MID, y=240)



root.mainloop()


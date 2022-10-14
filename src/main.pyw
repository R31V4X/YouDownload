from cProfile import run
from tkinter import *
from tkinter.ttk import *
import pytube
import os
import sys
from PIL import ImageTk, Image


root = Tk()

WIN_WIDTH, WIN_HEIGHT = 500, 400
WIN_X, WIN_Y = int(root.winfo_screenwidth()/2 - WIN_WIDTH/2), int(root.winfo_screenheight()/2 - WIN_HEIGHT/2)
WIN_X_MID = WIN_WIDTH/2

root.title("YouDownload")
root.iconbitmap("src/icon.ico")
root.geometry(f"{WIN_WIDTH}x{WIN_HEIGHT}+{WIN_X}+{WIN_Y}")
root.resizable(False, False)

# Path
home = os.path.expanduser("~")
path_download = os.path.join(home, "Downloads")

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

# Progress bar
progress_bar = Progressbar(root, orient = "horizontal", length=350, mode="determinate")



# Progress bar progress
def percent(bytes_remaning, size):
    return (((size-bytes_remaning)/size)*100)

progress = 1
def on_progress(stream, chunk, bytes_remaining):
    global progress
    size = stream.filesize
    progress = percent(bytes_remaining, size)
    progress_bar["value"] = progress
    root.update()


# Complete
complete = False
def complete(stream, path):
    global complete
    downloading_label["text"] = "Download Successful!"
    complete = True



# Downloading label
downloading_label = Label(root, text="Downloading.")

# Def downloading loop
def loop(i=0):
    global complete
    if complete == True:
        return None
    downloading_label["text"] = "Downloading." + str((i % 3) * ".")
    root.after(400, loop, i+1)

# Btn pressed
state_label = Label(root, text="")


def btn_pressed():
    global state_label
    link = field.get()
    try:
        video_link = pytube.YouTube(link, on_progress_callback=on_progress, on_complete_callback=complete)
    except:
        state_label.config(text="Video Not Found!")
        state_label.place(anchor=CENTER, x = WIN_X_MID, y = 270)
        return None
        
    # State
    state_label.config(text="Video Found!")
    state_label.place(anchor=CENTER, x = WIN_X_MID, y = 270)


    progress_bar.place(anchor=CENTER, x = WIN_X_MID, y = 315)
    downloading_label.place(anchor=CENTER, x= WIN_X_MID, y = 350)
    loop()


    # Get youtube video
    video = video_link.streams.get_highest_resolution().download(path_download)


# Dl Button
download_btn = Button(root, text="Download", width=30, command=btn_pressed)
download_btn.place(anchor=CENTER, x = WIN_X_MID, y=240)



root.mainloop()


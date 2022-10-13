from tkinter import *
from tkinter.ttk import *

root = Tk()

WIN_WIDTH, WIN_HEIGHT = 500, 400
WIN_X, WIN_Y = int(root.winfo_screenwidth()/2 - WIN_WIDTH/2), int(root.winfo_screenheight()/2 - WIN_HEIGHT/2)

root.title("YouDownload")
root.iconbitmap("src/icon.ico")
root.geometry(f"{WIN_WIDTH}x{WIN_HEIGHT}+{WIN_X}+{WIN_Y}")





root.mainloop()


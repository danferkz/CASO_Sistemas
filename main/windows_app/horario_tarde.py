from tkinter import *
from tkinter import ttk
import windows_app.RECARGA as reca
import windows_app.RECARGA as recar_train
import helpers.readfiles as readfiles
import windows_app.horario_tarde as tarde
from PIL import Image, ImageTk
from tkinter import Tk, Label, Button,Entry, Frame, END

def horaTARDE(root, mainFrame):
    root.title("Horarios de líneas de tren")
    mainFrame.destroy()
    mainFrame = Frame()
    mainFrame.config(width = "380", height = "676")
    mainFrame.pack()
    my_path = readfiles.Route()
    global logo, vaerDropBox
    logo = ImageTk.PhotoImage(Image.open(my_path + "\main\images\HORARIO2.png"))
    Label(mainFrame, image = logo).place(relx = 0, rely = 0)

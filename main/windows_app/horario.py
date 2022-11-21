from tkinter import *
import windows_app.horario as inic
import helpers.readfiles as readfiles
from PIL import Image, ImageTk
from tkinter import Tk, Label, Button,Entry, Frame, END

#* Estructura de la ventana del Dashboard general.
def horario(root, mainframe):
    root.title("Horarios de líneas de tren")

    mainframe.destroy()
    mainframe = Frame()
    mainframe.config(width = "480", height = "1034")
    mainframe.pack()
    my_path = readfiles.Route()

    global logo

    logo = ImageTk.PhotoImage(Image.open(my_path + "\main\images\REGISTER_IN_US_NEW.png"))

    Label(mainframe, image = logo).place(relx = 0, rely = 0)
############################## 
    Label(mainframe, text = "")
    
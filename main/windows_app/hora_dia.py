from tkinter import *
import windows_app.RECARGA as reca
import windows_app.RECARGA as recar_train
import helpers.readfiles as readfiles
import windows_app.hora_dia as dia
from PIL import Image, ImageTk
from tkinter import Tk, Label, Button,Entry, Frame, END
    

#* Estructura de la ventana del Dashboard general.

def horaMAÑANA(root, mainFrame):
    root.title("Horarios de líneas de tren")
    mainFrame.destroy()
    mainFrame = Frame(root)
    mainFrame.config(width = "380", height = "676")
    mainFrame.pack()
    my_path = readfiles.Route()
    global logo
    logo = ImageTk.PhotoImage(Image.open(my_path + "\main\images\HORARIO1.png"))
    Label(mainFrame, image = logo).place(relx = 0, rely = 0)



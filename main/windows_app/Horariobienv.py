from tkinter import *
from tkinter import ttk
from tkinter import messagebox as MessageBox
import windows_app.LOG as log
import helpers.readfiles as readfiles
from PIL import Image, ImageTk
from tkinter import Tk, Label, Button,Entry, Frame, END

#* Estructura de la ventana del Dashboard general.
def horario(root, mainframe):
    root.title("Horarios de líneas de tren")

    mainframe.destroy()
    mainframe = Frame()
    mainframe.config(width = "380", height = "676")
    mainframe.pack()
    my_path = readfiles.Route()

    global logo, vaerDropBox
    
    logo = ImageTk.PhotoImage(Image.open(my_path + "\main\images\HORARIO.png"))
    
    Label(mainframe, image = logo).place(relx = 0, rely = 0)
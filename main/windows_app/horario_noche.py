from tkinter import *
from tkinter import ttk
import windows_app.RECARGA as reca
import windows_app.RECARGA as recar_train
import helpers.readfiles as readfiles
import windows_app.hora_dia as dia
import windows_app.horario_tarde as tarde
import windows_app.horario_noche as noche
from PIL import Image, ImageTk
from tkinter import Tk, Label, Button,Entry, Frame, END

def horario(root, mainFrame):
    root.title("Horarios de líneas de tren")

    mainFrame.destroy()
    mainFrame = Frame()
    mainFrame.config(width = "380", height = "676")
    mainFrame.pack()
    my_path = readfiles.Route()
    global logo, vaerDropBox
    logo = ImageTk.PhotoImage(Image.open(my_path + "\main\images\HORARIO3.png"))
    Label(mainFrame, image = logo).place(relx = 0, rely = 0)
    
    
#* Estructura de la ventana del Dashboard general.

def horaNOCHE(root, mainFrame):
    root.title("RESERVA")
    mainFrame.destroy()
    mainFrame = Frame(root)
    mainFrame.config(width = "380", height = "676")
    mainFrame.pack()
    my_path = readfiles.Route()
    global logo
    logo = ImageTk.PhotoImage(Image.open(my_path + "\main\images\HORARIO3.png"))
    Label(mainFrame, image = logo).place(relx = 0, rely = 0)
###############################

#RUTAS
def Selec_Rooty(root, mainFrame):
    a = vaerDropBox.get()
    
    if a == 'Dia':
        dia.horaMAÑANA(root, mainFrame)
    elif a == 'Tarde':
        tarde.horaTARDE(root, mainFrame)
    else:
        noche.horaNOCHE(root, mainFrame)
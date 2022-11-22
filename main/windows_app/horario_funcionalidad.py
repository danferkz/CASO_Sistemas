from tkinter import *
from tkinter import ttk
from tkinter import messagebox as MessageBox
import windows_app.LOG as log
import helpers.readfiles as readfiles
from PIL import Image, ImageTk
from tkinter import Tk, Label, Button,Entry, Frame, END
import tkinter as tk


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

    categoriesNUMEROSvar = ['Dia', 'Tarde', 'Noche']
    Label(mainframe, text = "Seleccion de fases del Dia", relief= "flat", bg="#767574", font=("Inter", 10)).place(x = 100, y = 300)
    vaerDropBox= ttk.Combobox(mainframe,font=("Inter", 16,"bold"),width = 10)
    vaerDropBox.set("variables")
    vaerDropBox["values"]  = categoriesNUMEROSvar
    vaerDropBox.place(x = 100, y = 350)
    
    
    Button(mainframe, text = "Continuar", width = 25,relief="flat",font=("Inter", 12,"bold"),bg="#000000",fg="#ffffff", command = lambda: Selec_Rooty()).place(x = 100, y = 400)
    


#RUTAS
def Selec_Rooty():
    a = vaerDropBox.get()
    my_path = readfiles.Route()
    
    if a == 'Dia':
        logo = ImageTk.PhotoImage(Image.open(my_path + "\main\images\HORARIO_(mañana).png"))
    elif a == 'Tarde':
        logo = ImageTk.PhotoImage(Image.open(my_path + "\main\images\HORARIO_(tarde).png"))
    else:
        logo = ImageTk.PhotoImage(Image.open(my_path + "\main\images\HORARIO_(noche).png"))
    





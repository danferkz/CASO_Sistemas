from tkinter import *
import windows_app.registro as reg
import windows_app.logs as lo
import windows_app.nueva as nue_a
import windows_app.nuevaventana2 as nuedos
import helpers.readfiles as readfiles
from PIL import Image, ImageTk
from tkinter import Tk, Label, Button,Entry, Frame, END

#* Estructura de la ventana de Inicio.
def inici(root, mainFrame):
    root.title("Inicio")
    mainFrame.config(width = "480", height = "1034")
    mainFrame.pack()
    my_path = readfiles.Route()
    global fondo
    fondo = ImageTk.PhotoImage(Image.open(my_path + "\main\images\INICIO_IN_US_NEW.png"))
    
    Label(mainFrame, image = fondo).place(relx = 0, rely = 0)
    
    
    Button(mainFrame, text = "REGISTRAR", width = 15, height = 3,bg="#000000", relief="flat",fg="#ffffff",font=("Inter", 15), command = lambda: nuedos.nuevo_ventana2(root, mainFrame)).place(relx = 0.36, y = 850)
    Button(mainFrame, text = "Nueva ventana", width = 15, height = 3,bg="#000000", relief="flat",fg="#ffffff",font=("Inter", 20,"bold"), command = lambda: nue_a.nuevo_ventana(root, mainFrame)).place(relx = 0.36, y = 450)
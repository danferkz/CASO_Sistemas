from tkinter import *
import windows_app.registro as reg
import helpers.readfiles as readfiles
from PIL import Image, ImageTk
from tkinter import Tk, Label, Button,Entry, Frame, END

#* Estructura de la ventana de Inicio.
def inici(root, mainFrame):
    root.title("Inicio")
    mainFrame.config(width = "380", height = "676")
    mainFrame.pack()
    my_path = readfiles.Route()
    global fondo
    fondo = ImageTk.PhotoImage(Image.open(my_path + "\main\images\INICIO_nue.png"))
    
    Label(mainFrame, image = fondo).place(relx = 0, rely = 0)
    
    
    Button(mainFrame, text = "REGISTRAR",width = 15, height = 3,bg="#000000", relief="flat",fg="#ffffff",font=("Inter", 15),command = lambda: reg.registro(root, mainFrame)).place(x = 50, y = 50)
    #Button(mainFrame, text = "Nueva ventana", width = 15, height = 3,bg="#000000", relief="flat",fg="#ffffff",font=("Inter", 20,"bold"),command = lambda: nue_a.nuevo_ventana(root, mainFrame)).place(relx = 0.36, y = 450)
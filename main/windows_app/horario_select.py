
from tkinter import *
from tkinter import ttk
from tkinter import messagebox as MessageBox
import windows_app.LOG as log
import windows_app.hora_dia as dia
import helpers.readfiles as readfiles
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

    logo = ImageTk.PhotoImage(Image.open(my_path + "\main\images\HORARIO1.png"))

    Label(mainFrame, image = logo).place(relx = 0, rely = 0)
############################## 
    categoriesNUMEROSvar = ['Dia', 'Tarde', 'Noche']
    Label(mainFrame, text = "Seleccion de fase de Dia", relief= "flat", bg="#767574", font=("Inter", 10)).place(x = 100, y = 300)
    vaerDropBox= ttk.Combobox(mainFrame,font=("Inter", 16,"bold"),width = 10)
    vaerDropBox.set("Dia")
    vaerDropBox["values"]  = categoriesNUMEROSvar
    vaerDropBox.place(x = 100, y = 350)
    
    
    Button(mainFrame, text = "FORMAR TABLAS", width = 25,relief="flat",font=("Inter", 12,"bold"),bg="#000000",fg="#ffffff", command = lambda: Selec_Rooty(root, mainFrame)).place(x = 100, y = 400)
    


#RUTAS
def Selec_Rooty(root, mainFrame):
    a = vaerDropBox.get()
    
    if a == 'Dia':
        dia.horaMAÑANA(root, mainFrame)
    elif a == 'Tarde':
        "dos_cua.pantalla4x4(root, mainFrame)"
    else:
        "dos_cua.pantalla4x4(root, mainFrame)"
    
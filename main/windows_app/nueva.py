from tkinter import *
from tkinter import ttk
import windows_app.logs as log
import windows_app.inic as inic
import helpers.readfiles as readfiles
from PIL import Image, ImageTk
from tkinter import Tk, Label, Button,Entry, Frame, END
    

#* Estructura de la ventana del Dashboard general.
def nuevo_ventana(root, mainFrame):
    root.title("Nuevo")

    mainFrame.destroy()
    mainFrame = Frame()
    mainFrame.config(width = "480", height = "1034")
    mainFrame.pack()
    my_path = readfiles.Route()
    
    global logo
    
    logo = ImageTk.PhotoImage(Image.open(my_path + "\main\images\REGISTER_IN_US_NEW.png"))
    
    Label(mainFrame, image = logo).place(relx = 0, rely = 0)
##############################
    Label(mainFrame, text = "Nuevo Registro",font=("Inter", 16)).place(x = 300, y = 425)    
    aA_Aa3_3 = StringVar()
    Entry(mainFrame, width = 25, borderwidth = 2, textvariable = aA_Aa3_3,font=("Inter", 30)).place(x = 150, y = 300)
    
################################
    
    #Button(mainFrame, text = "Ejecutar",command = lambda: resultado.Resol_(root, mainFrame)).place(x = 800, y = 684)
    Button(mainFrame, text = "Cancelar", width = 10,relief="flat",font=("Inter", 15,"bold"), command = lambda: inic.inici(root, mainFrame)).place(x = 300, y = 500)
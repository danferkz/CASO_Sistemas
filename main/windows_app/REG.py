from tkinter import *
import windows_app.inic as inic
import windows_app.INI_SE as se
import windows_app.HOME as ho
import helpers.readfiles as readfiles
from PIL import Image, ImageTk
from tkinter import Tk, Label, Button,Entry, Frame, END
    

#* Estructura de la ventana del Dashboard general.

def REC(root, mainFrame):
    root.title("REGISTRO")
    mainFrame.destroy()
    mainFrame = Frame(root)
    mainFrame.config(width = "380", height = "676")
    mainFrame.pack()
    my_path = readfiles.Route()
    global logo
    logo = ImageTk.PhotoImage(Image.open(my_path + "\main\images\REGISTER_final.png"))
    Label(mainFrame, image = logo).place(relx = 0, rely = 0)
###############################
    
    nom = StringVar()
    Entry(mainFrame, width = 14, borderwidth = 2, textvariable = nom, font=("Inter", 22), relief="flat").place(x = 60, y = 182)
    ape = StringVar()
    Entry(mainFrame, width = 14, borderwidth = 2, textvariable = ape, font=("Inter", 22), relief="flat").place(x = 60, y = 260)
    cor = StringVar()
    Entry(mainFrame, width = 14, borderwidth = 2, textvariable = cor, font=("Inter", 22), relief="flat").place(x = 95, y = 340)
    passw = StringVar()
    Entry(mainFrame, width = 14, borderwidth = 2, textvariable = passw, font=("Inter", 22), relief="flat").place(x = 95, y = 410)
    
################################
    
    #Button(mainFrame, text = "Ejecutar",command = lambda: resultado.Resol_(root, mainFrame)).place(x = 800, y = 684)
    Button(mainFrame, text = "Registrarse", width = 10, bg="#FFFEFD", relief="flat",font=("Inter", 15,"bold"), command = lambda: ho.HOM(root, mainFrame)).place(x = 100, y = 490)

"""
def recargas(root, mainFrame):
    root.title("Recargas")

    mainFrame.destroy()
    mainFrame = Frame()
    mainFrame.config(width = "480", height = "1034")
    mainFrame.pack()
    my_path = readfiles.Route()
    
    global logo
    
    logo = ImageTk.PhotoImage(Image.open(my_path + "\main\images\REGISTER_IN_US_NEW.png"))
    
    Label(mainFrame, image = logo).place(relx = 0, rely = 0)
##############################
    Label(mainFrame, text = "Registro",font=("Inter", 16)).place(x = 300, y = 425)    
    aA_Aa3_3 = StringVar()
    Entry(mainFrame, width = 25, borderwidth = 2, textvariable = aA_Aa3_3,font=("Inter", 30)).place(x = 150, y = 300)
    
################################
    
    #Button(mainFrame, text = "Ejecutar",command = lambda: resultado.Resol_(root, mainFrame)).place(x = 800, y = 684)
    Button(mainFrame, text = "Cancelar", width = 10,relief="flat",font=("Inter", 15,"bold"), command = lambda: inic.inici(root, mainFrame)).place(x = 300, y = 500)
    
"""
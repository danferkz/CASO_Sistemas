from tkinter import *
import windows_app.inic as inic
import helpers.readfiles as readfiles
from PIL import Image, ImageTk
from tkinter import Tk, Label, Button,Entry, Frame, END
    

#* Estructura de la ventana del Dashboard general.
def registro(root, mainFrame):
    root.title("Registro")

    mainFrame.destroy()
    mainFrame = Frame()
    mainFrame.config(width = "380", height = "676")
    mainFrame.pack()
    my_path = readfiles.Route()
    
    global logo
    
    logo = ImageTk.PhotoImage(Image.open(my_path + "\main\images\REGISTER_nue.png"))
    
    Label(mainFrame, image = logo).place(relx = 0, rely = 0)
##############################    
    nom = StringVar()
    Entry(mainFrame, width = 10, borderwidth = 2, textvariable = nom,font=("Inter", 25),relief="flat").place(x = 150, y = 100)
    ap = StringVar()
    Entry(mainFrame, width = 10, borderwidth = 2, textvariable = ap,font=("Inter", 25)).place(x = 150, y = 200)
    cor = StringVar()
    Entry(mainFrame, width = 10, borderwidth = 2, textvariable = cor,font=("Inter", 25)).place(x = 150, y = 250)
    con = StringVar()
    Entry(mainFrame, width = 10, borderwidth = 2, textvariable = con,font=("Inter", 25)).place(x = 150, y = 300)
    
    Button(mainFrame, text = "Register", width = 10,relief="flat",font=("Inter", 15,"bold"), command = lambda: inic.inici(root, mainFrame)).place(x = 100, y = 485)
################################
    
    #Button(mainFrame, text = "Ejecutar",command = lambda: resultado.Resol_(root, mainFrame)).place(x = 800, y = 684)
    Button(mainFrame, text = "Cancelar", width = 10,relief="flat",font=("Inter", 15,"bold"), command = lambda: inic.inici(root, mainFrame)).place(x = 200, y = 600)
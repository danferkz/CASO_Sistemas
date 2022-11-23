from tkinter import *
import windows_app.RECARGA as reca
import windows_app.RECARGA as recar_train
import helpers.readfiles as readfiles
from PIL import Image, ImageTk
from tkinter import Tk, Label, Button,Entry, Frame, END
    

#* Estructura de la ventana del Dashboard general.

def Enviar_NOti(root, mainFrame):
    root.title("NOTIFICACIONES")
    mainFrame.destroy()
    mainFrame = Frame(root)
    mainFrame.config(width = "380", height = "676")
    mainFrame.pack()
    my_path = readfiles.Route()
    global logo
    logo = ImageTk.PhotoImage(Image.open(my_path + "\main\images\lNOTIFICACIONES2.png"))
    Label(mainFrame, image = logo).place(relx = 0, rely = 0)
    notifi=StringVar
    Entry(mainFrame, width = 12, borderwidth = 8, textvariable = notifi,font=("Inter"),relief="flat").place(x = 100, y = 240)
    
################################
    
    #Button(mainFrame, text = "Ejecutar",command = lambda: resultado.Resol_(root, mainFrame)).place(x = 800, y = 684)
    Button(mainFrame, text = "ENVIAR", width = 10, bg="#FFFEFD", relief="flat",font=("Inter", 15,"bold"), command = lambda: notifi).place(x = 100, y = 490)

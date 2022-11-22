from tkinter import *
import windows_app.HOME as home
import helpers.readfiles as readfiles
from PIL import Image, ImageTk
from tkinter import Tk, Label, Button,Entry, Frame, END
    

#* Estructura de la ventana del Dashboard general.

def RESERVA(root, mainFrame):
    root.title("RESERVA")
    mainFrame.destroy()
    mainFrame = Frame(root)
    mainFrame.config(width = "380", height = "676")
    mainFrame.pack()
    my_path = readfiles.Route()
    global logo
    logo = ImageTk.PhotoImage(Image.open(my_path + "\main\images\is_RESERVA1.png"))
    Label(mainFrame, image = logo).place(relx = 0, rely = 0)
###############################

    
################################
    
    #Button(mainFrame, text = "Ejecutar",command = lambda: resultado.Resol_(root, mainFrame)).place(x = 800, y = 684)
    Button(mainFrame, text = "Regresar", width = 10, bg="#FFFEFD", relief="flat",font=("Inter", 15,"bold"), command = lambda: home.HOM(root, mainFrame)).place(x = 100, y = 490)

from tkinter import *
import windows_app.HOME as ho
import helpers.readfiles as readfiles
from PIL import Image, ImageTk
from tkinter import Tk, Label, Button,Entry, Frame, END
    

#* Estructura de la ventana del Dashboard general.

def LOG(root, mainFrame):
    root.title("LOG IN")
    mainFrame.destroy()
    mainFrame = Frame(root)
    mainFrame.config(width = "380", height = "676")
    mainFrame.pack()
    my_path = readfiles.Route()
    global logo
    logo = ImageTk.PhotoImage(Image.open(my_path + "\main\images\LOGIN_ULTIMO.png"))
    Label(mainFrame, image = logo).place(relx = 0, rely = 0)
    
    
    
    usu = StringVar()
    Entry(mainFrame, width = 14, borderwidth = 2, textvariable = usu, font=("Inter", 22), relief="flat").place(x = 95, y = 245)
    cont = StringVar()
    Entry(mainFrame, width = 14, borderwidth = 2, textvariable = cont, font=("Inter", 22), relief="flat").place(x = 95, y = 320)
    
################################
    
    Button(mainFrame, text = "Ingresar", width = 10, bg="#FFFEFD", relief="flat",font=("Inter", 15,"bold"), command = lambda: ho.HOM(root, mainFrame)).place(x = 100, y = 440)
    Button(mainFrame, text = "Olvidé mi contraseña", width = 18, bg="#FFFEFD", relief="flat",font=("Inter", 15,"bold"), command = lambda: ho.HOM(root, mainFrame)).place(x = 80, y = 560)

################################
    
    #Button(mainFrame, text = "Ejecutar",command = lambda: resultado.Resol_(root, mainFrame)).place(x = 800, y = 684)
    #Button(mainFrame, text = "INGRESAR", width = 10,relief="flat",font=("Inter", 15,"bold"), command = lambda: ho.HOM(root, mainFrame)).place(x = 300, y = 500)
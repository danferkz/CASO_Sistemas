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
    logo = ImageTk.PhotoImage(Image.open(my_path + "\main\images\LOGIN_final.png"))
    Label(mainFrame, image = logo).place(relx = 0, rely = 0)
    
    
    
    Entry()
    Label(mainFrame, text = "Registro",font=("Inter", 16)).place(x = 300, y = 425)    
    aA_Aa3_3 = StringVar()
    Entry(mainFrame, width = 25, borderwidth = 2, textvariable = aA_Aa3_3,font=("Inter", 30)).place(x = 150, y = 300)
    
################################
    
    #Button(mainFrame, text = "Ejecutar",command = lambda: resultado.Resol_(root, mainFrame)).place(x = 800, y = 684)
    Button(mainFrame, text = "INGRESAR", width = 10,relief="flat",font=("Inter", 15,"bold"), command = lambda: ho.HOM(root, mainFrame)).place(x = 300, y = 500)
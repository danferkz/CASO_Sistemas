from tkinter import *
import windows_app.BIENV as bienv
import windows_app.RECARGA as recar_train
import windows_app.METODO_PAGO as met_pago
import helpers.readfiles as readfiles
from PIL import Image, ImageTk
from tkinter import Tk, Label, Button,Entry, Frame, END
    

#* Estructura de la ventana del Dashboard general.

def MET_PAGO(root, mainFrame):
    root.title("SELECCIÓN DE MÉTODO DE PAGO")
    mainFrame.destroy()
    mainFrame = Frame(root)
    mainFrame.config(width = "380", height = "676")
    mainFrame.pack()
    my_path = readfiles.Route()
    global logo
    logo = ImageTk.PhotoImage(Image.open(my_path + "\main\images\METODO_PAGO.png"))
    Label(mainFrame, image = logo).place(relx = 0, rely = 0)
###############################
    
    visa = StringVar()
    Checkbutton(mainFrame, width = 1, textvariable = visa, bg="#FFFEFD",font=("Inter", 22), relief="flat").place(x = 30, y = 240)
    mastercard = StringVar()
    Checkbutton(mainFrame, width = 1, textvariable = mastercard, bg="#FFFEFD",font=("Inter", 22), relief="flat").place(x = 180, y = 240)
    dinners = StringVar()
    Checkbutton(mainFrame, width = 1, textvariable = dinners, bg="#FFFEFD",font=("Inter", 22), relief="flat").place(x = 30, y = 340)
    american = StringVar()
    Checkbutton(mainFrame, width = 1, textvariable = american, bg="#FFFEFD",font=("Inter", 22), relief="flat").place(x = 180, y = 340)
    
################################
    
    Button(mainFrame, text = "Siguiente", width = 10, bg="#FFFEFD", relief="flat",font=("Inter", 15,"bold"), command = lambda: met_pago.MET_PAGO(root, mainFrame)).place(x = 125, y = 540)

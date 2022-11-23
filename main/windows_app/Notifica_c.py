from tkinter import *
import windows_app.RECARGA as reca
import windows_app.ENVIONO as envia
import helpers.readfiles as readfiles
from PIL import Image, ImageTk
from tkinter import Tk, Label, Button,Entry, Frame, END
    

#* Estructura de la ventana del Dashboard general.

def VisNo_otifica(root, mainFrame):
    root.title("NOTIFICACIONES")
    mainFrame.destroy()
    mainFrame = Frame(root)
    mainFrame.config(width = "380", height = "676")
    mainFrame.pack()
    my_path = readfiles.Route()
    global logo
    logo = ImageTk.PhotoImage(Image.open(my_path + "\main\images\dnOTIFINES_uno.png"))
    Label(mainFrame, image = logo).place(relx = 0, rely = 0)


    

    Button(mainFrame, text = "ENVIAR Incidencia????", width = 10, bg = "#03989e", relief="flat",font=("Inter", 15,"bold"), command = lambda: envia.Enviar_NOti(root, mainFrame)).place(x = 100, y = 490)

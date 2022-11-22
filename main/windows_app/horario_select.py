from tkinter import *
from tkinter import ttk
from tkinter import messagebox as MessageBox
import windows_app.LOG as log
import windows_app.hora_dia as dia
import windows_app.horario_tarde as tarde
import windows_app.horario_noche as noche
import windows_app.hora_dia as dia
import helpers.readfiles as readfiles
from PIL import Image, ImageTk
from tkinter import Tk, Label, Button,Entry, Frame, END


def horarioBien(root, mainFrame):
    root.title("Horarios de líneas de tren")
    mainFrame.destroy()
    mainFrame = Frame()
    mainFrame.config(width = "380", height = "676")
    mainFrame.pack()
    my_path = readfiles.Route()

    global logo, vaerDropBox

    logo = ImageTk.PhotoImage(Image.open(my_path + "\main\images\HORARIO_BIENVENIDA.png"))

    Label(mainFrame, image = logo).place(relx = 0, rely = 0)
    
############################## 
    

    Button(mainFrame, text = "Continuar", width = 25,relief="flat",font=("Inter", 12,"bold"),bg="#000000",fg="#ffffff", command = lambda: dia.horaMAÑANA(root, mainFrame)).place(x = 100, y = 400)
    
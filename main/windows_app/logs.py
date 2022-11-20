from tkinter import *
from tkinter import ttk
import windows_app.registro as inic
import helpers.readfiles as readfiles
from PIL import Image, ImageTk
from tkinter import Tk, Label, Button,Entry, Frame, END

def log_In(root, mainFrame):
    root.title("LOG IN")

    mainFrame.destroy()
    mainFrame = Frame()
    mainFrame.config(width = "480", height = "1034")
    mainFrame.pack()
    my_path = readfiles.Route()
    
    global logo
    
    logo = ImageTk.PhotoImage(Image.open(my_path + "\main\images\LOG_IN_US_NEW.png"))
    
    Label(mainFrame, image = logo).place(relx = 0, rely = 0)
##############################
    Label(mainFrame, text = "MAX",font=("Inter", 16)).place(x = 300, y = 200)    
    aA_Aa3_3 = IntVar()
    Entry(mainFrame, width = 8, borderwidth = 2, textvariable = aA_Aa3_3,font=("Inter", 16),relief="flat").place(x = 400, y = 200)
    Label(mainFrame, text = "X1",font=("Inter", 16)).place(x = 300, y = 225)
    
################################
    
    #Button(mainFrame, text = "Ejecutar",command = lambda: me.m(root, mainFrame)).place(x = 300, y = 400)
    Button(mainFrame, text = "Cancelar", width = 10,relief="flat",font=("Inter", 15,"bold"), command = lambda: inic.registro(root, mainFrame)).place(x = 300, y = 500)
from tkinter import *
import helpers.readfiles as readfiles
import windows_app.horario_select as hora
import windows_app.bien_rec as rebien
import windows_app.Notifica_c as noti
import windows_app.REserva as reser
from PIL import Image, ImageTk
from tkinter import Tk, Label, Button,Entry, Frame, END
    

#* Estructura de la ventana del Dashboard general.
def HOM(root, mainFrame):
    root.title("HOME")

    mainFrame.destroy()
    mainFrame = Frame()
    mainFrame.config(width = "380", height = "676")
    mainFrame.pack()
    my_path = readfiles.Route()
    
    global logo
    
    logo = ImageTk.PhotoImage(Image.open(my_path + "\main\images\HOME_F.png")) 
    
    Label(mainFrame, image = logo).place(relx = 0, rely = 0)
##############################    
    Button(mainFrame, text = "HORARIO", width = 20,relief="flat",font=("Inter", 15,"bold"), command = lambda: hora.horario(root, mainFrame)).place(x = 125, y = 200)
    Button(mainFrame, text = "RECARGA", width = 20,relief="flat",font=("Inter", 15,"bold"), command = lambda: rebien.BIEN_REc(root, mainFrame)).place(x = 125, y = 250)
    Button(mainFrame, text = "NOTIFICACIONES", width = 20,relief="flat",font=("Inter", 15,"bold"), command = lambda: noti.VisNo_otifica(root, mainFrame)).place(x = 125, y = 300)
    Button(mainFrame, text = "RESERVA", width = 20,relief="flat",font=("Inter", 15,"bold"), command = lambda: reser.RESERVA(root, mainFrame)).place(x = 125, y = 350)
################################
    
    #Button(mainFrame, text = "Ejecutar",command = lambda: resultado.Resol_(root, mainFrame)).place(x = 800, y = 684)
    #Button(mainFrame, text = "Cancelar", width = 10,relief="flat",font=("Inter", 15,"bold"), command = lambda: inic.inici(root, mainFrame)).place(x = 200, y = 600)
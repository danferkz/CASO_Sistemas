from tkinter import *
import windows_app.inic as ini
import helpers.readfiles as readfiles

#* Estructura general
root = Tk()
root.resizable(0,0)
mainFrame = Frame(root)
ini.Login(root, mainFrame)
my_path = readfiles.Route()
root.iconbitmap(my_path + "\main\images\APP.ico")

#* Función para cerrar y destruir la ventana al cerrar la aplicación externamente.
def quit_me():
    root.quit()
<<<<<<< HEAD
    root.destroy()
    
    
    
    
=======
    root.destroy() 
>>>>>>> b76de1c5fef8965baf11e00cb6dd3e71faa6b719

root.protocol("WM_DELETE_WINDOW", quit_me)
root.mainloop()
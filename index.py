#Desde aquí se llama a la función que realiza el login y al mismo timepo une todas los archivos
import msvcrt
from login import inicio
import shutil
from cgitb import text
import tkinter as tk
from tkinter import *



#shutil.copy('txt.txt', 'base_de_datos.py')
#msvcrt.getch()


ventana_login = tk.Tk()


ventana_login.title('Proyecto Taller')
ventana_login.minsize(80,60)

def cerrar_ventana_login():
    ventana_login.destroy()


btn_login = tk.Button(ventana_login,text = 'Iniciar sesion', command=print())
btn_login.place(x=60,y=30)

btn_login.pack

#btn_reg = tk.Button(ventana_login,text = 'Registrarse', command=login.registrar())
#btn_reg.place(x=10,y=40)

btn_salir = tk.Button(ventana_login,text = 'Salir', command=cerrar_ventana_login)
btn_salir.place(x=80,y=100)


''' lb_usuario = tk.Label(ventana_login,text='Ingrese su nombre de usuario: ')
lb_usuario.place(x=10, y=10)

sv_usuario = tk.StringVar()
e_usuario = ttk.Entry(ventana_login,textvariable = sv_usuario, width = 40)
e_usuario.place(x=180,y=10) '''


tk.mainloop()
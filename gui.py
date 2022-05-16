from cgitb import text
import tkinter as tk
from tkinter import *
from turtle import width
from typing import Text
from email.mime import base




ventana = tk.Tk()
ventana.title('Proyecto Taller')
ventana.minsize(800,600)

def cerrar_ventana():
    ventana.destroy()


btn_login = tk.Button(ventana,text = 'Iniciar sesion', command=login.login())
btn_login.place(x=10,y=10)

btn_login.pack

#btn_reg = tk.Button(ventana,text = 'Registrarse', command=login.registrar())
#btn_reg.place(x=10,y=40)

btn_salir = tk.Button(ventana,text = 'Salir', command=cerrar_ventana)
btn_salir.place(x=10,y=70)


''' lb_usuario = tk.Label(ventana,text='Ingrese su nombre de usuario: ')
lb_usuario.place(x=10, y=10)

sv_usuario = tk.StringVar()
e_usuario = ttk.Entry(ventana,textvariable = sv_usuario, width = 40)
e_usuario.place(x=180,y=10) '''










tk.mainloop()
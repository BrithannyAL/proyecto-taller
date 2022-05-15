from cgitb import text
import tkinter as tk
from tkinter import ttk
from turtle import width
from typing import Text


ventana = tk.Tk()
ventana.title('Proyecto Taller')
ventana.minsize(800,600)

def cerrar_ventana():
    ventana.destroy()

def detalles():
    print(sv_usuario.get())
    print(sv_pass.get())


lb_usuario = tk.Label(ventana,text='Ingrese su nombre de usuario: ')
lb_usuario.place(x=10, y=10)

sv_usuario = tk.StringVar()
e_usuario = ttk.Entry(ventana,textvariable = sv_usuario, width = 40)
e_usuario.place(x=180,y=10)

lb_pass = tk.Label(ventana,text='Ingrese su contraseña: ')
lb_pass.place(x=10, y=40)

sv_pass = tk.StringVar()
e_pass = ttk.Entry(ventana,textvariable = sv_pass, width = 40)
e_pass.place(x=180,y=40)

btn_salir = tk.Button(ventana,text = 'Salir', command=cerrar_ventana)
btn_detalles = tk.Button(ventana, text = 'Imprimir', command=detalles)

btn_salir.place(x=10,y=70)
btn_detalles.place(x=10,y=110)


tk.mainloop()
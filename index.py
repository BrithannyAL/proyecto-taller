#Desde aquí se llama a la función que realiza el login y al mismo timepo une todas los archivos
import msvcrt
import shutil
from cgitb import text
import tkinter as tk
from tkinter import ttk
from tkinter import *
import login

#shutil.copy('txt.txt', 'base_de_datos.py')
#msvcrt.getch()

ventana_login = tk.Tk()


ventana_login.title('Proyecto Taller')
ventana_login.minsize(800,600)

def cerrar_ventana_login():
    ventana_login.destroy()

def hide(x):
    for i in x:
        i.pack_forget()

lb_usuario = tk.Label(ventana_login,text='Ingrese su nombre de usuario: ')
lb_usuario.place(x=10, y=10)

sv_usuario = tk.StringVar()
e_usuario = ttk.Entry(ventana_login,textvariable = sv_usuario, width = 40)
e_usuario.place(x=180,y=10) 

lb_usuario.pack()
e_usuario.pack()
lb_usuario.pack_forget()
e_usuario.pack_forget()

lb_contra = tk.Label(ventana_login,text='Ingrese su contrasena: ')
lb_contra.place(x=10, y=10)

sv_contrasena = tk.StringVar()
e_contra = ttk.Entry(ventana_login,textvariable = sv_contrasena, width = 40)
e_contra.place(x=180,y=10) 

lb_contra.pack()
e_contra.pack()
lb_contra.pack_forget()
e_contra.pack_forget()

btn_ingresar = tk.Button(ventana_login,text = 'Ingresar')
lb_contra.pack_forget()
btn_ingresar.configure(command= lambda: login.login(e_usuario.get(), e_contra.get()))


btn_login = tk.Button(ventana_login,text = 'Iniciar sesion')
btn_login.place(x=60,y=100)

btn_reg = tk.Button(ventana_login,text = 'Registrarse')
btn_reg.place(x=10,y=40)

btn_salir = tk.Button(ventana_login,text = 'Salir')
btn_salir.place(x=80,y=100)


btn_login.configure(command=lambda: [hide([btn_salir,btn_login,btn_reg]),lb_usuario.pack(), e_usuario.pack(),lb_contra.pack(),e_contra.pack(), btn_ingresar.pack()])
btn_salir.configure(command= cerrar_ventana_login)

btn_login.pack()
btn_salir.pack()
btn_reg.pack()



tk.mainloop()
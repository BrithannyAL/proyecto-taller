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

def clear_text(x):
   for i in x:
        i.delete(0, END)




btn_agregar_curso = tk.Button(ventana_login,text = 'Agregar curso')
btn_agregar_curso.configure(command= lambda: login.login(e_usuario.get(), e_contra.get()))
btn_agregar_curso.pack_forget

btn_modificar_curso = tk.Button(ventana_login,text = 'Modificar curso')
btn_modificar_curso.configure(command= lambda: login.login(e_usuario.get(), e_contra.get()))
btn_modificar_curso.pack_forget

btn_agregar_carrera = tk.Button(ventana_login,text = 'Agregar carrera')
btn_agregar_carrera.configure(command= lambda: login.login(e_usuario.get(), e_contra.get()))
btn_agregar_carrera.pack_forget

btn_modificar_carrera = tk.Button(ventana_login,text = 'Modificar carrera')
btn_modificar_carrera.configure(command= lambda: login.login(e_usuario.get(), e_contra.get()))
btn_modificar_carrera.pack_forget

btn_matricular_carrera = tk.Button(ventana_login,text = 'Matricular carrera')
btn_matricular_carrera.configure(command= lambda: login.login(e_usuario.get(), e_contra.get()))
btn_matricular_carrera.pack_forget

btn_matricular_curso = tk.Button(ventana_login,text = 'Matricular curso')
btn_matricular_curso.configure(command= lambda: login.login(e_usuario.get(), e_contra.get()))
btn_matricular_curso.pack_forget

btn_generar_reporte = tk.Button(ventana_login,text = 'Generar reporte')
btn_generar_reporte.configure(command= lambda: login.login(e_usuario.get(), e_contra.get()))
btn_generar_reporte.pack_forget

btn_registrar_actividad = tk.Button(ventana_login,text = 'Registrar actividad')
btn_registrar_actividad.configure(command= lambda: login.login(e_usuario.get(), e_contra.get()))
btn_registrar_actividad.pack_forget

btn_determinar_estado = tk.Button(ventana_login,text = 'Determinar estado del curso')
btn_determinar_estado.configure(command= lambda: login.login(e_usuario.get(), e_contra.get()))
btn_determinar_estado.pack_forget

btn_ver_horario = tk.Button(ventana_login,text = 'Ver horario')
btn_ver_horario.configure(command= lambda: login.login(e_usuario.get(), e_contra.get()))
btn_ver_horario.pack_forget


btn_log_out = tk.Button(ventana_login,text = 'Salir del usuario')
btn_log_out.configure(command= lambda: [btn_login.pack(),btn_reg.pack(),btn_salir.pack(), hide([btn_agregar_curso,btn_modificar_curso,btn_agregar_carrera,btn_modificar_carrera,btn_log_out,btn_matricular_carrera,btn_matricular_curso,btn_registrar_actividad,btn_generar_reporte,btn_determinar_estado,btn_ver_horario])])
btn_log_out.pack_forget     

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

def ingresar(bool):
    if bool == 1:
        btn_agregar_curso.pack()
        btn_modificar_curso.pack()
        btn_agregar_carrera.pack()
        btn_modificar_carrera.pack()
        btn_log_out.pack()
        clear_text([e_usuario,e_contra])
        hide([lb_usuario,e_usuario,lb_contra,e_contra,btn_ingresar])
    elif bool == 2:
        btn_matricular_carrera.pack()
        btn_matricular_curso.pack()
        btn_generar_reporte.pack()
        btn_registrar_actividad.pack()
        btn_determinar_estado.pack()
        btn_ver_horario.pack()
        btn_log_out.pack()
        clear_text([e_usuario,e_contra])
        hide([lb_usuario,e_usuario,lb_contra,e_contra, btn_ingresar])


btn_ingresar = tk.Button(ventana_login,text = 'Ingresar')
btn_ingresar.configure(command= lambda:  [ingresar(login.login(e_usuario.get(), e_contra.get())) ])


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
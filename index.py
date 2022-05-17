#Desde aquí se llama a la función que realiza el login y al mismo timepo une todas los archivos
from email.mime import base
import msvcrt
import shutil
from cgitb import text
import tkinter as tk
from tkinter import ttk
from tkinter import *
import login
import funciones_estudiante
import base_de_datos

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

def show(x):
    for i in x:
        i.pack()

def clear_text(x):
   for i in x:
        i.delete(0, END)


#Menu matricular carrera

sv_nombre_persona = tk .StringVar()
cb_carrera = ttk.Combobox(ventana_login, textvariable=sv_nombre_persona)
cb_carrera['values'] =  base_de_datos.carreras.nombre_carrera(base_de_datos.lista_carreras)
cb_carrera['state'] = 'readonly'
cb_carrera.pack_forget()

btn_ingresar_carrera = tk.Button(ventana_login,text='Matricular')
btn_ingresar_carrera.configure(command= lambda: funciones_estudiante.matricular_carrera(cb_carrera.get(),base_de_datos.carreras.recorrer_lista(base_de_datos.lista_carreras)))
btn_ingresar_carrera.pack_forget()

#Menu admin
btn_agregar_curso = tk.Button(ventana_login,text = 'Agregar curso')
btn_agregar_curso.configure(command= lambda: print)
btn_agregar_curso.pack_forget

btn_modificar_curso = tk.Button(ventana_login,text = 'Modificar curso')
btn_modificar_curso.configure(command= lambda: print)
btn_modificar_curso.pack_forget

btn_agregar_carrera = tk.Button(ventana_login,text = 'Agregar carrera')
btn_agregar_carrera.configure(command= lambda: print)
btn_agregar_carrera.pack_forget

btn_modificar_carrera = tk.Button(ventana_login,text = 'Modificar carrera')
btn_modificar_carrera.configure(command= lambda:print)
btn_modificar_carrera.pack_forget

#Menu estudiante
btn_matricular_carrera = tk.Button(ventana_login,text = 'Matricular carrera')
btn_matricular_carrera.configure(command= lambda:(show([cb_carrera,btn_ingresar_carrera]), hide([btn_matricular_carrera, btn_matricular_curso,btn_generar_reporte,btn_registrar_actividad,btn_determinar_estado,btn_ver_horario])))
btn_matricular_carrera.pack_forget

btn_matricular_curso = tk.Button(ventana_login,text = 'Matricular curso')
btn_matricular_curso.configure(command= lambda:  print)
btn_matricular_curso.pack_forget

btn_generar_reporte = tk.Button(ventana_login,text = 'Generar reporte')
btn_generar_reporte.configure(command= lambda:print)
btn_generar_reporte.pack_forget

btn_registrar_actividad = tk.Button(ventana_login,text = 'Registrar actividad')
btn_registrar_actividad.configure(command= lambda: print)
btn_registrar_actividad.pack_forget

btn_determinar_estado = tk.Button(ventana_login,text = 'Determinar estado del curso')
btn_determinar_estado.configure(command= lambda: print)
btn_determinar_estado.pack_forget

btn_ver_horario = tk.Button(ventana_login,text = 'Ver horario')
btn_ver_horario.configure(command= lambda:print)
btn_ver_horario.pack_forget

#Boton para salir
btn_log_out = tk.Button(ventana_login,text = 'Salir del usuario')
btn_log_out.configure(command= lambda: [show([btn_login,btn_reg,btn_salir]), hide([btn_agregar_curso,btn_modificar_curso,btn_agregar_carrera,btn_modificar_carrera,btn_log_out,btn_matricular_carrera,btn_matricular_curso,btn_registrar_actividad,btn_generar_reporte,btn_determinar_estado,btn_ver_horario, cb_carrera, btn_ingresar_carrera])])
btn_log_out.pack_forget     

#Login

def ingresar(bl, e_usuario, e_contra):
    print(bl)
    if type(bl) == list:
        if bl[0] == 1:
            show([btn_agregar_curso, btn_modificar_curso, btn_agregar_carrera, btn_modificar_carrera, btn_log_out])
            hide([])
        elif bl[0] == 2:
            show([btn_matricular_carrera, btn_matricular_curso, btn_generar_reporte, btn_registrar_actividad, btn_determinar_estado, btn_ver_horario, btn_log_out])
    return(generar_ventana_login())        

def generar_ventana_login():
    sv_usuario = tk.StringVar()
    sv_contrasena = tk.StringVar()
        
    lb_usuario = tk.Label(ventana_login,text='Ingrese su nombre de usuario: ')
    e_usuario = ttk.Entry(ventana_login,textvariable = sv_usuario, width = 40)

    lb_contra = tk.Label(ventana_login,text='Ingrese su contraseña: ')
    e_contra = ttk.Entry(ventana_login,textvariable = sv_contrasena, width = 40)
    
    btn_ingresar = tk.Button(ventana_login,text = 'Ingresar')
    btn_ingresar.configure(command= lambda:
        [ingresar(login.login(sv_usuario.get(),sv_contrasena.get()), e_usuario, e_contra),
         hide([lb_usuario, e_usuario, lb_contra, e_contra, btn_ingresar])])
    
    return(
        show([lb_usuario, e_usuario, lb_contra, e_contra, btn_ingresar])
    )
    
def generar_ventana_registrar():
    sv_new_name = StringVar()
    sv_new_num = StringVar()
    sv_new_user = StringVar()
    sv_new_pass = StringVar()
    
    lb_new_name = tk.Label(ventana_login, text="Ingrese su nombre")
    e_new_name = ttk.Entry(ventana_login, textvariable = sv_new_name, width = 40)
    
    lb_new_num = tk.Label(ventana_login, text="Ingrese su número de teléfono")
    e_new_num = ttk.Entry(ventana_login, textvariable = sv_new_num, width = 40)
    
    lb_new_user = tk.Label(ventana_login, text="Ingrese su usuario")
    e_new_user = ttk.Entry(ventana_login,textvariable = sv_new_user, width = 40)
    
    lb_new_pass = tk.Label(ventana_login, text="Ingrese su contraseña")
    e_new_pass = ttk.Entry(ventana_login, textvariable = sv_new_pass, width = 40)
    
    btn_registrar_admin = tk.Button(ventana_login, text = "Registrarse como Administrador")
    btn_registrar_admin.configure(command=lambda:
        [login.registrar(0, sv_new_name.get(), sv_new_num.get(), sv_new_user.get(), sv_new_pass.get())])
    btn_registrar_estud = tk.Button(ventana_login, text = "Registrarse como Estudiante")
    btn_registrar_estud.configure(command=lambda:
        [login.registrar(1, sv_new_name.get(), sv_new_num.get(), sv_new_user.get(), sv_new_pass.get())])
    
    return(show([lb_new_name, e_new_name, lb_new_num, e_new_num ,lb_new_user, e_new_user, lb_new_pass, e_new_pass, btn_registrar_admin, btn_registrar_estud]))

btn_login = tk.Button(ventana_login,text = 'Iniciar sesion')
btn_login.place(x=60,y=100)

btn_reg = tk.Button(ventana_login,text = 'Registrarse')
btn_reg.place(x=10,y=40)

btn_salir = tk.Button(ventana_login,text = 'Salir')
btn_salir.place(x=80,y=100)

#CONFIGURACIÓN DE LOS BOTONES DE LA PANTALLA DE INICIO
btn_login.configure(command=lambda:
    [hide([btn_salir,btn_login,btn_reg]), generar_ventana_login()])

btn_reg.configure(command=lambda:
    [hide([btn_salir,btn_login,btn_reg]), generar_ventana_registrar()])

btn_salir.configure(command = cerrar_ventana_login)

btn_login.pack()
btn_reg.pack()
btn_salir.pack()


tk.mainloop()
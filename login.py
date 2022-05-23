# Se importan los dstos de los usuarios y las funciones para sus respectivas interfaces
from ast import Return
from email.mime import base
from operator import truediv
from tkinter import E, messagebox
from base_de_datos import dic_horario
from base_de_datos import estudiante, admin
from cargar_en_archivos import cargar_archivos_admins, cargar_archivos_estudiantes
from funciones_admin import agregar_curso, modificar_curso, agregar_carrera, modificar_carrera
from funciones_estudiante import  matricular_carrera, matricular_curso, ver_horario
import hashlib


def login(u,c):
    """
    Esta función es la que permite un usuario inicie cesión con una cuenta existente. El sistema de le pide al usuario que ingrese su usuario y contraseña para iniciar. Él mismo, determinará si la cuenta es de tipo estudiante, adminitrador o si no existe. En caso de que la cuenta no se encuentre en la base de datos, el sistema pedirá la cuenta nuevamente. Para esto se usa un ciclo que trabaja con el estado de una variable tipo boolean y al cambiar dicho estado, le ciclo se cierra."""
    try:
        estudiantes = cargar_archivos_estudiantes()
        admins = cargar_archivos_admins()
        registro_actual = None
        tipo = None
        
        pun_admin = admins  
        while registro_actual == None:
            if pun_admin.usuario == u and pun_admin.contrasena == hashlib.md5(c.encode('ascii')).hexdigest():
                registro_actual = pun_admin
                tipo = 1
            else:
                if pun_admin.sig != None:
                    pun_admin = pun_admin.sig
                else:
                    registro_actual = True 
        pun_estudiantes = estudiantes
        
        while registro_actual == True:
            if pun_estudiantes.usuario == u and pun_estudiantes.contrasena == hashlib.md5(c.encode('ascii')).hexdigest():
                registro_actual = pun_estudiantes
                tipo = 2
            else:
                if pun_estudiantes.sig != None:
                    pun_estudiantes = pun_estudiantes.sig
                else:
                    registro_actual = False
                            
        if registro_actual == False or registro_actual == True:
            messagebox.showerror(title="Error", message="El usuario no fue encontrado, intente de nuevo")
        else:
            return [tipo,registro_actual]

    except:
        messagebox.showerror(title="Error", message="Ha habido un error en el sistema")
        print("Ha habido un error en el sistema")


def registrar(op, vname, vnum, vuser, vpass):
    """
        Esta es la segunda opción del menú principal. La función permite registrar un nuevo usuario de tipo estudiante o admin. Primero, el sistema le pide los datos necesarios al usuario que está creando la cuenta, este mismo verifica si el usuario ingresado ya está regstrado en el sistema. Una vez que el sisteema haya recolectado los datos para la creación de la cuenta, verifica el tipo indicado por el usuario para darle la forma adecuada dentro de la base de datos.
        Esta función no recibe parámetros."""   
    try:
        if op == 0:
            admins = cargar_archivos_admins()
            new = admin(vname , 'admin' , vnum, vuser, hashlib.md5(vpass.encode('ascii')).hexdigest())
            if admins == None:
                admins = new
            else:
                admins.insertar(new)
            admins.guardar_en_archivos()
            messagebox.showinfo(message="El administrador se ha registrado con éxito")
        elif op == 1:
            global dic_horario
            estudiantes = cargar_archivos_estudiantes()
            new = estudiante(
                vname, 'estudiante', [], [], [], [],
                vuser, hashlib.md5(vpass.encode('ascii')).hexdigest(), dic_horario)
            if estudiantes == None:
                estudiantes = new
            else:
                estudiantes.insertar(new)
            estudiantes.guardar_en_archivos()
            messagebox.showinfo(message="El estudiante se ha registrado con éxito")
    except:
        messagebox.showerror(title="Error", message="Ha habido un error en el sistema")
        print("Ha habido un error en el sistema")

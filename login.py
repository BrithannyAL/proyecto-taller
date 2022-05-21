# Se importan los dstos de los usuarios y las funciones para sus respectivas interfaces
from ast import Return
from email.mime import base
from operator import truediv
from tkinter import E, messagebox
from base_de_datos import dic_horario, dic_reporte
from base_de_datos import estudiante, admin
from cargar_en_archivos import cargar_archivos_admins, cargar_archivos_estudiantes
from funciones_admin import agregar_curso, modificar_curso, agregar_carrera, modificar_carrera
from funciones_estudiante import generar_reporte, matricular_carrera, matricular_curso, generar_reporte, registro_actividades, aprobado_noAprobado, ver_horario
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
                    registro_actual = False
             
        pun_estudiantes = estudiantes
        while registro_actual == None:
            if pun_estudiantes.usuario == u and pun_estudiantes.contrasena == hashlib.md5(c.encode('ascii')).hexdigest():
                registro_actual = pun_estudiantes
                tipo = 2
            else:
                if pun_estudiantes.sig != None:
                    pun_estudiantes = pun_estudiantes.sig
                else:
                    registro_actual = False
                            
        if registro_actual != False:
            return (tipo)
        elif registro_actual == False:
            messagebox.showinfo(title="Error", message="El usuario no fue encontrado, intente de nuevo")
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
            global dic_reporte
            estudiantes = cargar_archivos_estudiantes()
            new = estudiante(
                vname, 'estudiante', [], [], [], [],
                vuser, hashlib.md5(vpass.encode('ascii')).hexdigest(), dic_reporte, dic_horario)
            if estudiantes == None:
                estudiantes = new
            else:
                estudiantes.insertar(new)
            estudiantes.guardar_en_archivos()
            messagebox.showinfo(message="El estudiante se ha registrado con éxito")
    except:
        messagebox.showerror(title="Error", message="Ha habido un error en el sistema")
        print("Ha habido un error en el sistema")

def funciones_admin(opcion):
    """
        Esta función es la que llama a las funciones de los administradores, según la opción que ellos hayan escogido en el menú. Para esto se usan los condicionales, los cuales comparan la respuesta del usuario con las opciones del menú para saber cuál es la función que se desea invocar.
        
        Parámetros:
        - opcion (inr): esta es la respuesta del usuario que es comparada con las opciones del menú. Para mayor facilidad se hizo con números."""
    global carreras
    global cursos
    if opcion == 1:
        cursos = agregar_curso(list(cursos))
    elif opcion == 2:
        cursos = modificar_curso(list(cursos))
    elif opcion == 3:
        carreras = agregar_carrera(list(carreras), cursos)
    elif opcion == 4:
        carreras = modificar_carrera(list(carreras), cursos)
    elif opcion == 5:
        opci = input("¿Desea cerrar la aplicación? (y/n)")
        if opci == "y":
            quit()

def funciones_estudiante(opcion, usuario):
    """
        Esta función es la que llama a las funciones de los estudiantes, según la opción que ellos hayan escogido en el menú. Para esto se usan los condicionales, los cuales comparan la respuesta del usuario con las opciones del menú para saber cuál es la función que se desea invocar.
        
        Parámetros:
        - opcion (int): esta es la respuesta del usuario que es comparada con las opciones del menú. Para mayor facilidad se hizo con números."""
    global carreras
    global cursos
    global estudiantes
    if opcion == 1:
        estudiantes = matricular_carrera(
            usuario, carreras, cursos, estudiantes)
    elif opcion == 2:
        estudiantes = matricular_curso(usuario, carreras, cursos, estudiantes)
    elif opcion == 3:
        estudiantes = generar_reporte(usuario, carreras, cursos, estudiantes)
    elif opcion == 4:
        estudiantes = registro_actividades(
            usuario, carreras, cursos, estudiantes)
    elif opcion == 5:
        aprobado_noAprobado(usuario, estudiantes, cursos)
    elif opcion == 6:
        ver_horario(usuario, estudiantes)
    elif opcion == 7:
        opci = input("¿Desea cerrar la aplicación? (y/n)")
        if opci == "y":
            quit()

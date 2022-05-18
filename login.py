# Se importan los dstos de los usuarios y las funciones para sus respectivas interfaces
from ast import Return
from email.mime import base
from operator import truediv
from tkinter import E, messagebox
from base_de_datos import dic_horario, dic_reporte, estudiantes, admins
from base_de_datos import estudiante, admin
from funciones_admin import agregar_curso, modificar_curso, agregar_carrera, modificar_carrera
from funciones_estudiante import generar_reporte, matricular_carrera, matricular_curso, generar_reporte, registro_actividades, aprobado_noAprobado, ver_horario
import hashlib


def login(u,c):
    """
    Esta función es la que permite un usuario inicie cesión con una cuenta existente. El sistema de le pide al usuario que ingrese su usuario y contraseña para iniciar. Él mismo, determinará si la cuenta es de tipo estudiante, adminitrador o si no existe. En caso de que la cuenta no se encuentre en la base de datos, el sistema pedirá la cuenta nuevamente. Para esto se usa un ciclo que trabaja con el estado de una variable tipo boolean y al cambiar dicho estado, le ciclo se cierra."""
    try:
        a = estudiantes.buscar(u)
        l = admins.buscar(u)
        if l == False and a == False:
            messagebox.showinfo(message="El usuario no fue encontrado, intente de nuevo")
            print('El usuario no fue encontrado, intente de nuevo')
            return False
        elif l != False:
            if l[2] == u and l[3] == hashlib.md5(c.encode('ascii')).hexdigest():
                return [1,l[2]]
        elif a != False:
            if a[6] == u and a[7] == hashlib.md5(c.encode('ascii')).hexdigest():
                return [2,a[6]]
        else:
            messagebox.showinfo(message="El usuario o la contrasena son incorrectos")
            print('El usuario o la contrasena son incorrectos')
            return False
    except:
        messagebox.showerror("Ha habido un error en el sistema")
        print("Ha habido un error en el sistema")


def registrar(op, vname, vnum, vuser, vpass):
    """
        Esta es la segunda opción del menú principal. La función permite registrar un nuevo usuario de tipo estudiante o admin. Primero, el sistema le pide los datos necesarios al usuario que está creando la cuenta, este mismo verifica si el usuario ingresado ya está regstrado en el sistema. Una vez que el sisteema haya recolectado los datos para la creación de la cuenta, verifica el tipo indicado por el usuario para darle la forma adecuada dentro de la base de datos.
        Esta función no recibe parámetros."""   
    try:
        global estudiantes, admins
        if op == 0:
            admins.insertar(admins,admin(vname , 'admin' , vnum, vuser, hashlib.md5(vpass.encode('ascii')).hexdigest()))
            messagebox.showinfo(message="El administrador se ha registrado con éxito")
            print(admins.recorrer_lista())
        elif op == 1:
            estudiantes.insertar(estudiantes, estudiante (
                vname, 'estudiante' , [],  [],  [],  [], 
                vuser,  hashlib.md5(vpass.encode('ascii')).hexdigest(),
                dic_horario, dic_reporte))
            messagebox.showinfo(message="El estudiante se ha registrado con éxito")
            print(estudiantes.recorrer_lista())
    except:
        messagebox.showerror("Ha habido un error en el sistema")
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

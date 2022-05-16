# Se importan los dstos de los usuarios y las funciones para sus respectivas interfaces
from email.mime import base
from operator import truediv
from tkinter import E
import base_de_datos 
from funciones_admin import agregar_curso, modificar_curso, agregar_carrera, modificar_carrera
from funciones_estudiante import generar_reporte, matricular_carrera, matricular_curso, generar_reporte, registro_actividades, aprobado_noAprobado, ver_horario
import hashlib


def login(u,c):
    """
    Esta función es la que permite un usuario inicie cesión con una cuenta existente. El sistema de le pide al usuario que ingrese su usuario y contraseña para iniciar. Él mismo, determinará si la cuenta es de tipo estudiante, adminitrador o si no existe. En caso de que la cuenta no se encuentre en la base de datos, el sistema pedirá la cuenta nuevamente. Para esto se usa un ciclo que trabaja con el estado de una variable tipo boolean y al cambiar dicho estado, le ciclo se cierra."""
    a = base_de_datos.estudiantes.buscar(u)
    l = base_de_datos.admins.buscar(u)
    if l == False and a == False:
        print('El usuario no fue encontrado, intente de nuevo')
    elif l != False:
        if (l[2] == u and l[3] == hashlib.md5(c.encode('ascii')).hexdigest()):
            print("Entramos como admin")
            return True
    elif a !=False:
        if (a[6] == u and a[7] == hashlib.md5(c.encode('ascii')).hexdigest()):
            print("Entramos como estudiantes")
            return True
    else:
        print('El usuario o la contrasena son incorrectos')
        return False


def registrar():
    """
        Esta es la segunda opción del menú principal. La función permite registrar un nuevo usuario de tipo estudiante o admin. Primero, el sistema le pide los datos necesarios al usuario que está creando la cuenta, este mismo verifica si el usuario ingresado ya está regstrado en el sistema. Una vez que el sisteema haya recolectado los datos para la creación de la cuenta, verifica el tipo indicado por el usuario para darle la forma adecuada dentro de la base de datos.
        Esta función no recibe parámetros."""
    global estudiantes
    global usuarios
    nombre = input("Ingrese el nombre del usuario a registrar: ")
    tipo = input("Ingrese el tipo de usuario a registrar: (admin/estudiante)")
    telefono = input("Ingrese el numero de telefono del usuario: ")
    usuario = input("Ingrese el usuario a registrar: ")
    contraseña = input("Ingrese la contraseña del usuario a registrar: ")

    if tipo == 'admin':
        for i in usuarios:
            if i['autenticacion']['usuario'] == usuario:
                print('El nombre de usuario no se encuentra disponible')
        else:
            usuarios.append({
                'nombre': nombre,
                'tipo': tipo,
                'telefono': telefono,
                'autenticacion': {
                    'usuario': usuario,
                    'contraseña': hashlib.md5(contraseña.encode('ascii')).hexdigest()
                }
            })
        print("""El administrador se ha ingresado correctamente
        """)

    elif tipo == 'estudiante':
        for i in estudiantes:
            if i['autenticacion']['usuario'] == usuario:
                print('El nombre de usuario no se encuentra disponible')
        else:
            estudiantes.append({
                'nombre': nombre,
                'tipo': tipo,
                'tiempo': int,
                'estudios':
                {
                    'carreras': [],
                    'cursos': [],
                    'aprobados' : [],
                    'reprobados' : []
                },
                'autenticacion': {
                    'usuario': usuario,
                    'contraseña': hashlib.md5(contraseña.encode('ascii')).hexdigest()
                },
                'horario':
                {
                    'lunes':      {7: [], 8: [], 9: [], 10: [], 11: [], 12: [], 13: [], 14: [], 15: [], 16: [], 17: [], 18: [], 19: [], },
                    'martes':     {7: [], 8: [], 9: [], 10: [], 11: [], 12: [], 13: [], 14: [], 15: [], 16: [], 17: [], 18: [], 19: [], },
                    'miercoles':  {7: [], 8: [], 9: [], 10: [], 11: [], 12: [], 13: [], 14: [], 15: [], 16: [], 17: [], 18: [], 19: [], },
                    'jueves':     {7: [], 8: [], 9: [], 10: [], 11: [], 12: [], 13: [], 14: [], 15: [], 16: [], 17: [], 18: [], 19: [], },
                    'viernes':    {7: [], 8: [], 9: [], 10: [], 11: [], 12: [], 13: [], 14: [], 15: [], 16: [], 17: [], 18: [], 19: [], },
                    'sabado':     {7: [], 8: [], 9: [], 10: [], 11: [], 12: [], 13: [], 14: [], 15: [], 16: [], 17: [], 18: [], 19: [], },
                    'domingo':    {7: [], 8: [], 9: [], 10: [], 11: [], 12: [], 13: [], 14: [], 15: [], 16: [], 17: [], 18: [], 19: [], },

                },
                'reporte':
                {
                    'lunes':      [],
                    'martes':     [],
                    'miercoles':  [],
                    'jueves':     [],
                    'viernes':    [],
                    'sabado':     [],
                    'domingo':    [],
                }
            })
        print("""El estudiante se ha ingresado correctamente
        """)

    else:
        print("Este tipo de usuario no es válido")


# Según el tipo de usuario se mostrará una interfaz diferente definida por su tipo de usuario


def menu(tipo, usuario, nombre):
    """
        Esta función imprime el menú de opciones para cada tipo de usuarios (admin/estudiante). La función detecta el usuario usuario que le llega y apartir de este geberal el menú de opciones, las cuales son diferentes entre los tipos de usuarios. Para esto se utiliza un condicional. Después de haber impreso el menú de opciones, se le pedirá al usuario que seleccione una, y esta se enviará como parámetro a otra función.

        Parámetros:
        - tipo (str): este es el tipo de cuenta que ha iniciado sesión, lo necesitamos para que el sistema sepa cuál es el menú que debe imprimir.
        - nombre (str): el nombre del usuario de la cuenta, este se usa para imprimir el saludo de bienvenida."""
    if tipo == "admin":
        print("""********************************* Bienvenido {} *********************************
            Menu de opciones:
            1: Agregar cursos
            2: Modificar cursos
            3: Agregar carreras
            4: Modificar carreras
            5: Salir del usuario
            """.format(nombre))
        opcion = int(input("¿Qué acción desea realizar? "))
        funciones_admin(opcion)
    elif tipo == "estudiante":
        print("""
            ********************************* Bienvenido {} *********************************
            Menu de opciones:
            1: Matricular una carrera
            2: Matricular un curso
            3: Generar reporte
            4: Registrar una actividad
            5: Determinar el estado de un curso
            6: Ver horario
            7: Salir del usuario
            """.format(nombre))
        opcion = int(input("¿Qué acción desea realizar? "))
        funciones_estudiante(opcion, usuario)


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

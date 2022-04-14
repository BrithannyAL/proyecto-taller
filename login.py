#Se importan los dstos de los usuarios y las funciones para sus respectivas interfaces
from base_de_datos import usuarios
from base_de_datos import estudiantes
from funciones_admin import agregar_curso, modificar_curso, agregar_carrera, modificar_carrera
from funciones_estudiante import tbd
import hashlib

def login():
    correcto = False
    while correcto == False:
        print("Digite el usuario y contraseña para ingresar")
        usuario = input("Usuario: ")
        contra = hashlib.md5(input("Contraseña: ").encode('ascii')).hexdigest()
        for item in usuarios:
            if (usuario in item['autenticacion']['usuario']) and (contra in item['autenticacion']['contraseña']):
                correcto = True
                print("Ha ingresado como", item['tipo'])
                while 1 > 0:
                    menu(item['tipo'], usuario, item['nombre'])
        for item in estudiantes:
            if(usuario in item['autenticacion']['usuario'] and (contra in item['autenticacion']['contraseña'])):
                correcto = True
                print("Ha ingresado como ", item['tipo'])
                while 1 > 0:
                    menu(item['tipo'], usuario,)
        if correcto == False:
            print("Vuelva a intentar")
            
#Según el tipo de usuario se mostrará una interfaz diferente definida por su tipo de usuario

def menu(tipo, usuario, nombre):
    if tipo == "admin":
        print("""********************************* Bienvenido {} *********************************
            Menu de opciones:
            1: Agregar cursos
            2: Modificar cursos
            3: Agregar carreras
            4: Modificar carreras
            5: Salir
            """.format(nombre))
        opcion = int(input("¿Qué acción desea realizar? "))
        funciones_admin(opcion)
    elif tipo == "estudiante":
        print("""
            ********************************* Bienvenido {} *********************************
            Menu de opciones:
            1: Matricular una carrera
            2: Matricular un curso
            3: tbd
            4: tbd
            5: Salir
            """.format(usuario))
        opcion = int(input("¿Qué acción desea realizar? "))
        funciones_estudiante(opcion, usuario)


def funciones_admin(opcion):
    if opcion == 1:
        agregar_curso()
    elif opcion == 2:
        modificar_curso()
    elif opcion == 3:
        agregar_carrera()
    elif opcion == 4:
        modificar_carrera()
    elif opcion == 5:
        quit()

def funciones_estudiante(opcion, usuario):
    if opcion == 1:
        matricular_carrera(usuario)
    elif opcion == 2:
        matricular_curso(usuario)
    elif opcion == 3:
        tbd()
    elif opcion == 5:
        quit()

#Se importan los dstos de los usuarios y las funciones para sus respectivas interfaces
from base_de_datos import usuarios
from base_de_datos import estudiantes
from funciones_admin import agregar_curso, modificar_curso, agregar_carrera, modificar_carrera
from funciones_estudiante import matricular_carrera, matricular_curso, tbd, tbd2
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
                menu(item['tipo'])
        for item2 in estudiantes:
            if(usuario in item2['autenticacion']['usuario'] and (contra in item2['autenticacion']['contraseña'])):
                correcto = True
                print("Ha ingresado como ", item['tipo'])
                menu(item2['tipo'])
        if correcto == False:
            print("Vuelva a intentar")
            
#Según el tipo de usuario se mostrará una interfaz diferente definida por su tipo de usuario

def menu(tipo):
    if tipo == "admin":
        print("""*********************************
             Bienvenido usuario {} *********************************
            Menu de opciones:
            1: Agregar cursos
            2: Modificar cursos
            3: Agregar carreras
            4: Modificar carreras
            5: Salir
            """.format(tipo))
        opcion = int(input("¿Qué acción desea realizar? "))
        funciones_admin(opcion)
    elif tipo == "estudiante":
        print("""
            ********************************* Bienvenido usuario {} *********************************
            Menu de opciones:
            1: Matricular una carrera
            2: Matricular un curso
            3: tbd
            4: tbd
            5: Salir
            """.format(tipo))
        opcion = int(input("¿Qué acción desea realizar? "))
        funciones_estudiante(opcion)


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
        print(quit())

def funciones_estudiante(opcion):
    if opcion == 1:
        matricular_carrera()
    elif opcion == 2:
        matricular_curso()
    elif opcion == 3:
        tbd()
    elif opcion == 4:
        tbd2()

#Se importan los dstos de los usuarios y las funciones para sus respectivas interfaces
from tkinter import E
from base_de_datos import usuarios, estudiantes, carreras, cursos
from funciones_admin import agregar_curso, modificar_curso, agregar_carrera, modificar_carrera
from funciones_estudiante import matricular_carrera, matricular_curso, ver_horario
import hashlib


def login():
    correcto = False
    while correcto == False:
        print("Digite el usuario y contraseña para ingresar")
        print("Presione 'x' para cerrar el software")
        usuario = input("Usuario: ")
        if usuario == "x":
            quit()
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
                    menu(item['tipo'], usuario, item['nombre'])
        if correcto == False:
            print("Vuelva a intentar")

def registrar():
    nombre = input("Ingrese el nombre del usuario a registrar: ")
    tipo = input("Ingrese el tipo de usuario a registrar: ")
    telefono = input("Ingrese el numero de telefono del usuario: ")
    usuario = input("Ingrese el usuario a registrar: ")
    contraseña = input("Ingrese la contraseña del usuario a registrar: ")

    if tipo == 'admin':
        for i in usuarios:
            if i['autenticacion']['usuario'] == usuario:
                print('El nombre de usuario no se encuentra disponible')
            else:
                pass
    elif tipo == 'estudiante':
        pass
    else:
        print("Este tipo de usuario no es válido")
    
    
    return 
            
#Según el tipo de usuario se mostrará una interfaz diferente definida por su tipo de usuario
def menu(tipo, usuario, nombre):
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
            3: Ver mi horario
            4: tbd
            5: Salir del usuario
            """.format(usuario))
        opcion = int(input("¿Qué acción desea realizar? "))
        funciones_estudiante(opcion, usuario, carreras, cursos, estudiantes)


def funciones_admin(opcion):
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
        login()


def funciones_estudiante(opcion, usuario, carreras, cursos, estudiantes):
    if opcion == 1:
        matricular_carrera(usuario, carreras, cursos, estudiantes)
    elif opcion == 2:
        matricular_curso(usuario, carreras, cursos, estudiantes)
    elif opcion == 3:
        ver_horario(usuario, carreras, cursos, estudiantes)
    elif opcion == 5:
        login()

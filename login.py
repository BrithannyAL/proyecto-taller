from base_de_datos import usuarios
from funciones_admin import agregar_curso, modificar_curso, agregar_carrera, modificar_carrera
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
        if correcto == False:
            print("Vuelva a intentar")
            
def menu(tipo):
    if tipo == "admin":
        print("""
            ********************************* Bienvenido usuario {} *********************************
            Menu de opciones:
            1: Agregar cursos
            2: Modificar cursos
            3: Agregar carreras
            4: Modificar carreras
            """.format(tipo))
        
        opcion = int(input("¿Qué acción desea realizar? "))
        funciones_admin(opcion)

def funciones_admin(opcion):
    if opcion == 1:
        agregar_curso()
    elif opcion == 2:
        modificar_curso()
    elif opcion == 3:
        agregar_carrera()
    elif opcion == 4:
        modificar_carrera()

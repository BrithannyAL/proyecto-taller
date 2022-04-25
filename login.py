#Se importan los dstos de los usuarios y las funciones para sus respectivas interfaces
from tkinter import E
from base_de_datos import usuarios, estudiantes, carreras, cursos
from funciones_admin import agregar_curso, modificar_curso, agregar_carrera, modificar_carrera
from funciones_estudiante import generar_reporte, matricular_carrera, matricular_curso, generar_reporte, registro_actividades, aprobado_noAprobado
import hashlib

def inicio():
    opcion = input("""
Digite 1 si desea iniciar sesión 
Digite 2 si desea registrarse
Digite x si desea cerrar el software
""")
    if opcion == '1':
        login()
    elif opcion == '2':
        registrar()
    elif opcion == 'x':
        quit()
    else: 
        print("")
        print("Por favor ingrese una opcion valida")
        inicio()

def login():
    correcto = False
    while correcto == False:
        print("Digite el usuario y contraseña para ingresar")
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
            usuarios.append({
            'nombre' : nombre,
            'tipo' : tipo,
            'telefono' : telefono,
            'autenticacion' :{
                'usuario' : usuario,
                'contraseña' : hashlib.md5(contraseña.encode('ascii')).hexdigest()
                                } 
                                })
        print("""El administrador se ha ingresado correctamente
        """)
        inicio()
    elif tipo == 'estudiante':
        for i in estudiantes:
            if i['autenticacion']['usuario'] == usuario:
                print('El nombre de usuario no se encuentra disponible')
        else:
            estudiantes.append({
            'nombre' : nombre,
            'tipo' : tipo,
            'tiempo' : int,
            'estudios':
                {
                'carreras': [],
                'cursos': [],
                },
            'autenticacion' :{
                'usuario' : usuario,
                'contraseña' : hashlib.md5(contraseña.encode('ascii')).hexdigest()
                             },
                'horario':
                            {
            'lunes':      {7: [], 8:[], 9:[], 10:[], 11:[], 12:[], 13:[], 14:[], 15:[], 16:[], 17:[], 18:[], 19:[], },
            'martes':     {7: [], 8:[], 9:[], 10:[], 11:[], 12:[], 13:[], 14:[], 15:[], 16:[], 17:[], 18:[], 19:[], },
            'miercoles':  {7: [], 8:[], 9:[], 10:[], 11:[], 12:[], 13:[], 14:[], 15:[], 16:[], 17:[], 18:[], 19:[], },
            'jueves':     {7: [], 8:[], 9:[], 10:[], 11:[], 12:[], 13:[], 14:[], 15:[], 16:[], 17:[], 18:[], 19:[], },
            'viernes':    {7: [], 8:[], 9:[], 10:[], 11:[], 12:[], 13:[], 14:[], 15:[], 16:[], 17:[], 18:[], 19:[], },
            'sabado':     {7: [], 8:[], 9:[], 10:[], 11:[], 12:[], 13:[], 14:[], 15:[], 16:[], 17:[], 18:[], 19:[], },
            'domingo':    {7: [], 8:[], 9:[], 10:[], 11:[], 12:[], 13:[], 14:[], 15:[], 16:[], 17:[], 18:[], 19:[], },

                            },
                'reporte' : 
                {
                    'lunes':      {7: {}, 8: {}, 9: {}, 10:{}, 11:{}, 12:{}, 13:{}, 14:{}, 15:{}, 16:{}, 17:{}, 18:{}, 19:{}, 20:{}, 21:{}, 22:{}, 23:{}, 24:{} },
                    'martes':     {7: {}, 8: {}, 9: {}, 10:{}, 11:{}, 12:{}, 13:{}, 14:{}, 15:{}, 16:{}, 17:{}, 18:{}, 19:{}, 20:{}, 21:{}, 22:{}, 23:{}, 24:{}},
                    'miercoles':  {7: {}, 8: {}, 9: {}, 10:{}, 11:{}, 12:{}, 13:{}, 14:{}, 15:{}, 16:{}, 17:{}, 18:{}, 19:{}, 20:{}, 21:{}, 22:{}, 23:{}, 24:{} },
                    'jueves':     {7: {}, 8: {}, 9: {}, 10:{}, 11:{}, 12:{}, 13:{}, 14:{}, 15:{}, 16:{}, 17:{}, 18:{}, 19:{}, 20:{}, 21:{}, 22:{}, 23:{}, 24:{}},
                    'viernes':    {7: {}, 8: {}, 9: {}, 10:{}, 11:{}, 12:{}, 13:{}, 14:{}, 15:{}, 16:{}, 17:{}, 18:{}, 19:{}, 20:{}, 21:{}, 22:{}, 23:{}, 24:{}},
                    'sabado':     {7: {}, 8: {}, 9: {}, 10:{}, 11:{}, 12:{}, 13:{}, 14:{}, 15:{}, 16:{}, 17:{}, 18:{}, 19:{}, 20:{}, 21:{}, 22:{}, 23:{}, 24:{}},
                    'domingo':    {7: {}, 8: {}, 9: {}, 10:{}, 11:{}, 12:{}, 13:{}, 14:{}, 15:{}, 16:{}, 17:{}, 18:{}, 19:{}, 20:{}, 21:{}, 22:{}, 23:{}, 24:{}},
                }
                                })
        print("""El estudiante se ha ingresado correctamente
        """)
        inicio()
    else:
        print("Este tipo de usuario no es válido")
        inicio() 
            
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
            3: Generar reporte
            4: Registrar una actividad
            5: Deternminar el estado de un curso
            6: Salir del usuario
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
        opci = input("¿Desea cerrar la aplicación? (y/n)")
        if opci == "y":
            quit()
        login()

def funciones_estudiante(opcion, usuario):
    global carreras
    global cursos
    global estudiantes
    if opcion == 1:
        matricular_carrera(usuario, carreras, cursos, estudiantes)
    elif opcion == 2:
        matricular_curso(usuario, carreras, cursos, estudiantes)
    elif opcion == 3:
        generar_reporte(usuario, carreras, cursos, estudiantes)
    elif opcion == 4:
        registro_actividades(usuario, carreras, cursos, estudiantes)
    elif opcion == 5:
       aprobado_noAprobado(usuario, estudiantes)
    elif opcion == 6:
        opci = input("¿Desea cerrar la aplicación? (y/n)")
        if opci == "y":
            quit()
        login()

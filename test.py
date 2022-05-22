from cargar_en_archivos import cargar_archivos_estudiantes, cargar_archivos_admins, cargar_archivos_cursos, cargar_archivos_carreras
from base_de_datos import carreras, cursos
import hashlib

def escribir_carreras():
    global cargar_archivos_carreras
    list_carreras = cargar_archivos_carreras()
    list_carreras = carreras('Ingenieria en computacion', 8 , [1, 2, 3, 4, 5, 6, 7] , 1)
    list_carreras.insertar(carreras('Ingenieria en agronomia', 8 ,[1, 2, 3, 8, 9, 10 ] , 2))
    list_carreras.insertar(carreras('Administracion de empresas', 10 ,[1, 2, 3, 11, 12, 13 ] , 3))
    list_carreras.insertar(carreras('Administracion en produccion industrial', 12 ,[1, 2, 3, 14, 15] , 4 ))
    list_carreras.insertar(carreras('Ingenieria en electronica', 10 ,[1, 2, 3, 4, 16, 17] , 5 ))
    list_carreras.guardar_en_archivos()
    
def escribir_cursos():
    global cargar_archivos_cursos
    list_cursos = cargar_archivos_cursos()
    
    list_cursos = cursos('Matematica general' , 3 , 3,  ['lunes', 9, 12] , 1)
    list_cursos.insertar(cursos('Comunicacion escrita' , 2 , 3 , ['martes', 9, 12] , 2))
    list_cursos.insertar(cursos('Ingles 1' , 2 , 3 , ['miercoles', 9, 12] , 3))
    list_cursos.insertar(cursos('Introduccion a la programacion' , 2 , 3 , ['martes', 7, 8] , 4))
    list_cursos.insertar(cursos('Taller de programacion' , 3 , 3 , ['jueves', 9, 12] , 5))
    list_cursos.insertar(cursos('Fundamentos de organizacion de computadoras' , 2 , 3 , ['viernes', 9, 12] , 6))
    list_cursos.insertar(cursos('Marematica discreta' , 3 , 3 , ['lunes', 13, 14] , 7))
    list_cursos.insertar(cursos('Introduccion a la agronomia' , 3 , 3 , ['lunnes', 13, 14] , 8))
    list_cursos.insertar(cursos('Agromatica ' , 3 , 3 , ['miercoles', 14, 15] , 9))
    list_cursos.insertar(cursos('Biologia general' , 3 , 3 , ['jueves', 16, 17] , 10))
    list_cursos.insertar(cursos('Introducciona a la administracion de empresas' , 2 , 3 , ['viernes', 18, 19] , 11))
    list_cursos.insertar(cursos('Computacion para administracion' , 2 , 3 , ['lunes', 18, 19] , 12))
    list_cursos.insertar(cursos('Matematica para administracion' , 3 , 3 , ['martes', 14, 15] , 13))
    list_cursos.insertar(cursos('Dibijo tecnico' , 2 , 3 , ['miercoles', 19, 19] , 14))
    list_cursos.insertar(cursos('Quimica basica' , 2 , 3 , ['martes', 9, 12] , 15))
    list_cursos.insertar(cursos('Introduccion a la ingenieria' , 3 , 3 , ['martes', 13, 14] , 16))
    list_cursos.insertar(cursos('Calculo diferencial e integral' , 4 , 3 , ['miercoles', 18, 19] , 17))
    list_cursos.guardar_en_archivos()


u = 'fdgtrgt'
c = '12345'

estudiantes = cargar_archivos_estudiantes()
admins = cargar_archivos_admins()
registro_actual = None
tipo = None

while registro_actual == None:
    if admins.usuario == u and admins.contrasena == hashlib.md5(c.encode('ascii')).hexdigest():
        registro_actual = admins
        tipo = 1
    else:
        if admins.sig != None:
            admins = admins.sig
        else:
            if estudiantes.usuario == u and estudiantes.contrasena == hashlib.md5(c.encode('ascii')).hexdigest():
                registro_actual = estudiantes
                tipo = 2
            else:
                if estudiantes.sig != None:
                    estudiantes = estudiantes.sig
                else:
                    registro_actual = False
        
                    
if registro_actual != False:
    print(tipo)
    print(registro_actual)
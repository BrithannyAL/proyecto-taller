from base_de_datos import carreras
from base_de_datos import cursos
from login import menu_login

def agregar_curso():
    last_code = cursos[-1]['código']
    curso = input("Ingrese el nombre del curso que desea agregar: ")
    creditos = input("Ingrese la cantidad de creditos del curso: ")
    profesor = input("Ingrese el nombre del profesor del curso: ")
    codigo   = last_code + 1
    nuevo_curso = {'curso' : curso, 'creditos' : creditos, 'Profesor' : profesor, 'código' : codigo}
    cursos.append(nuevo_curso)
    print("""
          El nuevo curso es:
          {}""".format(nuevo_curso))
    #menu("admin")
    
def modificar_curso():
    print("Función que modifica curso")
    
def agregar_carrera():
    carrera_cursos = []
    salir = False
    carrera_name = input("Ingrese el nombre de la carrera que desea agregar: ")
    carrera_semestres = input("Ingrese la cantidad de semestres de la carrera: ")
    while salir == False:
        carrera_cursos.append(input("Ingrese los códigos de los cursos de dicha carrera: "))
        print("Presione x cuando haya terminado de agregar cursos.")
        for i in carrera_cursos:
            if i == "x":
                del carrera_cursos[-1]  
                salir = True
    nueva_carrera = {'carrera' : carrera_name, 'semestres' : carrera_semestres, 'cursos' : carrera_cursos}
    carreras.append(nueva_carrera)
    print(nueva_carrera)
    #menu("admin")
    
def modificar_carrera():
    print("Función que modifica carrera")
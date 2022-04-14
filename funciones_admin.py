from base_de_datos import carreras
from base_de_datos import cursos

def agregar_curso():
    last_code = cursos[-1]['código']
    curso = input("Ingrese el nombre del curso que desea agregar: ")
    creditos = input("Ingrese la cantidad de creditos del curso: ")
    profesor = input("Ingrese el nombre del profesor del curso: ")
    codigo   = last_code + 1
    nuevo_curso = {'curso' : curso, 'creditos' : creditos, 'Profesor' : profesor, 'codigo' : codigo}
    cursos.append(nuevo_curso)
    print("""
          El nuevo curso es:
          {}""".format(nuevo_curso))
    #menu("admin")
    
def modificar_curso():
    imprimir_cursos()
    curso_a_modificar = int(input("Escriba el código del curso que desea modificar: "))
    nombre_curso = input("""
                         El título del curso es {}
                         ¿Desea modificar el nombre del curso? (y/n) """
                         .format(cursos[curso_a_modificar]['curso']))
    profe = input("""
                  El nombre del profesor del curso es {}
                  ¿Desea modificar el profesor que imparte el curso? (y/n) """
                  .format(cursos[curso_a_modificar]['Profesor']))
    if nombre_curso == "y":
        cursos[curso_a_modificar]['curso'] = input("Nuevo título para el curso: ")
    if profe == "y":
        cursos[curso_a_modificar]['Profesor'] = input("Nuevo profesor para el curso: ")
    print("""El curso ha sido modificado: {}""".format(cursos[curso_a_modificar]))
        
    
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

def imprimir_cursos():
    print("***** Lista de cursos *****")
    for item in cursos:
        print("Código {}, curso {}".format(item['codigo'], item['curso']))
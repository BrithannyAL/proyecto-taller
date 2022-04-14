from base_de_datos import carreras
from base_de_datos import cursos
from base_de_datos import estudiantes

def matricular_carrera(usuario):
    carrera_m = input("Ingrese el nombre de la carrera que desea matricular: ")
    for i in estudiantes:
        if estudiantes[i]['nombre'] == usuario:
            estudiantes[i]['carrera'] = carrera_m

def matricular_curso():
    print("Matricular curso")

def tbd():
    print("tbd")

def tbd2():
    print("tbd")
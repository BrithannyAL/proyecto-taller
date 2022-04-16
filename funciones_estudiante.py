from base_de_datos import carreras
from base_de_datos import cursos
from base_de_datos import estudiantes

def matricular_carrera(usuario):
    print("")
    print("Las carreras disponibles son: ")
    print("")
    for i in carreras:
        print(i['carrera'])
        print("")
    carrera_m = input("Ingrese el nombre de la carrera que desea matricular: ")
    for i in estudiantes:
        if i['autenticacion']['usuario'] == usuario:
            for x in carreras:
                if x['carrera'] == carrera_m:
                    i['carrera'] = carrera_m
                    print(i)
                    break
            else:
                print("La carrera ingresada no existe")
        



def matricular_curso(usuario):
    curso_m = input("Ingrese el nombre del curso que desea matricular: ")
    for i in estudiantes:
        if i['autenticacion']['usuario'] == usuario:
            for x in cursos:
                if x['curso'] == curso_m:
                    i['curso'] = curso_m
                    print(i)
                    break
            else:
                print("El curso ingresado no existe")
    for x in cursos:
        for y in estudiantes:
            if x['horario_de_clases'][0] == y['horario']:
                print("")





def ver_horario(usuario):
    
    for i in estudiantes:
        if i['autenticacion']['usuario'] == usuario:
            print (i['horario'])
            print("")

def tbd2():
    print("tbd")
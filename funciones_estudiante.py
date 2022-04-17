from base_de_datos import carreras
from base_de_datos import cursos
from base_de_datos import estudiantes
import pprint

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
                for y in estudiantes:
                    if x['horario_de_clases'][0] in y['horario']: #Entra al horario y recorre los dias, por lo tanto el dia ya es el mismo
                        llaves_dias = list
                        llaves_dias = y['horario'].keys()
                        for a in llaves_dias:
                           if x['horario_de_clases'][0] == a:
                                dia = a
                                llaves_horas = list
                                llaves_horas = y['horario'][dia].keys()
                                for b in llaves_horas:
                                    if x['horario_de_clases'][1] == b:
                                        hora = b
                                        print(y['horario'][dia][hora] )
                                        print(x['horario_de_clases'][2])
                                        y['horario'][dia][hora] = curso_m
                                        pprint.pprint(y['horario'])
                                        quit()
                                break
                        print(dia)
                    else:
                        print("Dia no encontrado")
                    break
            else:
                print("El curso ingresado no existe")






def ver_horario(usuario):
    
    for i in estudiantes:
        if i['autenticacion']['usuario'] == usuario:
            print (i['horario'])
            print("")

def tbd2():
    print("tbd")
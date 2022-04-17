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
    flag = False
    print("Estos son los cursos disponibles: ")
    for o in cursos:    
        print(o['curso'])
        print(" ")
    curso_m = input("Ingrese el nombre del curso que desea matricular: ")
    for i in estudiantes:
        if i['autenticacion']['usuario'] == usuario:
            for x in cursos:
                if flag == True:
                    break
                if x['curso'] == curso_m:
                    if flag == True:
                        break
                    for y in estudiantes:
                        if flag == True:
                            break
                        if x['horario_de_clases'][0] in y['horario']: #Entra al horario y recorre los dias, por lo tanto el dia ya es el mismo
                            llaves_dias = list
                            llaves_dias = y['horario'].keys()
                            for a in llaves_dias:
                                if flag == True:
                                    break
                                if x['horario_de_clases'][0] == a:
                                    dia = a
                                    llaves_horas = list
                                    llaves_horas = y['horario'][dia].keys()
                                    for b in llaves_horas:
                                        if x['horario_de_clases'][1] == b:
                                            hora = b
                                            hora_inicio = x['horario_de_clases'][1]
                                            hora_final  = x['horario_de_clases'][2]
                                            cantidad_horas = hora_final - hora_inicio

                                            for contador in range(cantidad_horas):
                                                contador = 1
                                                y['horario'][dia][hora] = curso_m
                                                hora = hora + contador
                                                contador =+ 1
                                            print(y['horario'][dia])
                                            flag = True
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
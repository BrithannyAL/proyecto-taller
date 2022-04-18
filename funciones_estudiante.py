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
                if  x['carrera'] == carrera_m:
                    i['estudios']['carreras'] = carrera_m
                    print(i)
                    break
            else:
                print("La carrera ingresada no existe")
    
    #buscar si el codigo del curso esta en los codigos de la carrera y la carrera del estudiante
    #si el codigo del curso esta en la carrera entonces puede matricularlo pero hay que verificar que el estudiante esté en esa carrera
    #Si el código está en el estudiante pero no en la carrera no debería poder
    #Si el código está en el estudiante pero no en la carrera tampoco
    

def matricular_curso(usuario):
    flag = False
    print("Estos son los cursos disponibles: ")
    
    #IMPRIME LOS NOMBRES LOS CURSOS
    for o in cursos:    
        print(o['curso'])
        print(" ")
    #IMPRIME LOS NOMBRES LOS CURSOS
    
    curso_m = input("Ingrese el nombre del curso que desea matricular: ")
    
    for i in estudiantes:
        if i['autenticacion']['usuario'] == usuario:
            if i['estudios']['carreras'] == ():
                print("Primero ingrese una carrera")
                break
            else:
                carreras_en_curso = i['estudios']['carreras'] 
                for x in cursos:
                    if flag == True:
                        break
                    if x['curso'] == curso_m:
                        codigo_curso = x['codigo']
                        for l in carreras:
                            if l['carrera'] == carreras_en_curso: #Entro a la carrera del estudiante
                                if codigo_curso in l['cursos'] :
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
                                    print("El curso ingresado no pertenece a la carrera matriculada")  
                                    flag = True
                                    break                                                  
                else:
                    print("El curso ingresado no existe")


def ver_horario(usuario):
    
    for i in estudiantes:
        if i['autenticacion']['usuario'] == usuario:
            print ('Lunes: ' , i['horario']['lunes'])
            print ('Martes: ' , i['horario']['martes'])
            print ('Miercoles: ' , i['horario']['miercoles'])
            print ('Jueves: ' , i['horario']['jueves'])
            print ('Viernes: ' , i['horario']['viernes'])
            print ('Sabado: ' , i['horario']['sabado'])
            print ('Domingo: ' , i['horario']['viernes'])
            print("")

def tbd2():
    print("tbd")





    

from cgitb import reset
from tkinter.tix import Tree
from turtle import home
from funciones import horas_horario, verificar_curso

class bcolors:
    green = '\033[92m' #Verde
    yellow = '\033[93m' #Amarillo
    red = '\033[91m' #Rojo
    reset = '\033[0m' #RESETEAR COLOR

def matricular_carrera(usuario, carreras, cursos, estudiantes):
    print("")
    print("Las carreras disponibles son: ")
    for i in carreras:
        print(i['carrera'])
        print("")
    carrera_m = input("Ingrese el nombre de la carrera que desea matricular: ")
    for i in estudiantes:
        if i['autenticacion']['usuario'] == usuario:
            for x in carreras:
                if x['carrera'] == carrera_m:
                    i['estudios']['carreras'].append(carrera_m)
                    print('La carrera se ha matriculado existosamente')
                    break
            else:
                print("La carrera ingresada no existe")
    return estudiantes

    # buscar si el codigo del curso esta en los codigos de la carrera y la carrera del estudiante
    # si el codigo del curso esta en la carrera entonces puede matricularlo pero hay que verificar que el estudiante esté en esa carrera
    # Si el código está en el estudiante pero no en la carrera no debería poder
    # Si el código está en el estudiante pero no en la carrera tampoco

def matricular_curso(usuario, carreras, cursos, estudiantes):
    flag = False
    print("Estos son los cursos disponibles: ")
    for o in cursos:
        print(o['curso'])
        print(" ")
    curso_m = input("Ingrese el nombre del curso que desea matricular: ")
    for i in estudiantes:
        if i['autenticacion']['usuario'] == usuario:
            if i['estudios']['carreras'] == []:
                print("Primero ingrese una carrera")
                break
            else:                                                                                   
                carreras_en_curso = i['estudios']['carreras']
                for r_cursos in cursos:
                    if flag == True:
                        break
                    if r_cursos['curso'] == curso_m:
                        codigo_curso = r_cursos['codigo']
                        for r_carreras in carreras:
                            # Entro a la carrera del estudiante
                            if r_carreras['carrera'] in carreras_en_curso:
                                if codigo_curso in r_carreras['cursos']:
                                    if flag == True:
                                        break
                                    if flag == True:
                                        break
                                        # Entra al horario y recorre los dias, por lo tanto el dia ya es el mismo
                                    if r_cursos['horario_de_clases'][0] in i['horario']:
                                        llaves_dias = list
                                        llaves_dias = i['horario'].keys()
                                        for a in llaves_dias:
                                            if flag == True:
                                                break 
                                            if r_cursos['horario_de_clases'][0] == a:
                                                dia = a
                                                llaves_horas = list
                                                llaves_horas = i['horario'][dia].keys(
                                                    )
                                                for b in llaves_horas:
                                                    if r_cursos['horario_de_clases'][1] == b:
                                                        hora = b
                                                        hora_inicio = int(r_cursos['horario_de_clases'][1])
                                                        hora_final = int(r_cursos['horario_de_clases'][2])
                                                        cantidad_horas = hora_final - hora_inicio
                                                        if cantidad_horas == 0:
                                                            cantidad_horas = 1
                                                        for contador in range(cantidad_horas):
                                                            contador = 1
                                                            if i['horario'][dia][hora] == []:
                                                                horas_dia = horas_horario(usuario, estudiantes, r_cursos['horario_de_clases'][0]) ##
                                                                horas_semana = horas_horario(usuario, estudiantes, 'semana')
                                                                if cantidad_horas + horas_dia > 12:
                                                                    print("Está excediendo las 12 horas diarias")
                                                                    flag = True
                                                                    break
                                                                if cantidad_horas + horas_semana > 72:
                                                                    print("Está excediendo las 72 horas semanales")
                                                                    flag = True
                                                                    break
                                                                i['horario'][dia][hora] = [curso_m]
                                                                hora = hora + contador
                                                                contador = + 1
                                                                i['estudios']['cursos'].append(codigo_curso)
                                                                con = True
                                                            else:
                                                                print(
                                                                    "Usted tiene un choque de horarios")
                                                                flag = True
                                                                break
                                                        if flag == True:
                                                            break
                                                        print('Matricula realizada con exito')
                                                        flag = True
                                                        break
                                else:
                                    print(
                                        "El curso ingresado no pertenece a la carrera matriculada")
                                    flag = True
                                    break
                else:
                    print("El curso ingresado no existe")
    if con == True:
        i['reporte'][dia].append([curso_m,'curso',cantidad_horas, carreras_en_curso,])
    return estudiantes

def generar_reporte(usuario, carreras, cursos, estudiantes):
    horas_d = 0
    dia = input('''Ingrese el día del que quiere generar el reporte: 
Ingrese 'semana' si desea generar el reporte de la semana entera.
''')
    dias = ['lunes','martes','miercoles','jueves','viernes','sabado','domingo']
    if dia in dias:
        for i in estudiantes:
            if i['autenticacion']['usuario'] == usuario:
                print(dia, ': ')
                for l in i['reporte'][dia]:
                    if l[1] == 'ocio':
                        print(bcolors.green + 'Actividad: '+ str(l[0]) + bcolors.reset)
                        print(bcolors.green + 'Tipo: '+ str(l[1]) + bcolors.reset)
                        print(bcolors.green + 'Horas de dedicacion: ' + str(l[2]) + bcolors.reset)
                        porcentaje = l[2] * 100 // 18
                        print(bcolors.green + 'Porcentaje que ocupa en el día: ' + str(porcentaje) + '%' + bcolors.reset)
                        print('')
                    elif l[1] == 'curso':
                        print(bcolors.red + 'Actividad: '+ str(l[0]) + bcolors.reset)
                        print(bcolors.red + 'Tipo: '+ str(l[1]) + bcolors.reset)
                        print(bcolors.red + 'Horas de dedicacion: ' + str(l[2]) + bcolors.reset)
                        porcentaje = l[2] * 100 // 18
                        print(bcolors.red + 'Porcentaje que ocupa en el día: ' + str(porcentaje) + '%' + bcolors.reset)
                        print(bcolors.red + 'Carrera asociada: ' + str(l[3]) + bcolors.reset)
                        print('')
                    elif l[1] == 'Actividad extracurricular':
                        print(bcolors.yellow + 'Actividad: '+ str(l[0]) + bcolors.reset)
                        print(bcolors.yellow + 'Tipo: '+ str(l[1]) + bcolors.reset)
                        print(bcolors.yellow + 'Horas de dedicacion: ' + str(l[2]) + bcolors.reset)
                        porcentaje = l[2] * 100 // 18
                        print(bcolors.yellow + 'Porcentaje que ocupa en el día: ' + str(porcentaje) + '%' + bcolors.reset)
                        print(bcolors.yellow + 'Curso asociado: ' + str(l[3]) + bcolors.reset)
                        print('')
        horas_dia = horas_horario(usuario, estudiantes, dia)  
        horas_d = 18-horas_dia
        print('La cantidad de horas ocupadas este dia es de: ' , horas_dia)
        print('Tiene ', horas_d, 'horas disponibles el día ', dia)
        return estudiantes
    elif dia == 'semana':
        for i in estudiantes:
            llaves = list(i['reporte'].keys())
            if i['autenticacion']['usuario'] == usuario:
                for z in llaves:
                    print(z)
                    for l in i['reporte'][z]:
                        if l[1] == 'ocio':
                            print(bcolors.green + 'Actividad: '+ str(l[0]) + bcolors.reset)
                            print(bcolors.green + 'Tipo: '+ str(l[1]) + bcolors.reset)
                            print(bcolors.green + 'Horas de dedicacion: ' + str(l[2]) + bcolors.reset)
                            porcentaje = l[2] * 100 // 126
                            print(bcolors.green + 'Porcentaje que ocupa en la semana: ' + str(porcentaje) + '%' + bcolors.reset)
                            print('')
                        elif l[1] == 'curso':
                            print(bcolors.red + 'Actividad: '+ str(l[0]) + bcolors.reset)
                            print(bcolors.red + 'Tipo: '+ str(l[1]) + bcolors.reset)
                            print(bcolors.red + 'Horas de dedicacion: ' + str(l[2]) + bcolors.reset)
                            porcentaje = l[2] * 100 // 126
                            print(bcolors.red + 'Porcentaje que ocupa en la semana: ' + str(porcentaje) + '%' + bcolors.reset)
                            print(bcolors.red + 'Carrera asociada: ' + str(l[3]) + bcolors.reset)
                            print('')
                        elif l[1] == 'Actividad extracurricular':
                            print(bcolors.yellow + 'Actividad: '+ str(l[0]) + bcolors.reset)
                            print(bcolors.yellow + 'Tipo: '+ str(l[1]) + bcolors.reset)
                            print(bcolors.yellow + 'Horas de dedicacion: ' + str(l[2]) + bcolors.reset)
                            porcentaje = l[2] * 100 // 126
                            print(bcolors.yellow + 'Porcentaje que ocupa en la semana: ' + str(porcentaje) + '%' + bcolors.reset)
                            print(bcolors.yellow + 'Curso asociado: ' + str(l[3]) + bcolors.reset)
                            print('')
                        print('')
        
        horas_semana = horas_horario(usuario, estudiantes, dia)
        horas_libres = 126 - horas_semana
        print('La cantidad de horas ocupadas de esta semana es de: ' , horas_semana, ' horas')
        print('Tiene ', horas_libres, 'horas disponibles esta semana')
        return estudiantes
    else:
        print('El dato ingresado no es valido')
    

def registro_actividades(usuario, carreras, cursos, estudiantes):
    for i in estudiantes: 
        if i['autenticacion']['usuario'] == usuario:
            relacion_curso = input("Está su actividad relacionada con un curso? ")          
            if relacion_curso == 'si' or relacion_curso == 'Si':
                r_curso = input("A que curso está relacionada esta actividad? ")
                comp = verificar_curso(usuario, carreras, cursos, estudiantes, r_curso)
                if comp == True:
                    actividad = input("Cuál es el nombre de la actividad? ")
                    dia = input("Ingrese el día que va a realizar la actividad:")
                    hora_i = int(input("Ingrese la hora de inicio de la actividad: "))
                    hora_f = int(input("Ingrese la hora final de la actividad: "))
                    horas_t = hora_f - hora_i
                    horas_dia = horas_horario(usuario, estudiantes, dia) 
                    horas_semana = horas_horario(usuario, estudiantes, 'semana')
                    if horas_t + (horas_dia-1) > 12:
                        print("Está excediendo las 12 horas diarias")
                        break
                    if horas_t + horas_semana > 72:
                        print("Está excediendo las 72 horas semanales")
                        break
                    for z in range(horas_t):
                        if i['horario'][dia][hora_i] == []:
                            i['horario'][dia][hora_i] = [actividad]
                            hora_i = hora_i + 1
                        else:
                            print("Estas horas se presentan ocupadas")
                            break
                    i['reporte'][dia].append([actividad,'Actividad extracurricular',horas_t, r_curso])
                if comp == False:
                    print("Usted no está matriculado en este curso")
                    home()     
            elif relacion_curso == 'no' or relacion_curso == 'No':
                tipo = 'ocio'
                actividad = input ('Ingrese el nombre de la actividad: ')
                dia = input("Ingrese el día que va a realizar la actividad:")
                hora_i = int(input("Ingrese la hora de inicio de la actividad: "))
                hora_f = int(input("Ingrese la hora final de la actividad: "))
                horas_t = hora_f - hora_i
                horas_dia = horas_horario(usuario, estudiantes, dia) 
                horas_semana = horas_horario(usuario, estudiantes, 'semana')
                if horas_t + (horas_dia-1) > 12:
                    print("Está excediendo las 12 horas diarias")
                    break
                if horas_t + horas_semana > 72:
                    print("Está excediendo las 72 horas semanales")
                    break
                i['reporte'][dia].append([actividad,tipo,horas_t])
                for z in range(horas_t):
                    if i['horario'][dia][hora_i] == []:
                       i['horario'][dia][hora_i] = [actividad]
                       hora_i = hora_i + 1
                    else:
                        print("Estas horas se presentan ocupadas")
                        break
            else:
                print("Esa opcion no es válida")
                home()
    return estudiantes
                
def aprobado_noAprobado(usuario, estudiantes, cursos):
    cursos_del_estudiante = []
    for x in estudiantes:
        if x['autenticacion']['usuario'] == usuario:
            cursos_del_estudiante = x['estudios']['cursos']
    print("Los cursos en los que está matrículado son:")
    for cod in cursos_del_estudiante:
        for item in cursos:
            if item['codigo'] == cod:
                print("Cursos: {}, Curso: {}".format(item['codigo'], item['curso']))
    curso_a_modificar = int(input("Escriba al que se le cambiará el estado: "))
    estado = input("""
                   A = el curso está aprobado
                   R = el curso está reprobado
                   
                   ¿Cuál es el estado del curso? """)
    if estado == "A" or estado == "a":
        for x in estudiantes:
            if x['autenticacion']['usuario'] == usuario:
                x['estudios']['cursos'].remove(curso_a_modificar)
                x['estudios']['aprobados'].append(curso_a_modificar)
                print("Cursando: {}".format(x['estudios']['cursos']))
                print("Aprobados: {}".format(x['estudios']['aprobados']))
                break
    elif estado == "R" or estado == "r":
        for x in estudiantes:
            if x['autenticacion']['usuario'] == usuario:
                x['estudios']['cursos'].remove(curso_a_modificar)
                x['estudios']['reprobados'].append(curso_a_modificar)
                print("Cursando: {}".format(x['estudios']['cursos']))
                print("Reprobados: {}".format(x['estudios']['reprobados']))
                break

def ver_horario(usuario, estudiantes):
    dias = ['lunes','martes','miercoles','jueves','viernes','sabado','domingo']
    for x in estudiantes:
        if x['autenticacion']['usuario'] == usuario:
            for l in dias:
                print(x['horario'][l])
                print("")

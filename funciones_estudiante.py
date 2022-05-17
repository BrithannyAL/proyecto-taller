from turtle import home
from funciones import horas_horario, verificar_curso


class bcolors:
    green = '\033[92m'  # Verde
    yellow = '\033[93m'  # Amarillo
    red = '\033[91m'  # Rojo
    reset = '\033[0m'  # RESETEAR COLOR

def matricular_carrera(carrera, usuario , carreras_base):
    '''
        Esta funcion matricula una carrera en el usuario e imprime las carreras disponibles para matricular
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
                print("La carrera ingresada no existe")'''
    print([carrera,usuario,carreras_base])
    return ([carrera,usuario,carreras_base])


def matricular_curso(usuario, carreras, cursos, estudiantes):
    '''
    Esta funcion matricula un curso y tiene muchas comprobaciones dentro de ella para evitar errores, algunas de estas son; el evitar que se matricule un curso sin matricular una carrera antes o matricular un curso de una carrera que el usuario no ha matriculado '''
    carrera = str
    cursos_carrera = list
    flag = False
    con = False

    for r in estudiantes:
        if r['autenticacion']['usuario'] == usuario:
            if r['estudios']['carreras'] != []:
                carrera = r['estudios']['carreras']
                for p in carreras:
                    if carrera == [p['carrera']]:
                        cursos_carrera = p['cursos']
            elif r['estudios']['carreras'] == []:
                print('')
                print('Primero ingrese una carrera')
                print('')
                break
            else:
                break
            print("Estos son los cursos disponibles: ")
            for o in cursos:
                if o['codigo'] in cursos_carrera:

                    print(o['curso'])
                    print(" ")
            break
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
                        if codigo_curso in i['estudios']['aprobados']:
                            print(
                                "Usted no puede matricular este curso porque se encuentra aprobado")
                            flag = True
                            break
                        if codigo_curso in i['estudios']['reprobados']:
                            print(
                                "Usted no puede matricular este curso porque se encuentra reprobado")
                            flag = True
                            break
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
                                                        hora_inicio = int(
                                                            r_cursos['horario_de_clases'][1])
                                                        hora_final = int(
                                                            r_cursos['horario_de_clases'][2])
                                                        cantidad_horas = hora_final - hora_inicio
                                                        if cantidad_horas == 0:
                                                            cantidad_horas = 1
                                                        for contador in range(cantidad_horas):
                                                            contador = 1
                                                            if i['horario'][dia][hora] == []:
                                                                horas_dia = horas_horario(
                                                                    usuario, estudiantes, r_cursos['horario_de_clases'][0])
                                                                horas_semana = horas_horario(
                                                                    usuario, estudiantes, 'semana')
                                                                if cantidad_horas + horas_dia > 12:
                                                                    print(
                                                                        "Está excediendo las 12 horas diarias")
                                                                    flag = True
                                                                    break
                                                                if cantidad_horas + horas_semana > 72:
                                                                    print(
                                                                        "Está excediendo las 72 horas semanales")
                                                                    flag = True
                                                                    break
                                                                i['horario'][dia][hora] = [
                                                                    curso_m]
                                                                hora = hora + contador
                                                                contador = + 1
                                                                i['estudios']['cursos'].append(
                                                                    codigo_curso)
                                                                con = True
                                                            else:
                                                                print(
                                                                    "Usted tiene un choque de horarios")
                                                                flag = True
                                                                break
                                                        if flag == True:
                                                            break
                                                        print(
                                                            'Matricula realizada con exito')
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
        i['reporte'][dia].append(
            [curso_m, 'curso', cantidad_horas, carreras_en_curso, ])
    return estudiantes

def generar_reporte(usuario, carreras, cursos, estudiantes):
    '''
        Esta funcion genera los reportes de las actividades matriculadas e imprime sus distintos atributos, ademas de esto diferencia por colores cada tipo de actividad'''
    horas_d = 0
    dia = input('''Ingrese el día del que quiere generar el reporte: 
Ingrese 'semana' si desea generar el reporte de la semana entera.
''')
    dias = ['lunes', 'martes', 'miercoles',
            'jueves', 'viernes', 'sabado', 'domingo']
    if dia in dias:
        for i in estudiantes:
            if i['autenticacion']['usuario'] == usuario:
                print(dia, ': ')
                for l in i['reporte'][dia]:
                    if l[1] == 'ocio':
                        print(bcolors.green + 'Actividad: ' +
                              str(l[0]) + bcolors.reset)
                        print(bcolors.green + 'Tipo: ' +
                              str(l[1]) + bcolors.reset)
                        print(bcolors.green + 'Horas de dedicacion: ' +
                              str(l[2]) + bcolors.reset)
                        porcentaje = l[2] * 100 // 18
                        print(bcolors.green + 'Porcentaje que ocupa en el día: ' +
                              str(porcentaje) + '%' + bcolors.reset)
                        print('')
                    elif l[1] == 'curso':
                        print(bcolors.red + 'Actividad: ' +
                              str(l[0]) + bcolors.reset)
                        print(bcolors.red + 'Tipo: ' +
                              str(l[1]) + bcolors.reset)
                        print(bcolors.red + 'Horas de dedicacion: ' +
                              str(l[2]) + bcolors.reset)
                        porcentaje = l[2] * 100 // 18
                        print(bcolors.red + 'Porcentaje que ocupa en el día: ' +
                              str(porcentaje) + '%' + bcolors.reset)
                        print(bcolors.red + 'Carrera asociada: ' +
                              str(l[3]) + bcolors.reset)
                        print('')
                    elif l[1] == 'Actividad extracurricular':
                        print(bcolors.yellow + 'Actividad: ' +
                              str(l[0]) + bcolors.reset)
                        print(bcolors.yellow + 'Tipo: ' +
                              str(l[1]) + bcolors.reset)
                        print(bcolors.yellow + 'Horas de dedicacion: ' +
                              str(l[2]) + bcolors.reset)
                        porcentaje = l[2] * 100 // 18
                        print(bcolors.yellow + 'Porcentaje que ocupa en el día: ' +
                              str(porcentaje) + '%' + bcolors.reset)
                        print(bcolors.yellow + 'Curso asociado: ' +
                              str(l[3]) + bcolors.reset)
                        print('')
        horas_dia = horas_horario(usuario, estudiantes, dia)
        horas_d = 18-horas_dia
        print('La cantidad de horas ocupadas este dia es de: ', horas_dia)
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
                            print(bcolors.green + 'Actividad: ' +
                                  str(l[0]) + bcolors.reset)
                            print(bcolors.green + 'Tipo: ' +
                                  str(l[1]) + bcolors.reset)
                            print(bcolors.green + 'Horas de dedicacion: ' +
                                  str(l[2]) + bcolors.reset)
                            porcentaje = l[2] * 100 // 126
                            print(bcolors.green + 'Porcentaje que ocupa en la semana: ' +
                                  str(porcentaje) + '%' + bcolors.reset)
                            print('')
                        elif l[1] == 'curso':
                            print(bcolors.red + 'Actividad: ' +
                                  str(l[0]) + bcolors.reset)
                            print(bcolors.red + 'Tipo: ' +
                                  str(l[1]) + bcolors.reset)
                            print(bcolors.red + 'Horas de dedicacion: ' +
                                  str(l[2]) + bcolors.reset)
                            porcentaje = l[2] * 100 // 126
                            print(bcolors.red + 'Porcentaje que ocupa en la semana: ' +
                                  str(porcentaje) + '%' + bcolors.reset)
                            print(bcolors.red + 'Carrera asociada: ' +
                                  str(l[3]) + bcolors.reset)
                            print('')
                        elif l[1] == 'Actividad extracurricular':
                            print(bcolors.yellow + 'Actividad: ' +
                                  str(l[0]) + bcolors.reset)
                            print(bcolors.yellow + 'Tipo: ' +
                                  str(l[1]) + bcolors.reset)
                            print(bcolors.yellow + 'Horas de dedicacion: ' +
                                  str(l[2]) + bcolors.reset)
                            porcentaje = l[2] * 100 // 126
                            print(bcolors.yellow + 'Porcentaje que ocupa en la semana: ' +
                                  str(porcentaje) + '%' + bcolors.reset)
                            print(bcolors.yellow + 'Curso asociado: ' +
                                  str(l[3]) + bcolors.reset)
                            print('')
                        print('')

        horas_semana = horas_horario(usuario, estudiantes, dia)
        horas_libres = 126 - horas_semana
        print('La cantidad de horas ocupadas de esta semana es de: ',
              horas_semana, ' horas')
        print('Tiene ', horas_libres, 'horas disponibles esta semana')
        return estudiantes
    else:
        print('El dato ingresado no es valido')
        

def registro_actividades(usuario, carreras, cursos, estudiantes):
    '''
        Funcion que registra actividades ya sea que esten asociadas a un curso o no. Esta funcion realiza gran cantidad de comprobaciones para evitar errores, por ejemplo, la actividad tiene que matricularse dentro de las horas disponibles (7-18)'''
    insertar = False
    dias = ['lunes','martes','miercoles','jueves','viernes','sabado','domingo']
    codigo_curso = int
    for i in estudiantes:
        if i['autenticacion']['usuario'] == usuario:
            relacion_curso = input(
                "Está su actividad relacionada con un curso? ")
            if relacion_curso == 'si' or relacion_curso == 'Si':
                r_curso = input(
                    "A que curso está relacionada esta actividad? ")
                comp = verificar_curso(
                    usuario, carreras, cursos, estudiantes, r_curso)
                for z in cursos:
                    if z['curso'] == r_curso:
                        codigo_curso = z['codigo']
                if codigo_curso in i['estudios']['aprobados']:
                    print(
                        "Usted no puede matricular esta actividad porque el curso se encuentra aprobado")
                    break
                if codigo_curso in i['estudios']['reprobados']:
                    print(
                        "Usted no puede matricular esta actividad porque el curso se encuentra reprobado")
                    break
                if comp == True:
                    actividad = input("Cuál es el nombre de la actividad? ")
                    dia = input(
                        "Ingrese el día que va a realizar la actividad:")
                    if dia not in dias:
                        print('Ese dia no existe, recuerde que los dias deben ser escritos con minuscula')
                        break
                    hora_i = int(
                        input("Ingrese la hora de inicio de la actividad: "))
                    if hora_i < 7 or hora_i > 24:
                        print('Hora no valida, recuerde que el horario disponible es de las 9 a las 24 horas')
                        break
                    hora_f = int(
                        input("Ingrese la hora final de la actividad: "))
                    if hora_i < 7 or hora_i > 24:
                        print('Hora no valida, recuerde que el horario disponible es de las 9 a las 24 horas')
                        break
                    if hora_i > hora_f:
                        print('Esta operacion no es posible, la actividad esta empezando antes de que termine')
                        break
                    horas_i1 = hora_i
                    horas_i2 = hora_i
                    horas_t = hora_f - hora_i
                    horas_dia = horas_horario(usuario, estudiantes, dia)
                    horas_semana = horas_horario(
                        usuario, estudiantes, 'semana')
                    if horas_t + (horas_dia-1) > 12:
                        print("Está excediendo las 12 horas diarias")
                        break
                    if horas_t + horas_semana > 72:
                        print("Está excediendo las 72 horas semanales")
                        break
                    for z in range(horas_t):
                        if i['horario'][dia][horas_i2] == []:
                            insertar = True
                            horas_i2 = horas_i2 + 1
                        elif i['horario'][dia][horas_i2] != []:
                            print("Estas horas se presentan ocupadas")
                            insertar = False
                            break
                    if insertar == True:
                        i['reporte'][dia].append([actividad, 'Actividad extracurricular', horas_t, r_curso])
                        for p in range(horas_t):
                            i['horario'][dia][horas_i1] = actividad
                            horas_i1 = horas_i1 + 1
                if comp == False:
                    print("Usted no está matriculado en este curso")
                    home()
            elif relacion_curso == 'no' or relacion_curso == 'No':
                tipo = 'ocio'
                actividad = input('Ingrese el nombre de la actividad: ')
                dia = input("Ingrese el día que va a realizar la actividad:")
                if dia not in dias:
                    print('Ese dia no existe, recuerde que los dias deben ser escritos con minuscula')
                    break                
                hora_i = int(
                    input("Ingrese la hora de inicio de la actividad: "))
                if hora_i < 7 or hora_i > 24:
                    print('Hora no valida, recuerde que el horario disponible es de las 9 a las 24 horas')
                    break
                hora_f = int(
                    input("Ingrese la hora final de la actividad: "))
                horas_i1 = hora_i
                horas_i2 = hora_i
                if hora_i < 7 or hora_i > 24:
                    print('Hora no valida, recuerde que el horario disponible es de las 9 a las 24 horas')
                if hora_i > hora_f:
                    print('Esta operacion no es posible, la actividad esta empezando antes de que termine')
                    break
                fecha_i = str(input('Ingrese la fecha de inicio: '))
                fecha_f = str(input('Ingrese la fecha de final: '))
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
                    if i['horario'][dia][horas_i2] == []:
                        insertar = True
                        horas_i2 = horas_i2 + 1
                    elif i['horario'][dia][horas_i2] != []:
                        print("Estas horas se presentan ocupadas")
                        insertar = False
                        break
                if insertar == True:
                    i['reporte'][dia].append([actividad, tipo, horas_t])
                    for p in range(horas_t):
                        i['horario'][dia][horas_i1] = actividad
                        horas_i1 = horas_i1 + 1
            else:
                print("Esa opcion no es válida")
                home()
    return estudiantes


def aprobado_noAprobado(usuario, estudiantes, cursos):
    """
        La función permite al estudiante cambiar el estado de un curso (cursnado, aprobado o reprobado). Primero verificamos la carrera que está cursando el estudiante, esto lo hacemos buscando por medio del usuario en la base de datos de estudiantes. Una vez hayamos identificado, buscamos todas las carreras relacionadas a ese curso en las que el estudiante esté matriculado para imprimirlas en una lista junto con su clave unica.
        Se le pide al usuario estudiante que elija el curso al que desea cambiar su estado por medio de la clave unica. el sistema cambiará en el estado del curso dentro de la base de datos de estudiante y además eliminará dentro del horario del estudiante todas las clases de este curso para dejar espacio en casa de que quiera matricular otro.
        Todo esto se hizo recorriendo con ciclos las bases de datos y para llegar a la información necesaria, se utilizó los comprobantes if.
            
        Parametros:
        - usuario (str): es el usuario de la cuenta que ha iniciado sesión
        - estudiantes (list): es la base de datos en donde se almacenan las cuentas de los estudiantes
        - cursos (tuple): es la base de datos en donde se almacenan todos los cursos"""
    cursos_del_estudiante = []
    name_curso = ''
    for x in estudiantes:
        if x['autenticacion']['usuario'] == usuario:
            cursos_del_estudiante = x['estudios']['cursos']
    print("Los cursos en los que está matrículado son:")
    for cod in cursos_del_estudiante:
        for item in cursos:
            if item['codigo'] == cod:
                print("Cursos: {}, Curso: {}".format(
                    item['codigo'], item['curso']))
    curso_a_modificar = int(input("Escriba al que se le cambiará el estado: "))
    for item in cursos:
        if item['codigo'] == curso_a_modificar:
            name_curso = item['curso']
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
                for h in x['horario']:
                    for m in x['horario'][h]:
                        if name_curso in x['horario'][h][m]:
                            x['horario'][h][m].remove(name_curso)
                            print("El curso ha cambiado su estado a 'Aprobado'")
                    break
    elif estado == "R" or estado == "r":
        for x in estudiantes:
            if x['autenticacion']['usuario'] == usuario:
                x['estudios']['cursos'].remove(curso_a_modificar)
                x['estudios']['reprobados'].append(curso_a_modificar)
                print("Cursando: {}".format(x['estudios']['cursos']))
                print("Reprobados: {}".format(x['estudios']['reprobados']))
                for h in x['horario']:
                    for m in x['horario'][h]:
                        if name_curso in x['horario'][h][m]:
                            x['horario'][h][m].remove(name_curso)
                            print("El curso ha cambiado su estado a 'Reprobado'")
                    break

'''Funcion que recorre e imprime el horario del usuario dia por dia'''

def ver_horario(usuario, estudiantes):
    dias = ['lunes', 'martes', 'miercoles',
            'jueves', 'viernes', 'sabado', 'domingo']
    for x in estudiantes:
        if x['autenticacion']['usuario'] == usuario:
            for l in dias:
                print(l)
                print(x['horario'][l])
                print("")

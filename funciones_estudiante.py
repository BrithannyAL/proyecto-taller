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
                                                        hora_inicio = r_cursos['horario_de_clases'][1]
                                                        hora_final = r_cursos['horario_de_clases'][2]
                                                        cantidad_horas = hora_final - hora_inicio
                                                        if cantidad_horas == 0:
                                                            cantidad_horas = 1
                                                        for contador in range(cantidad_horas):
                                                            contador = 1
                                                            if i['horario'][dia][hora] == []:
                                                                i['horario'][dia][hora] = [curso_m]
                                                                hora = hora + contador
                                                                contador = + 1
                                                                i['estudios']['cursos'].append(
                                                                    {'curso': curso_m, 'estado': 'cursando'})
                                                            else:
                                                                print(
                                                                    "Usted tiene un choque de horarios")
                                                                flag = True
                                                                break
                                                        if flag == True:
                                                            break
                                                        print(
                                                            i['horario'][dia])
                                                        flag = True
                                                        break
                                else:
                                    print(
                                        "El curso ingresado no pertenece a la carrera matriculada")
                                    flag = True
                                    break
                else:
                    print("El curso ingresado no existe")


def ver_horario(usuario, carreras, cursos, estudiantes):

    for i in estudiantes:
        if i['autenticacion']['usuario'] == usuario:
            print('Lunes: ', i['horario']['lunes'])
            print('Martes: ', i['horario']['martes'])
            print('Miercoles: ', i['horario']['miercoles'])
            print('Jueves: ', i['horario']['jueves'])
            print('Viernes: ', i['horario']['viernes'])
            print('Sabado: ', i['horario']['sabado'])
            print('Domingo: ', i['horario']['viernes'])
            print("")


def registro_actividades():
    print("tbd")

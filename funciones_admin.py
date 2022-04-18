def agregar_curso():
    last_code = cursos[-1]['codigo']
    curso = input("Ingrese el nombre del curso que desea agregar: ")
    creditos = input("Ingrese la cantidad de creditos del curso: ")
    horas_l = input("Ingrese la cantidad de horas lectivas del curso: ")
    codigo   = last_code + 1
    nuevo_curso = {'curso' : curso, 'creditos' : creditos, 'horas_lectivas' : horas_l, 'codigo' : codigo}
    cursos.append(nuevo_curso)
    print("""
          El nuevo curso es:
          {}""".format(nuevo_curso))
    

def modificar_curso():
    imprimir(0)
    curso_a_modificar = int(input("Escriba el código del curso que desea modificar: "))
    nombre_curso = input("""
                         El título del curso es {}
                         ¿Desea modificar el nombre del curso? (y/n) """
                         .format(cursos[curso_a_modificar -1]['curso']))
    horas_lectivas = input("""
                           La cantidad de horas del curso es {}
                           ¿Desea modificar la cantidad de horas que imparte el curso? (y/n) """
                           .format(cursos[curso_a_modificar -1]['horas_lectivas']))
    if nombre_curso == "y":
        cursos[curso_a_modificar -1]['curso'] = input("Nuevo título para el curso: ")
    if horas_lectivas == "y":
        cursos[curso_a_modificar -1]['horas_lectivas'] = input("Nuevo horas lectivas para el curso: ")
    print("""El curso ha sido modificado: {}""".format(cursos[curso_a_modificar -1]))
    
def agregar_carrera(lista_carrera, cursos):
    salir = False
    carrera_cursos = []
    codigo = (lista_carrera[-1]['codigo']) + 1
    carrera_name = input("Ingrese el nombre de la carrera que desea agregar: ")
    carrera_semestres = input("Ingrese la cantidad de semestres de la carrera: ")
    imprimir(0, cursos)
    print("Presione x cuando haya terminado de agregar cursos.")
    while salir == False:
        carrera_cursos.append(input("Ingrese los códigos de los cursos de dicha carrera: "))
        for i in carrera_cursos:
            if i == "x":
                del carrera_cursos[-1]  
                salir = True
    nueva_carrera = {'carrera' : carrera_name, 'semestres' : carrera_semestres, 'cursos' : carrera_cursos, 'codigo': codigo}
    lista_carrera.append(nueva_carrera)
    print(nueva_carrera)
    return tuple(lista_carrera)
    

def modificar_carrera():
    imprimir(1)
    carrera_a_modificar = int(input("Escriba el código del curso que desea modificar: "))
    name_carrera = input("""
                         El título de la carrera es {}
                         ¿Desea modificar el nombre de la carrera? (y/n) """
                         .format(carreras[carrera_a_modificar - 1]['carrera']))
    seme_carrera = input("""
                         La cantidad de semestres en la carrera son {}
                         ¿Desea modificar la cantidad de semestres de la carrera? (y/n) """
                         .format(carreras[carrera_a_modificar]['semestres']))
    imprimir_codigos_cursos_en_carreras(carrera_a_modificar)
    curs_carrera = input("¿Desea modificar los cursos dentro de la carrera? (y/n) ")
    if name_carrera == "y":
        carreras[carrera_a_modificar - 1]['carrera'] = input("Escriba el nuevo nombre de la carrera: ")
    if seme_carrera == "y":
        carreras[carrera_a_modificar - 1]['semestres'] = input("Escriba la cantidad de semestres de la carrera: ")
    if curs_carrera == "y":
        imprimir(0)
        nuevos_cursos = modificar_codigos_en_carreras()
        carreras[carrera_a_modificar - 1]['cursos'] = nuevos_cursos
    print(carreras)
    
def imprimir_codigos_cursos_en_carreras(codigo):
    carrera = int
    for item in carreras:
        if codigo == item['codigo']:
            carrera = item['carrera']
            break
    print("""
          Los cursos dentro de la carrera son:
          {}""".format(carreras[codigo - 1]['cursos']))
    
def modificar_codigos_en_carreras():
    nuevos_cursos = []
    salir = False
    print("Presione x cuando haya terminado de agregar cursos.")
    while salir == False:
        nuevos_cursos.append(input("Escriba los códigos de los cursos de la carrera: "))
        for item in nuevos_cursos:
            if item == "x":
                del nuevos_cursos[-1]
                salir = True
    return nuevos_cursos

def imprimir(num, lista):
    if num == 0:
        print("***** Lista de cursos *****")
        for item in lista:
            print("Código {}: {}".format(item['codigo'], item['curso']))
    elif num == 1:
        print("***** Lista de carreras *****")
        for item in lista:
            print("Código {}: {}".format(item['codigo'], item['carrera']))
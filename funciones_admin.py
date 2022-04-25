def agregar_curso(lista_cursos):
    """
        Esta función le permite hacer a los administradoresnagregar nuevos cursos en la base de datos
        de el software. Le pide al admin el nombre del curso, la cantidad de créditos y las horas de las clases.
        Esos datos se acomodan en un obejto y se le agrega una clave unica llamada código, que en la base datos
        se gerera de de uno en uno, así que al código anterior le sumamos 1. Cuando ya hemos generado el nuevo 
        objeto, este lo insertamos dentro de la base de datos de cursos para ser retronada y ser convertida a tupla
        para protejer sus datos.
        
        Los parametros de la función son:
        lista_cursos = list: Esta es la base de datos que contiene los cursos con todas las caracteristicas de los
        mismos.
        estudiante ="""
    print(estudiantes[2])
    last_code = lista_cursos[-1]['codigo']
    curso = input("Ingrese el nombre del curso que desea agregar: ")
    creditos = input("Ingrese la cantidad de creditos del curso: ")
    horas_l = input("Ingrese la cantidad de horas lectivas del curso: ")
    codigo   = last_code + 1
    nuevo_curso = {'curso' : curso, 'creditos' : creditos, 'horas_lectivas' : horas_l, 'codigo' : codigo}
    lista_cursos.append(nuevo_curso)
    print("""
          El nuevo curso es:
          {}""".format(nuevo_curso))
    return tuple(lista_cursos)
    
def modificar_curso(lista_cursos):
    """
        Esta función le permite a los administradores modificar las caracteriticas de un curso ya existente en la 
        base de datos. Para eso lo primero que hacemos es imprimir la lista de cursos para que el admin pueda
        leerlos y escoger por medio de la clave única (código) el curso que modificará. Una vez haya escogido el
        curso, se le pregunta se desea cambiar el nombre del curso y/o la cantidad de horas de las clases.
        A partir de estas respuestas, se le presentarán al admin espacios para que pueda escribir el nuevo nombre
        del curso y la nueva cantidad de horas de clases.
        Estás respuestas se recolectan y reasignan sobre los campos en donde se almacenaba la vieja información.
        Luego la información es retornada como una tupla.
        
        Los parametros de esta función son:
        lista_cursos = list: Es la base de datos en forma de lista que contiene los cursos con toda su información"""
    imprimir(0, lista_cursos)
    curso_a_modificar = int(input("Escriba el código del curso que desea modificar: "))
    nombre_curso = input("""
                         El título del curso es {}
                         ¿Desea modificar el nombre del curso? (y/n) """
                         .format(lista_cursos[curso_a_modificar -1]['curso']))
    horas_lectivas = input("""
                           La cantidad de horas del curso es {}
                           ¿Desea modificar la cantidad de horas que imparte el curso? (y/n) """
                           .format(lista_cursos[curso_a_modificar -1]['horas_lectivas']))
    if nombre_curso == "y":
        lista_cursos[curso_a_modificar -1]['curso'] = input("Nuevo título para el curso: ")
    if horas_lectivas == "y":
        lista_cursos[curso_a_modificar -1]['horas_lectivas'] = input("Nuevo horas lectivas para el curso: ")
    print("""El curso ha sido modificado: {}""".format(lista_cursos[curso_a_modificar -1]))
    return(tuple(lista_cursos))
    
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
    
def modificar_carrera(lista_carreras, cursos):
    imprimir(1, lista_carreras)
    
    carrera_a_modificar = int(input("Escriba el código del curso que desea modificar: "))
    name_carrera = input("""
                         El título de la carrera es {}
                         ¿Desea modificar el nombre de la carrera? (y/n) """
                         .format(lista_carreras[carrera_a_modificar - 1]['carrera']))
    seme_carrera = input("""
                         La cantidad de semestres en la carrera son {}
                         ¿Desea modificar la cantidad de semestres de la carrera? (y/n) """
                         .format(lista_carreras[carrera_a_modificar -1]['semestres']))
    imprimir_codigos_cursos_en_carreras(carrera_a_modificar, lista_carreras)
    curs_carrera = input("¿Desea modificar los cursos dentro de la carrera? (y/n) ")
    if name_carrera == "y":
        lista_carreras[carrera_a_modificar - 1]['carrera'] = input("Escriba el nuevo nombre de la carrera: ")
    if seme_carrera == "y":
        lista_carreras[carrera_a_modificar - 1]['semestres'] = input("Escriba la cantidad de semestres de la carrera: ")
    if curs_carrera == "y":
        imprimir(0, cursos)
        nuevos_cursos = modificar_codigos_en_carreras()
        lista_carreras[carrera_a_modificar - 1]['cursos'] = nuevos_cursos
    print(lista_carreras)
    return tuple(lista_carreras)
    
def imprimir_codigos_cursos_en_carreras(codigo, lista):
    carrera = int
    for item in lista:
        if codigo == item['codigo']:
            carrera = item['carrera']
            break
    print("""
          Los cursos dentro de la carrera son:
          {}""".format(lista[codigo - 1]['cursos']))
    
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
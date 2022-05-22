from email.mime import base
from pickle import TRUE
from turtle import home
from base_de_datos import estudiante
from funciones import horas_horario, verificar_curso
from tkinter import E, messagebox
from cargar_en_archivos import cargar_archivos_estudiantes




def matricular_carrera(carrera, usuario , carreras):
    if usuario.carreras != []:
        messagebox.showerror(message='Solo puede matricular una carrera')
        return 0
    codigo = 0
    l = carreras()
    if l != False:
        while l.sig != None:
            if l.carrera == carrera:
                codigo = l.codigo
            l = l.sig
        if l.sig == None:
            if l.carrera == carrera:
                codigo = l.codigo
        if codigo == 0:
            messagebox.showerror(message='Elija una carrera') 
        elif codigo in usuario.carreras:
            messagebox.showerror(message='Ya ha matriculado esta carrera')
        else:
            usuario.carreras.append(codigo)
            while usuario.ant != None:
                usuario = usuario.ant
            usuario.guardar_en_archivos()


            messagebox.showinfo(message='Carrera matriculada exitosamente')
            print(usuario.carreras)
    return ([usuario])


def matricular_curso(curso, usuario, cursos, carreras):
    '''Esta funcion matricula un curso y tiene muchas comprobaciones dentro de ella para evitar errores, algunas de estas son; el evitar que se matricule un curso sin matricular una carrera antes o matricular un curso de una carrera que el usuario no ha matriculado '''
    codigos = []
    codigo = 0
    l = cursos()
    c = carreras()
    
    cursos_carrera = []
    while c.sig != None:
        if [c.codigo] == usuario.carreras:
            cursos_carrera = c.cursos
        c = c.sig 
        if c.sig == None:
            if [c.codigo] == usuario.carreras:
                cursos_carrera = c.cursos

    if l != False:

        while l.sig != None:
            if l.curso == curso:
                codigo = l.codigo
                codigos.append(l.codigo)
            l = l.sig
        if l.sig == None:
            if l.curso == curso:
                codigo = l.codigo
                codigos.append(l.codigo)
        
        carrera = usuario.carreras
        if carrera == []:
            messagebox.showerror(message='Primero matricule una carrera')
        elif codigo in usuario.cursos:
            messagebox.showerror(message='Ya ha matriculado este curso')
        elif codigo in usuario.aprobados or codigo in usuario.reprobados:
            messagebox.showerror(message='Este curso se encuentra aprobado o reprobado')
        elif codigo not in cursos_carrera:
            messagebox.showerror(message='Este curso no pertenece a su carrera')
        elif insertar_en_horario(curso, usuario, cursos)[0] == False:
            error = insertar_en_horario(curso, usuario, cursos)[1]
            if error[1] == 'choque':
                messagebox.showerror(message='Usted presenta un choque de horarios')
            elif error[1] == 'horas': 
                messagebox.showerror(message='Está excediendo las horas diarias o semanales')
            elif error[1] == 'no':
                messagebox.showerror(message='Este curso no existe')
        else:
            insertar_en_horario(curso, usuario, cursos)
            usuario.cursos.append(codigo)
            while usuario.ant != None:
                usuario = usuario.ant
            usuario.guardar_en_archivos()
            messagebox.showinfo(message='Curso matriculado exitosamente')
    else: messagebox.showerror(message='El curso que intenta matricular no existe') 
                         


def ingresar_actividad(usuario,estudiantes,actividad,dia,hora_i,hora_f,radioValue,curso_r):
    if actividad == '' or dia == '' or hora_i == '' or hora_f == '':
        messagebox.showerror(message='Por favor rellene todos los campos')
    elif radioValue == 1:
        if curso_r == '':
            messagebox.showerror(message='Por favor rellene todos los campos')
        elif hora_i < hora_f:
            messagebox.showerror(message='La hora final es mayor a la hora de inicio')
        else:
            usuario.actividades[dia].append(['Actividad:', actividad, 'dia:', dia, 'Hora de inicio:', hora_i, 'Hora final:',hora_f, 'Curso relacionado', curso_r])
            print(usuario.actividades)
            usuario.guardar_en_archivos()
            messagebox.showinfo(message='Actividad agregada exitosamente')
    elif radioValue == 2:
        if hora_i < hora_f:
            messagebox.showerror(message='La hora final es mayor a la hora de inicio')
        else:
            usuario.actividades[dia].append(['Actividad:', actividad, 'dia:', dia, 'Hora de inicio:', hora_i, 'Hora final:',hora_f])
            print(usuario.actividades)
            while usuario.ant != None:
                usuario = usuario.ant
            usuario.guardar_en_archivos()
            messagebox.showinfo(message='Actividad agregada exitosamente')





def insertar_en_horario(curso_o_actividad, estudiante, curso_base):
    c = curso_base()
    while c.sig != None:

        if c.curso == curso_o_actividad:
            curso = c
        c = c.sig 
        if c.sig == None:
            if c.curso == curso_o_actividad:
                curso = c  
    horas_d = 0
    horas_s = 0     
    horario = curso.horario_de_clases
    dia = horario[0]
    hora_i = horario[1]
    hora_f = horario[2]

#Obtiene las horas semanales
    for i in estudiante.horario:
        h = 7
        while h <= 24:
            if estudiante.horario[i][h] != []:
                horas_s = horas_s + 1
            h = h+1  
    
#Obtiene las horas diarias    
        h = 7
        while h <= 24:
            if estudiante.horario[dia][h] != []:
                horas_d = horas_d + 1
            h = h+1  

    for x in range(hora_f-hora_i):
        if estudiante.horario[dia][hora_i] != []:
            return [False,'choque']
        elif horas_d + (hora_f-hora_i) > 12 or horas_s + (hora_f-hora_i) > 72:
            return[False,'horas']
    else:
        for x in range(hora_f-hora_i):
            estudiante.horario[dia][hora_i] = curso_o_actividad
            hora_i = hora_i + 1
            return [True,'a']


def ver_horario(usuario, base_de_datos):
    horario = []
    dias = ['lunes', 'martes', 'miercoles', 'jueves', 'viernes', 'sabado', 'domingo']
    estudiante =  base_de_datos.estudiante.buscar(base_de_datos.estudiantes,usuario)
    for x in dias:
        horario.append([x, ': ', estudiante[8][x]])
    messagebox.showinfo(message=horario)
    return horario





























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




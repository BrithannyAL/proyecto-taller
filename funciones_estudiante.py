from email.mime import base
from pickle import TRUE
from turtle import home
from base_de_datos import estudiante
from funciones import horas_horario, verificar_curso
from tkinter import E, messagebox
from cargar_en_archivos import cargar_archivos_cursos, cargar_archivos_estudiantes




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
        elif int(hora_i) > int(hora_f):
            print(hora_i)
            print(hora_f)
            messagebox.showerror(message='La hora de inicio es mayor a la hora final')
        else:
            usuario.actividades[dia].append(['Actividad:', actividad, 'dia:', dia, 'Hora de inicio:', hora_i, 'Hora final:',hora_f, 'Curso relacionado', curso_r])
            print(usuario.actividades)
            usuario.guardar_en_archivos()
            messagebox.showinfo(message='Actividad agregada exitosamente')
    elif radioValue == 2:
        if int(hora_i) > int(hora_f):
            print(hora_i)
            print(hora_f)
            messagebox.showerror(message='La hora de inicio es mayor a la hora final')
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



def aprobar(u,curso_aprobado):
    cursos_en_curso = u.cursos
    cursos = cargar_archivos_cursos()
    puntero = cursos
    if curso_aprobado == '':
        messagebox.showerror(message='Por favor seleccione un curso')
    else:
        while puntero.sig != None:
            if curso_aprobado == puntero.curso:
                codigo = puntero.codigo
            puntero = puntero.sig
        if puntero.sig == None:
            if curso_aprobado == puntero.curso:
                codigo = puntero.codigo
        for i in cursos_en_curso:
            if i == codigo:
                print(cursos_en_curso)
                cursos_en_curso.remove(i)
                print(cursos_en_curso)
                u.aprobados.append(codigo)
                print(u.cursos)
                print(u.aprobados)
                while usuario.ant != None:
                    usuario = usuario.ant
                usuario.guardar_en_archivos()                
                messagebox.showinfo(message='Curso aprobado')
 

def reprobar(u,curso_reprobado):
    cursos_en_curso = u.cursos
    cursos = cargar_archivos_cursos()
    puntero = cursos
    if curso_reprobado == '':
        messagebox.showerror(message='Por favor seleccione un curso')
    else:
        while puntero.sig != None:
            if curso_reprobado == puntero.curso:
                codigo = puntero.codigo
            puntero = puntero.sig
        if puntero.sig == None:
            if curso_reprobado == puntero.curso:
                codigo = puntero.codigo
        for i in cursos_en_curso:
            if i == codigo:
                print(cursos_en_curso)
                cursos_en_curso.remove(i)
                print(cursos_en_curso)
                u.reprobados.append(codigo)
                print(u.cursos)
                print(u.reprobados)
                while usuario.ant != None:
                    usuario = usuario.ant
                usuario.guardar_en_archivos()
                messagebox.showinfo(message='Curso reprobado')
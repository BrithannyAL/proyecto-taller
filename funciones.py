#Se importan las librerías necesarias
import getpass
import time
from cargar_en_archivos import cargar_archivos_cursos, cargar_archivos_carreras

def horas_horario(usuario, estudiantes, dia):
    """
       Esta función le permite saber al usuario cuantas horas tiene libres durante la semana"""
    contador = 0
    semana = 0
    if dia == 'semana':
        for i in estudiantes:
            llaves = list(i['horario'].keys())
            if i['autenticacion']['usuario'] == usuario:
                    for a in llaves:
                        contador = 0
                        llaves_dia = list(i['horario'][a].keys())
                        for d in llaves_dia:
                            for c in i['horario'][a][d]:
                                if c != []:
                                    pass
                                contador += 1
                        semana = semana + contador
        return semana
    else:
        for i in estudiantes:
            if i['autenticacion']['usuario'] == usuario:
                contador = 0
                llaves_dia = list(i['horario'][dia].keys())
                for z in llaves_dia:
                    if i['horario'][dia][z] != []:
                        contador += 1
        #print('La cantidad de horas del ', dia, ' es: ', contador)
        return contador

def verificar_curso(usuario, carreras, cursos, estudiantes, r_curso):
    """
        Esta función nos permite saber si un curso está dentro de la lista de cursos en las que el estudiante está matriculado. Todas las verificaciones para obtener la información se hacen con condicionales y los ciclos for se usan para recorrer las listas."""
    for i in estudiantes:
        if i['autenticacion']['usuario'] == usuario:
            for z in cursos:
                if z['curso'] == r_curso:
                    codigo = z['codigo'] 
                    for x in i['estudios']['cursos']:
                        if x == codigo:
                            return True
                    else:
                        return False
            else: print("Este curso no existe")
            
def lista_cursos():
    lista = cargar_archivos_cursos()
    lista_nombres = []
    
    while lista.sig != None:
        lista_nombres.append(lista.curso)
        lista = lista.sig
    
    return lista_nombres

def lista_cursos_codigo():
    lista = cargar_archivos_cursos()
    lista_nombres = []
    
    while lista.sig != None:
        lista_nombres.append('{}, {}'.format(lista.codigo, lista.curso))
        lista = lista.sig
    
    return lista_nombres

def lista_carreras():
    lista = cargar_archivos_carreras()
    lista_nombres = []
    
    while lista.sig != None:
        lista_nombres.append(lista.carrera)
        lista = lista.sig
    
    return lista_nombres
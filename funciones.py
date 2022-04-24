import hashlib
import getpass
import time

def cifrar (entrada):
    entrada_c=entrada.encode('ascii')
    resultado = hashlib.md5(entrada_c)
    return (resultado.hexdigest())
    
def obtener_calve(mensaje):
    pswd = getpass.getpass(mensaje+": ")
    return (pswd)

def calcular_horas(cursos):
    for i in cursos:
        horas = cursos['creditos']
        horas_lectivas = cursos['horas_lectivas']
        horas = horas * 3
        horas = horas - horas_lectivas

def horas_horario(usuario, estudiantes, dia):
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

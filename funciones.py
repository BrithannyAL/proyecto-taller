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

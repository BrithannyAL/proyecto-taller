import hashlib
import getpass
import time
from base_de_datos import cursos

def cifrar (entrada):
    entrada_c=entrada.encode('ascii')
    resultado = hashlib.md5(entrada_c)
    return (resultado.hexdigest())

def obtener_calve(mensaje):
    pswd = getpass.getpass(mensaje+": ")
    return (pswd)

def calcular_horas():
    for i in cursos:
        horas = cursos['creditos']
        horas_lectivas = cursos['horas_lectivas']
        horas = horas * 3
        horas = horas - horas_lectivas

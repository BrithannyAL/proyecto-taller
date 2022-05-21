from base_de_datos import admin, estudiante
from tkinter.messagebox import askyesno  


def cargar_archivos_admins():
    global admin
    respuesta = None
    try:
        with open("admins.dat", "tr") as lector:
            lectura = eval(lector.readline()[:-1])
            if lectura != '':
                respuesta = admin(lectura[0], lectura[1], lectura[2], lectura[3], lectura[4])
            lectura = eval(lector.readline()[:-1])    
            while (lectura != ''):
                respuesta.insertar(admin(lectura[0], lectura[1], lectura[2], lectura[3], lectura[4]))
                lectura = eval(lector.readline()[:-1])      
    except FileNotFoundError as error:
        respuesta = askyesno(title="Error", message="No se encontró el archivo de datos ¿Desea crear un nuevo archivo de registros?")
        if respuesta:
            open("admins.dat", "tw").close()
    finally:
        return respuesta
    
def cargar_archivos_estudiantes():
    global estudiante
    respuesta = None
    try:
        with open("estudiantes.dat", "tr") as lector:
            lectura = eval(lector.readline()[:-1])
            if lectura != '':
                respuesta = estudiante(lectura[0], lectura[1], lectura[2], lectura[3], lectura[4], lectura[5], lectura[6],lectura[7], lectura[8], lectura[9])
            lectura = eval(lector.readline()[:-1])    
            while (lectura != ''):
                respuesta.insertar(estudiante(lectura[0], lectura[1], lectura[2], lectura[3], lectura[4], lectura[5], lectura[6], lectura[7], lectura[8], lectura[9]))
                lectura = eval(lector.readline()[:-1])      
    except FileNotFoundError as error:
        respuesta = askyesno(title="Error", message="No se encontró el archivo de datos ¿Desea crear un nuevo archivo de registros?")
        if respuesta:
            open("estudiantes.dat", "tw").close()
    finally:
        return respuesta
    
def cargar_archivos_cursos():
    respuesta = None
    try:
        with open("cursos.dat", "tr") as lector:
            lectura = eval(lector.readline()[:-1])
            if lectura != '':
                respuesta = estudiante(lectura[0], lectura[1], lectura[2], lectura[3], lectura[4])
            lectura = eval(lector.readline()[:-1])    
            while (lectura != ''):
                respuesta.insertar(estudiante(lectura[0], lectura[1], lectura[2], lectura[3], lectura[4]))
                lectura = eval(lector.readline()[:-1])      
    except FileNotFoundError as error:
        respuesta = askyesno(title="Error", message="No se encontró el archivo de datos ¿Desea crear un nuevo archivo de registros?")
        if respuesta:
            open("cursos.dat", "tw").close()
    finally:
        return respuesta
    
def cargar_archivos_carreras():
    respuesta = None
    try:
        with open("carreras.dat", "tr") as lector:
            lectura = eval(lector.readline()[:-1])
            if lectura != '':
                respuesta = estudiante(lectura[0], lectura[1], lectura[2], lectura[3])
            lectura = eval(lector.readline()[:-1])    
            while (lectura != ''):
                respuesta.insertar(estudiante(lectura[0], lectura[1], lectura[2], lectura[3]))
                lectura = eval(lector.readline()[:-1])      
    except FileNotFoundError as error:
        respuesta = askyesno(title="Error", message="No se encontró el archivo de datos ¿Desea crear un nuevo archivo de registros?")
        if respuesta:
            open("carreras.dat", "tw").close()
    finally:
        return respuesta
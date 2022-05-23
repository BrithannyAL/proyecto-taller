from base_de_datos import cursos, carreras
from cargar_en_archivos import cargar_archivos_cursos, cargar_archivos_carreras
from tkinter import E, messagebox

def agregar_curso(vname, vcredit, vday, vhi, vhf):
    """
        Esta función le permite hacer a los administradoresnagregar nuevos cursos en la base de datos de el software. Le pide al admin el nombre del curso, la cantidad de créditos y las horas de las clases. Esos datos se acomodan en un obejto y se le agrega una clave unica llamada código, que en la base datos se gerera de de uno en uno, así que al código anterior le sumamos 1. Cuando ya hemos generado el nuevo  objeto, este lo insertamos dentro de la base de datos de cursos para ser retronada y ser convertida a tupla para protejer sus datos.

        Parámetros:
        - lista_cursos (list): Esta es la base de datos que contiene los cursos con todas las caracteristicas de los
        mismos."""
    try:    
        horario_lectivo = [vday, int(vhi), int(vhf)]
        horas_lectivas = int(vhf) - int(vhi)
        lista_cursos = cargar_archivos_cursos()
        codigo = 0
        
        while lista_cursos.sig != None:
            lista_cursos = lista_cursos.sig
        codigo = lista_cursos.codigo + 1
        while lista_cursos.ant != None:
            lista_cursos = lista_cursos.ant
            
        if horas_lectivas > int(vcredit):
            messagebox.showerror(title='Error en los datos', message='El curso vale {} creditos, no puede matricular más de {} horas'.format(vcredit, vcredit))
        else:        
            new = cursos(vname, vcredit, horas_lectivas, horario_lectivo, codigo)
            lista_cursos.insertar(new)
            lista_cursos.guardar_en_archivos()
            
    except ValueError:
        messagebox.showerror(title='Error en los datos', message='Las horas y los créditos deben ser números')
        
def mostrar_cursos(vcurso):
    lista_cursos = cargar_archivos_cursos()
    
    while lista_cursos != None and lista_cursos.curso == vcurso:
        lista_cursos = lista_cursos.sig
    
    return[lista_cursos.curso, lista_cursos.creditos, lista_cursos.horario_de_clases[0], lista_cursos.horario_de_clases[1], lista_cursos.horario_de_clases[2]]
        
    
        


def modificar_curso(original, vname, vcredit, vday, vhi, vhf):
    """
        Esta función le permite a los administradores modificar las caracteriticas de un curso ya existente en la  base de datos. Para eso lo primero que hacemos es imprimir la lista de cursos para que el admin pueda leerlos y escoger por medio de la clave única (código) el curso que modificará. Una vez haya escogido el curso, se le pregunta se desea cambiar el nombre del curso y/o la cantidad de horas de las clases. A partir de estas respuestas, se le presentarán al admin espacios para que pueda escribir el nuevo nombre del curso y la nueva cantidad de horas de clases. Estás respuestas se recolectan y reasignan sobre los campos en donde se almacenaba la vieja información. Luego la información es retornada como una tupla.

        Parámetros:
        - lista_cursos (list): Es la base de datos en forma de lista que contiene los cursos con toda su información"""
    try: 
        lista = cargar_archivos_cursos()
        
        while lista.sig != None:
            if lista.curso == original:
                break
            lista = lista.sig
            
        lista.curso = vname
        lista.creditos = vcredit
        lista.horario_de_clases[0] = vday
        lista.horario_de_clases[1] = vhi
        lista.horario_de_clases[2] = vhf  
        
        while lista.ant != None:
            lista = lista.ant
            
        lista.guardar_en_archivos()
    except ValueError:
        messagebox.showerror(title='Error en los datos', message='Las horas y los créditos deben ser números')  


def agregar_carrera(vname, vsem, cursos):
    """
        Esta función le permite a los adminitradores agregar una nueva carrera en una base de datos. La función primero genera una clave unica para la nueva carrera (codigo). Se le pide al admin que ingrese el nombre y la cantidad de semestre de la carrera. El siguiente dato son los cursos que estarán relacionados en el plan de estudios de la carrera, por lo tanto, al admin, se le imprime una lista con los nombre de los cursos y sus respectivos códigos para que pueda agregarlos por medio de él. Esto último se hace con un ciclo while, de forma que el admin pueda ir agregando los codigos de los cursos que desee dentro de la carrera, y de forma ilimitada hasta que se le indique al app que ya ha acabado de agregar cursos (digitando una x). Luego tomamos todos los datos recolectados y los ordenamos dentro de un diccionario para que este pueda ser agregado a la base de datos de carreras y esta misma, pueda ser devuelta en forma de tupla.

        Parámetros:
        - lista_carrera (list): esta es la base de datos en forma de lista al que agregaremos la nueva carrera.
        -cursos (tuple): la utilizamos para imprimir los cursos que puede elegir el admin para relacionarla con la
        carrera."""
    try:
        lista = cargar_archivos_carreras()
        
        while lista.sig != None:
            lista = lista.sig
        codigo = int(lista.codigo) + 1
        
        cursos.split()
        
        new = carreras(vname, vsem, codigo, cursos)
        lista.insertar(new)
        
        while lista.ant != None:
            lista = lista.ant
        lista.guardar_en_archivos()
    except:
        messagebox.showerror(title='Error', message="Ha habido un error en el sistema")


def modificar_carrera(original, vname, vsem, cursos):
    """
        Esta es la función que le permite a los administradores modificar una carrera existente dentro de la base de datos. Lo primero es presentarle al usuario una lista de carreras con su respectivo codigo para que el admnistrador pueda escoger el curso a modificar por medio de ellos. Lo sieguiente es que se le pregunta al admin si desea modificar el nombre, la cantidad de semestres y los cursos relacionados a esta carrera. Una vez se hayan contestado las preguntas, a partir de esta, se le tomará la información seleccionada al administrador y guardarla en un diccionario que se agregará en la base de datos. Para la modificaicón de los cursos, se llama a una función que devuelve los cursos impresos que están relacionados con esa carrera, para que el admin decida si quiere hacer el cambio. En el caso de que diga que si, lo llevamos a una función específica para que escoja los cursos que sea modificar. Una vez toda la información esté recolectada y guardada en el diccionario, se inserta en la base de datos, para que esta sea retornada en forma de tupla.

        Parámetros:
        - lista_carrera (list): esta es la base de datos en forma de lista en la que garemos la modificación
        de la carrera.
        -cursos (tuple): la utilizamos para imprimir los cursos que puede elegir el admin para relacionarla con la
        carrera."""
    try: 
        lista = cargar_archivos_carreras()
        
        while lista.sig != None:
            if lista.carrera == original:
                break
            lista = lista.sig
            
        lista.carrera = vname
        lista.semestres = vsem
        lista.cursos = cursos.split()
        
        while lista.ant != None:
            lista = lista.ant
            
        lista.guardar_en_archivos()
    except:
       messagebox.showerror(title='Error', message="Ha habido un error en el sistema")
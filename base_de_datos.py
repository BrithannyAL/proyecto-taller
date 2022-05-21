import hashlib
from tkinter import messagebox
from tkinter.messagebox import askyesno

#VARIABLES GLOBALES
dic_horario = {
            'lunes':      {7: [], 8: [], 9: [], 10:[], 11:[], 12:[], 13:[], 14:[], 15:[], 16:[], 17:[], 18:[], 19:[], 20:[], 21:[], 22:[], 23:[], 24:[] },
            'martes':     {7: [], 8: [], 9: [], 10:[], 11:[], 12:[], 13:[], 14:[], 15:[], 16:[], 17:[], 18:[], 19:[], 20:[], 21:[], 22:[], 23:[], 24:[]},
            'miercoles':  {7: [], 8: [], 9: [], 10:[], 11:[], 12:[], 13:[], 14:[], 15:[], 16:[], 17:[], 18:[], 19:[], 20:[], 21:[], 22:[], 23:[], 24:[] },
            'jueves':     {7: [], 8: [], 9: [], 10:[], 11:[], 12:[], 13:[], 14:[], 15:[], 16:[], 17:[], 18:[], 19:[], 20:[], 21:[], 22:[], 23:[], 24:[]},
            'viernes':    {7: [], 8: [], 9: [], 10:[], 11:[], 12:[], 13:[], 14:[], 15:[], 16:[], 17:[], 18:[], 19:[], 20:[], 21:[], 22:[], 23:[], 24:[]},
            'sabado':     {7: [], 8: [], 9: [], 10:[], 11:[], 12:[], 13:[], 14:[], 15:[], 16:[], 17:[], 18:[], 19:[], 20:[], 21:[], 22:[], 23:[], 24:[]},
            'domingo':    {7: [], 8: [], 9: [], 10:[], 11:[], 12:[], 13:[], 14:[], 15:[], 16:[], 17:[], 18:[], 19:[], 20:[], 21:[], 22:[], 23:[], 24:[]},
            }

dic_reporte = {
            'lunes':      [],
            'martes':     [],
            'miercoles':  [],
            'jueves':     [],
            'viernes':    [],
            'sabado':     [],
            'domingo':    [],
            }

class carreras:
    carrera =  ''
    semestres =  None
    cursos =  []
    codigo =  None
    sig = None
    
    def __init__(self,ca,s,cu,co):
        self.carrera=ca
        self.semestres=s
        self.cursos=cu
        self.codigo=co

    def recorrer_lista(self) -> str:
        actual = self
        respuesta = []
        while actual.sig != None:
            respuesta.append([actual.carrera, actual.semestres, actual.cursos, actual.codigo])
            actual=actual.sig
        respuesta.append([actual.carrera, actual.semestres, actual.cursos, actual.codigo])
        return respuesta

    def nombre_carrera(self):
        actual = self
        respuesta = []
        while actual.sig != None:
            respuesta.append([actual.carrera])
            actual=actual.sig
        respuesta.append([actual.carrera])
        return respuesta

    def buscar(self,a):
        actual = self
        while actual.sig != None:
            if actual.carrera == a:
                return actual.carrera, actual.semestres, actual.cursos, actual.codigo
            else:
                actual = actual.sig
                if actual.carrera == a:
                    return actual.carrera, actual.semestres, actual.cursos, actual.codigo
        return False
    
    def insertar (self,rn):
        puntero=self
        while (puntero.sig!=None):
            puntero=puntero.sig
        puntero.sig=rn
        
    def guardar_en_archivos(self):
        puntero=self
        try:
            with open("carreras.dat", "tw") as archivo:
                archivo.writelines(
                    [puntero.carrera, puntero.semestres, puntero.cursos, puntero.codigo].__str__()+"\n")
                while puntero.sig != None:
                    puntero = puntero.sig
                    archivo.writelines(
                        [puntero.carrera, puntero.semestres, puntero.cursos, puntero.codigo].__str__()+"\n")
        except FileNotFoundError as error:
            messagebox.showerror(title="Error" ,message="Problemas al guardar la información en los archivos")
    
"""lista_carreras = carreras('Ingenieria en computacion', 8 , [1, 2, 3, 4, 5, 6, 7] , 1)
lista_carreras.insertar(lista_carreras, carreras('Ingenieria en agronomia', 8 ,[1, 2, 3, 8, 9, 10 ] , 2))
lista_carreras.insertar(lista_carreras, carreras('Administracion de empresas', 10 ,[1, 2, 3, 11, 12, 13 ] , 3))
lista_carreras.insertar(lista_carreras, carreras('Administracion en produccion industrial', 12 ,[1, 2, 3, 14, 15] , 4 ))
lista_carreras.insertar(lista_carreras, carreras('Ingenieria en electronica', 10 ,[1, 2, 3, 4, 16, 17] , 5 ))"""


class cursos:
    curso = ''
    creditos = None
    horas_lectivas = None
    horario_de_clases = []
    codigo = 1
    sig = None

    def __init__(self , cu , c, h_l , h_c , co ):
        self.curso=cu
        self.creditos= c
        self.horas_lectivas=h_l
        self.horario_de_clases=h_c
        self.codigo=co

    def recorrer_lista(self) -> str:
        actual = self
        respuesta = "["
        while actual.sig != None:
            respuesta+=f"'{actual.curso, actual.creditos, actual.horas_lectivas, actual.horario_de_clases, actual.codigo}',"
            actual=actual.sig
        respuesta+= f"'{actual.curso, actual.creditos, actual.horas_lectivas, actual.horario_de_clases, actual.codigo}']"
        return respuesta

    def nombre_curso(self):
        actual = self
        respuesta = []
        while actual.sig != None:
            respuesta.append([actual.curso])
            actual=actual.sig
        respuesta.append([actual.curso])
        return respuesta

    def buscar(self,a):
        actual = self
        while actual.sig != None:
            if actual.curso == a:
                return actual.curso, actual.creditos, actual.horas_lectivas, actual.horario_de_clases, actual.codigo
            else:
                actual = actual.sig
                if actual.curso == a:
                    return actual.curso, actual.creditos, actual.horas_lectivas, actual.horario_de_clases, actual.codigo
        return False
    
    def insertar (self,rn):
        puntero=self
        while (puntero.sig!=None):
            puntero=puntero.sig
        puntero.sig=rn
        
    def guardar_en_archivos(self):
        puntero=self
        try:
            with open("cursos.dat", "tw") as archivo:
                archivo.writelines(
                    [puntero.curso, puntero.creditos, puntero.horas_lectivas, puntero.horario_de_clases, puntero.codigo].__str__()+"\n")
                while puntero.sig != None:
                    puntero = puntero.sig
                    archivo.writelines(
                        [puntero.curso, puntero.creditos, puntero.horas_lectivas, puntero.horario_de_clases, puntero.codigo].__str__()+"\n")
        except FileNotFoundError as error:
            messagebox.showerror(title="Error" ,message="Problemas al guardar la información en los archivos")

"""lista_cursos = cursos('Matematica general' , 3 , 3,  ['lunes', 9, 12] , 1)
lista_cursos.insertar(lista_cursos,cursos('Comunicacion escrita' , 2 , 3 , ['martes', 9, 12] , 2))
lista_cursos.insertar(lista_cursos,cursos('Ingles 1' , 2 , 3 , ['miercoles', 9, 12] , 3))
lista_cursos.insertar(lista_cursos,cursos('Introduccion a la programacion' , 2 , 3 , ['martes', 7, 8] , 4))
lista_cursos.insertar(lista_cursos,cursos('Taller de programacion' , 3 , 3 , ['jueves', 9, 12] , 5))
lista_cursos.insertar(lista_cursos,cursos('Fundamentos de organizacion de computadoras' , 2 , 3 , ['viernes', 9, 12] , 6))
lista_cursos.insertar(lista_cursos,cursos('Marematica discreta' , 3 , 3 , ['lunes', 13, 14] , 7))
lista_cursos.insertar(lista_cursos,cursos('Introduccion a la agronomia' , 3 , 3 , ['lunnes', 13, 14] , 8))
lista_cursos.insertar(lista_cursos,cursos('Agromatica ' , 3 , 3 , ['miercoles', 14, 15] , 9))
lista_cursos.insertar(lista_cursos,cursos('Biologia general' , 3 , 3 , ['jueves', 16, 17] , 10))
lista_cursos.insertar(lista_cursos,cursos('Introducciona a la administracion de empresas' , 2 , 3 , ['viernes', 18, 19] , 11))
lista_cursos.insertar(lista_cursos,cursos('Computacion para administracion' , 2 , 3 , ['lunes', 18, 19] , 12))
lista_cursos.insertar(lista_cursos,cursos('Matematica para administracion' , 3 , 3 , ['martes', 14, 15] , 13))
lista_cursos.insertar(lista_cursos,cursos('Dibijo tecnico' , 2 , 3 , ['miercoles', 19, 19] , 14))
lista_cursos.insertar(lista_cursos,cursos('Quimica basica' , 2 , 3 , ['martes', 9, 12] , 15))
lista_cursos.insertar(lista_cursos,cursos('Introduccion a la ingenieria' , 3 , 3 , ['martes', 13, 14] , 16))
lista_cursos.insertar(lista_cursos,cursos('Calculo diferencial e integral' , 4 , 3 , ['miercoles', 18, 19] , 17))"""


class admin:
    nombre = None
    tipo = None
    telefono = None
    usuario = None
    contrasena = None
    sig = None

    def __init__(self, n , ti , te , u , c):
        self.nombre=n
        self.tipo=ti
        self.telefono=te
        self.usuario=u
        self.contrasena=c

    def recorrer_lista(self) -> str:
        actual = self
        respuesta = "["
        while actual.sig != None:
            respuesta+=f"'{actual.nombre, actual.tipo, actual.usuario, actual.contrasena}',"
            actual=actual.sig
        respuesta+= f"'{actual.nombre, actual.tipo, actual.usuario, actual.contrasena}']"
        return respuesta

    def buscar(self,a):
        actual = self
        while actual.sig != None:
            if actual.usuario == a:
                return actual.nombre, actual.tipo, actual.usuario, actual.contrasena
            else:
                actual = actual.sig
                if actual.usuario == a:
                    return actual.nombre, actual.tipo, actual.usuario, actual.contrasena
        return False
            
    def insertar (self,rn):
        puntero=self
        while (puntero.sig!=None):
            puntero=puntero.sig
        puntero.sig=rn
            
    def guardar_en_archivos(self):
        puntero=self
        try:
            with open("admins.dat", "tw") as archivo:
                archivo.writelines(
                    [puntero.nombre, puntero.tipo, puntero.telefono, puntero.usuario, puntero.contrasena].__str__()+"\n")
                while puntero.sig != None:
                    puntero = puntero.sig
                    archivo.writelines(
                        [puntero.nombre, puntero.tipo, puntero.telefono, puntero.usuario, puntero.contrasena].__str__()+"\n")
        except FileNotFoundError as error:
            messagebox.showerror(title="Error" ,message="Problemas al guardar la información en los archivos")


class estudiante:
    nombre = None
    tipo = None
    carreras = []
    cursos = []
    aprobados = []
    reprobados = []
    usuario = None
    contrasena = None
    horario = None
    reporte = None
    sig = None

    def __init__(self,n,t,ca,cu,a,r,u,c,dicr,dich):
        self.nombre = n
        self.tipo = t 
        self.carreras= ca
        self.cursos= cu
        self.aprobados= a
        self.reprobados= r
        self.usuario= u
        self.contrasena = c
        self.horario = dich
        self.reporte = dicr

    def contar(self):
        cont=1
        actual=self
        while actual.sig!=None:
            actual=actual.sig
            cont+=1
        return(cont)
   
    def recorrer_lista(self) -> str:
        actual = self
        respuesta = "["
        while actual.sig != None:
            respuesta+=f"'{actual.nombre, actual.tipo, actual.carreras, actual.cursos, actual.aprobados, actual.reprobados, actual.usuario, actual.contrasena, actual.horario, actual.reporte}',"
            actual=actual.sig
        respuesta+= f"'{actual.nombre, actual.tipo, actual.carreras, actual.cursos, actual.aprobados, actual.reprobados, actual.usuario, actual.contrasena, actual.horario, actual.reporte}']"
        return respuesta

    def buscar(self,a):
        actual = self
        while actual.sig != None:
            if actual.usuario == a:
                return actual.nombre, actual.tipo, actual.carreras, actual.cursos, actual.aprobados, actual.reprobados, actual.usuario, actual.contrasena, actual.horario, actual.reporte
            else:
                actual = actual.sig
                if actual.usuario == a:
                    return actual.nombre, actual.tipo, actual.carreras, actual.cursos, actual.aprobados, actual.reprobados, actual.usuario, actual.contrasena, actual.horario, actual.reporte
        return False
    
    def insertar (self,rn):
        puntero=self
        while (puntero.sig!=None):
            puntero=puntero.sig
        puntero.sig=rn
        
    def guardar_en_archivos(self):
        puntero=self
        try:
            with open("estudiantes.dat", "tw") as archivo:
                archivo.writelines(
                    [puntero.nombre, puntero.tipo, puntero.carreras, puntero.cursos, puntero.aprobados, puntero.reprobados, puntero.usuario, puntero.contrasena, puntero.reporte, puntero.horario].__str__()+"\n")
                while puntero.sig != None:
                    puntero = puntero.sig
                    archivo.writelines(
                        [puntero.nombre, puntero.tipo, puntero.carreras, puntero.cursos, puntero.aprobados, puntero.reprobados, puntero.usuario, puntero.contrasena, puntero.reporte, puntero.horario].__str__()+"\n")
        except FileNotFoundError as error:
            messagebox.showerror(title="Error" ,message="Problemas al guardar la información en los archivos")

"""estudiantes = estudiante (
        'Estudiante 1', 'estudiante' , ['Ingenieria en computacion'],  [1, 2, 3, 4, 5, 6, 7],  [],  [], 
        'e1',  hashlib.md5('12345'.encode('ascii')).hexdigest(),
            {
            'lunes':      {7: [], 8:[], 9:["Matematica general"], 10:["Matematica general"], 11:["Matematica general"], 12:["Matematica general"], 13:["Matematica discreta"], 14:["Matematica discreta"], 15:[], 16:[], 17:[], 18:["Repaso mate"], 19:["Repaso mate"], 20:[], 21:[], 22:["descanso"], 23:["descanso"], 24:[] },
            'martes':     {7: ["Introduccion a la programacion"], 8:["Introduccion a la programacion"], 9:["Comunicacion escrita"], 10:["Comunicacion escrita"], 11:["Comunicacion escrita"], 12:["Comunicacion escrita"], 13:[], 14:[], 15:[], 16:[], 17:[], 18:[], 19:[], 20:[], 21:[], 22:[], 23:[], 24:[] },
            'miercoles':  {7: [], 8:[], 9:["Ingles 1"], 10:["Ingles 1"], 11:["Ingles 1"], 12:["Ingles 1"], 13:[], 14:[], 15:[], 16:[], 17:[], 18:[], 19:[], 20:[], 21:[], 22:[], 23:[], 24:[] },
            'jueves':     {7: [], 8:[], 9:["Taller de programacion"], 10:["Taller de programacion"], 11:["Taller de programacion"], 12:["Taller de programacion"], 13:[], 14:[], 15:[], 16:[], 17:[], 18:[], 19:[], 20:[], 21:[], 22:[], 23:[], 24:[] },
            'viernes':    {7: [], 8:[], 9:["Fundamentos de organizacion de computadoras"], 10:["Fundamentos de organizacion de computadoras"], 11:["Fundamentos de organizacion de computadoras"], 12:["Fundamentos de organizacion de computadoras"], 13:[], 14:[], 15:[], 16:[], 17:[], 18:[], 19:[], 20:[], 21:[], 22:[], 23:[], 24:[] },
            'sabado':     {7: [], 8:[], 9:[], 10:[], 11:[], 12:[], 13:[], 14:[], 15:[], 16:[], 17:[], 18:[], 19:[], 20:[], 21:[], 22:[], 23:[], 24:[] },
            'domingo':    {7: [], 8:[], 9:[], 10:[], 11:[], 12:[], 13:[], 14:[], 15:[], 16:[], 17:[], 18:[], 19:[], 20:[], 21:[], 22:[], 23:[], 24:[] },
            },
            {
            'lunes':      [['Matematica general' , 'curso' , 3, ['Ingenieria en computacion']],['Matematica discreta' , 'curso' , 2, ['Ingenieria en computacion'], ], ['Repaso mate' , 'Actividad extracurricular' , 2, 'Matematica general','14/2/22','16/2/22'] , ['descanso', 'ocio', 2,'14/2/22','16/2/22']],
            'martes':     [['Introduccion a la programacion' , 'curso' , 2, ['Ingenieria en computacion']],['Comunicacion escrita' , 'curso' , 4, ['Ingenieria en computacion']],],
            'miercoles':  [['Ingles 1' , 'curso' , 4, ['Ingenieria en computacion']],],
            'jueves':     [['Taller de programacion' , 'curso' , 4, ['Ingenieria en computacion']],],
            'viernes':    [['Fundamentos de organizacion de computadoras' , 'curso' , 4, ['Ingenieria en computacion']],],
            'sabado':     [],
            'domingo':    [],
            }
                )

estudiantes.insertar(estudiantes, estudiante (
        'Estudiante 2', 'estudiante' , ['Ingenieria en procuccion industrial'],  [1, 2, 3, 4, 14, 15],  [],  [], 
        'e2',  hashlib.md5('12345'.encode('ascii')).hexdigest(),
            {
            'lunes':      {7: [], 8: [], 9: [], 10:[], 11:[], 12:[], 13:[], 14:[], 15:[], 16:[], 17:[], 18:[], 19:[], 20:[], 21:[], 22:[], 23:[], 24:[] },
            'martes':     {7: ["Introduccion a la programacion"], 8: ["Introduccion a la programacion"], 9: ["Comunicacion escrita"], 10:["Comunicacion escrita"], 11:["Comunicacion escrita"], 12:["Comunicacion escrita"], 13:[], 14:[], 15:[], 16:[], 17:[], 18:[], 19:[], 20:[], 21:[], 22:[], 23:[], 24:[]},
            'miercoles':  {7: [], 8: [], 9: ["Ingles 1"], 10:["Ingles 1"], 11:["Ingles 1"], 12:["Ingles 1"], 13:[], 14:[], 15:[], 16:[], 17:[], 18:[], 19:[], 20:[], 21:[], 22:[], 23:[], 24:[] },
            'jueves':     {7: [], 8: [], 9: [], 10:[], 11:[], 12:[], 13:[], 14:[], 15:[], 16:[], 17:[], 18:[], 19:[], 20:[], 21:[], 22:[], 23:[], 24:[]},
            'viernes':    {7: [], 8: [], 9: [], 10:[], 11:[], 12:[], 13:[], 14:[], 15:[], 16:[], 17:[], 18:[], 19:[], 20:[], 21:[], 22:[], 23:[], 24:[]},
            'sabado':     {7: [], 8: [], 9: [], 10:[], 11:[], 12:[], 13:[], 14:[], 15:[], 16:[], 17:[], 18:[], 19:[], 20:[], 21:[], 22:[], 23:[], 24:[]},
            'domingo':    {7: [], 8: [], 9: [], 10:[], 11:[], 12:[], 13:[], 14:[], 15:[], 16:[], 17:[], 18:[], 19:[], 20:[], 21:[], 22:[], 23:[], 24:[]},
            },
            dic_reporte))

estudiantes.insertar(estudiantes,estudiante (
        'Estudiante 3', 'estudiante' , [],  [],  [],  [], 
        'e3',  hashlib.md5('12345'.encode('ascii')).hexdigest(),
            dic_horario, dic_reporte))"""
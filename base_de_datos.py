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

class carreras:
    carrera =  ''
    semestres =  None
    cursos =  []
    codigo =  None
    sig = None
    ant = None
    
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
        rn.ant = puntero
        
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

class cursos:
    curso = ''
    creditos = None
    horas_lectivas = None
    horario_de_clases = []
    codigo = None
    sig = None
    ant = None

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
        rn.ant = puntero
        
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

class admin:
    nombre = None
    tipo = None
    telefono = None
    usuario = None
    contrasena = None
    sig = None
    ant = None

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
        rn.ant = puntero
            
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
    actividades = None
    sig = None
    ant = None

    def __init__(self,n,t,ca,cu,a,r,u,c,act,dich):
        self.nombre = n
        self.tipo = t 
        self.carreras= ca
        self.cursos= cu
        self.aprobados= a
        self.reprobados= r
        self.usuario= u
        self.contrasena = c
        self.actividades = act
        self.horario = dich
        

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
            respuesta+=f"'{actual.nombre, actual.tipo, actual.carreras, actual.cursos, actual.aprobados, actual.reprobados, actual.usuario, actual.contrasena,actual.actividades, actual.horario}',"
            actual=actual.sig
        respuesta+= f"'{actual.nombre, actual.tipo, actual.carreras, actual.cursos, actual.aprobados, actual.reprobados, actual.usuario, actual.contrasena,actual.actividades, actual.horario}']"
        return respuesta

    def buscar(self,a):
        actual = self
        while actual.sig != None:
            if actual.usuario == a:
                return actual.nombre, actual.tipo, actual.carreras, actual.cursos, actual.aprobados, actual.reprobados, actual.usuario, actual.contrasena, actual.actividades,actual.horario
            else:
                actual = actual.sig
                if actual.usuario == a:
                    return actual.nombre, actual.tipo, actual.carreras, actual.cursos, actual.aprobados, actual.reprobados, actual.usuario, actual.contrasena, actual.actividades, actual.horario
        return False
    
    def insertar (self,rn):
        puntero=self
        while (puntero.sig!=None):
            puntero=puntero.sig
        puntero.sig=rn
        rn.ant = puntero
        
    def guardar_en_archivos(self):
        puntero=self
        try:
            with open("estudiantes.dat", "tw") as archivo:
                archivo.writelines(
                    [puntero.nombre, puntero.tipo, puntero.carreras, puntero.cursos, puntero.aprobados, puntero.reprobados, puntero.usuario, puntero.contrasena, puntero.actividades, puntero.horario].__str__()+"\n")
                while puntero.sig != None:
                    puntero = puntero.sig
                    archivo.writelines(
                        [puntero.nombre, puntero.tipo, puntero.carreras, puntero.cursos, puntero.aprobados, puntero.reprobados, puntero.usuario, puntero.contrasena, puntero.actividades, puntero.horario].__str__()+"\n")
        except FileNotFoundError as error:
            messagebox.showerror(title="Error" ,message="Problemas al guardar la información en los archivos")


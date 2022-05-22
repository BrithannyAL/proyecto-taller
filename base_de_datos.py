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
    actividades = None
    sig = None

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
        'Estudiante 2', 'estudiante' , ['Ingenieria en produccion industrial'],  [2, 3, 4],  [],  [], 
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
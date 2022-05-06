import hashlib


class carreras:
    carrera =  ''
    semestres =  None
    cursos =  []
    codigo =  None

    def __init__(self,ca,s,cu,co):
        self.carrera=ca
        self.semestres=s
        self.cursos=cu
        self.codigo=co

ingenieria_en_computacion = carreras('Ingenieria en computacion', 8 , [1, 2, 3, 4, 5, 6, 7] , 1)
ingenieria_en_agronomia = carreras('Ingenieria en agronomia', 8 ,[1, 2, 3, 8, 9, 10 ] , 2)
administracion_de_empresas = carreras('Administracion de empresas', 10 ,[1, 2, 3, 11, 12, 13 ] , 3)
administracion_en_produccion_industrial = carreras('Administracion en produccion industrial', 12 ,[1, 2, 3, 14, 15] , 4 )
administracion_en_electronica = carreras('Administracion en produccion industrial', 10 ,[1, 2, 3, 4, 16, 17] , 5 )

print (ingenieria_en_computacion)

class cursos:
    curso = ''
    creditos = None
    horas_lectivas = None
    horario_de_clases = []
    codigo = 1

    def __init__(self , cu , c, h_l , h_c , co ):
        self.curso=cu
        self.creditos= c
        self.horas_lectivas=h_l
        self.horario_de_clases=h_c
        self.codigo=co


matematica = cursos('Matematica general' , 3 , 3,  ['lunes', 9, 12] , 1)
comunicacion = cursos('Comunicacion escrita' , 2 , 3 , ['martes', 9, 12] , 2)
comunicacion = cursos('Ingles 1' , 2 , 3 , ['miercoles', 9, 12] , 3)
intro_progra = cursos('Introduccion a la programacion' , 2 , 3 , ['martes', 7, 8] , 4)
taller_progra = cursos('Taller de programacion' , 3 , 3 , ['jueves', 9, 12] , 5)
fundamentos = cursos('Fundamentos de organizacion de computadoras' , 2 , 3 , ['viernes', 9, 12] , 6)
mate_discreta = cursos('Marematica discreta' , 3 , 3 , ['lunes', 13, 14] , 7)
intro_agro = cursos('Introduccion a la agronomia' , 3 , 3 , ['lunnes', 13, 14] , 8)
agromatica = cursos('Agromatica' , 3 , 3 , ['miercoles', 14, 15] , 9)
biologia = cursos('Biologia general' , 3 , 3 , ['jueves', 16, 17] , 10)
intro_admin = cursos('Introducciona a la administracion de empresas' , 2 , 3 , ['viernes', 18, 19] , 11)
compu_admin = cursos('Computacion para administracion' , 2 , 3 , ['lunes', 18, 19] , 12)
mate_admin = cursos('Matematica para administracion' , 3 , 3 , ['martes', 14, 15] , 13)
dibujo = cursos('Dibijo tecnico' , 2 , 3 , ['miercoles', 19, 19] , 14)
quimica = cursos('Quimica basica' , 2 , 3 , ['martes', 9, 12] , 15)
intro_ingenieria = cursos('Introduccion a la ingenieria' , 3 , 3 , ['martes', 13, 14] , 16)
calculo = cursos('Calculo diferencial e integral' , 4 , 3 , ['miercoles', 18, 19] , 17)


class admin:
    nombre = None
    tipo = None
    telefono = None
    usuario = None
    contrasena = None

    def __init__(self, n , ti , te , u , c):
        self.nombre=n
        self.tipo=ti
        self.telefono=te
        self.usuario=u
        self.contrasena=c

a1 = admin('Brithanny Arguello' , 'admin' , 12345678, 'barguello' , hashlib.md5('12345'.encode('ascii')).hexdigest())

class estudiante:
    nombre = None
    tipo = None
    carreras = []
    cursos = []
    aprobados = []
    reprobados = []
    usuario = None
    contrasena = None
    horario = {}
    reporte = {}

    def __init__(self,n,t,ca,cu,a,r,u,c,h,rep):
        self.nombre = n
        self.tipo = t 
        self.carreras= ca
        self.cursos= cu
        self.aprobados= a
        self.reprobados= r
        self.usuario= u
        self.contrasena = c
        self.horario = h
        self.reporte = rep

e1 = estudiante (
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
e2 = estudiante (
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
            {
            'lunes':      [],
            'martes':     [],
            'miercoles':  [],
            'jueves':     [],
            'viernes':    [],
            'sabado':     [],
            'domingo':    [],
            }
                )
e3 = estudiante (
        'Estudiante 3', 'estudiante' , [],  [],  [],  [], 
        'e2',  hashlib.md5('12345'.encode('ascii')).hexdigest(),
            {
            'lunes':      {7: [], 8: [], 9: [], 10:[], 11:[], 12:[], 13:[], 14:[], 15:[], 16:[], 17:[], 18:[], 19:[], 20:[], 21:[], 22:[], 23:[], 24:[] },
            'martes':     {7: [], 8: [], 9: [], 10:[], 11:[], 12:[], 13:[], 14:[], 15:[], 16:[], 17:[], 18:[], 19:[], 20:[], 21:[], 22:[], 23:[], 24:[]},
            'miercoles':  {7: [], 8: [], 9: [], 10:[], 11:[], 12:[], 13:[], 14:[], 15:[], 16:[], 17:[], 18:[], 19:[], 20:[], 21:[], 22:[], 23:[], 24:[] },
            'jueves':     {7: [], 8: [], 9: [], 10:[], 11:[], 12:[], 13:[], 14:[], 15:[], 16:[], 17:[], 18:[], 19:[], 20:[], 21:[], 22:[], 23:[], 24:[]},
            'viernes':    {7: [], 8: [], 9: [], 10:[], 11:[], 12:[], 13:[], 14:[], 15:[], 16:[], 17:[], 18:[], 19:[], 20:[], 21:[], 22:[], 23:[], 24:[]},
            'sabado':     {7: [], 8: [], 9: [], 10:[], 11:[], 12:[], 13:[], 14:[], 15:[], 16:[], 17:[], 18:[], 19:[], 20:[], 21:[], 22:[], 23:[], 24:[]},
            'domingo':    {7: [], 8: [], 9: [], 10:[], 11:[], 12:[], 13:[], 14:[], 15:[], 16:[], 17:[], 18:[], 19:[], 20:[], 21:[], 22:[], 23:[], 24:[]},
            },
            {
            'lunes':      [],
            'martes':     [],
            'miercoles':  [],
            'jueves':     [],
            'viernes':    [],
            'sabado':     [],
            'domingo':    [],
            }
                )
    




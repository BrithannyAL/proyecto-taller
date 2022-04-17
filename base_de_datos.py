import hashlib

carreras = [
    {
        'carrera' : 'Ingenieria en computacion',
        'semestres' : (8),
        'cursos' : (1,2,3,4,5,6,7)
    },
    {
        'carrera' : 'Ingenieria en agronomia',
        'semestres' : (8),
        'cursos' : (1,2,3,4,8,9,10)
    },
    {
        'carrera' : 'Administracion de empresas',
        'semestres' : (10),
        'cursos' : (1,2,3,4,11,12,13)
    },
    {
        'carrera' : 'Ingenieria en procuccion industrial',
        'semestres' : (12),
        'cursos' : (1,2,3,4,14,15)
    },
    {
        'carrera' : 'Ingenieria electronica',
        'semestres' : (10),
        'cursos' : (1,2,3,4,16,17)
    }
        ]

cursos = (
    {
        'curso' : "Matematica general",
        'creditos' : (3),
        'horas_lectivas' : 3,
        'fecha_inicio' : int,
        'fecha_final' : int,
        'horario_de_clases' : ('lunes' , 9 , 12),
        'codigo' : (1)
    },
    {
        'curso' : "Comunicacion escrita",
        'creditos' : (2),
        'horas_lectivas' : 3,
        'fecha_inicio' : int,
        'fecha_final' : int,
        'horario_de_clases' : (),
        'codigo' : (2)
    }, 
    {
        'curso' : "Ingles 1",
        'creditos' : (2),
        'horas_lectivas' : 3,
        'fecha_inicio' : int,
        'fecha_final' : int,
        'horario_de_clases' : (),
        'codigo' : (3)
    },
    {
        'curso' : "Introduccion a la programacion",
        'creditos' : (2),
        'horas_lectivas' : 3,
        'fecha_inicio' : int,
        'fecha_final' : int,
        'horario_de_clases' : (),
        'codigo' : (4)
    },
    {
        'curso' : "Taller de programacion",
        'creditos' : (3),
        'horas_lectivas' : 3,
        'fecha_inicio' : int,
        'fecha_final' : int,
        'horario_de_clases' : (),
        'codigo' : (5)
    },
    {
        'curso' : "Fundamentos de organizacion de computadoras",
        'creditos' : (2),
        'horas_lectivas' : 3,
        'fecha_inicio' : int,
        'fecha_final' : int,
        'horario_de_clases' : (),
        'codigo' : (6)
    },
    {
        'curso' : "Matematica discreta",
        'creditos' : (3),
        'horas_lectivas' : 3,
        'fecha_inicio' : int,
        'fecha_final' : int,
        'horario_de_clases' : (),
        'codigo' : (7)
    },
    {
        'curso' : "Introduccion a la agronomia",
        'creditos' : (2),
        'horas_lectivas' : 3,
        'fecha_inicio' : int,
        'fecha_final' : int,
        'horario_de_clases' : (),
        'codigo' : (8)
    },
    {
        'curso' : "Agromatica",
        'creditos' : (3),
        'horas_lectivas' : 3,
        'fecha_inicio' : int,
        'fecha_final' : int,
        'horario_de_clases' : (),
        'codigo' : (9)
    },
    {
        'curso' : "Biologia general",
        'creditos' : (3),
        'horas_lectivas' : 3,
        'fecha_inicio' : int,
        'fecha_final' : int,
        'horario_de_clases' : (),
        'codigo' : (10)
    },
    {
        'curso' : "Introduccion a la administracion de empresas",
        'creditos' : (2),
        'horas_lectivas' : 3,
        'fecha_inicio' : int,
        'fecha_final' : int,
        'horario_de_clases' : (),
        'codigo' : (11)
    },
    {
        'curso' : "Computacion para administracion",
        'creditos' : (2),
        'horas_lectivas' : 3,
        'fecha_inicio' : int,
        'fecha_final' : int,
        'horario_de_clases' : (),
        'codigo' : (12)
    },
    {
        'curso' : "Matematica para administracion",
        'creditos' : (3),
        'horas_lectivas' : 3,
        'fecha_inicio' : int,
        'fecha_final' : int,
        'horario_de_clases' : (),
        'codigo' : (13)
    },
       {
        'curso' : "Dibujo tecnico",
        'creditos' : (2),
        'horas_lectivas' : 3,
        'fecha_inicio' : int,
        'fecha_final' : int,
        'horario_de_clases' : (),
        'codigo' : (14)
    },
       {
        'curso' : "Quimica basica",
        'creditos' : (2),
        'horas_lectivas' : 3,
        'fecha_inicio' : int,
        'fecha_final' : int,
        'horario_de_clases' : (),
        'codigo' : (15)
    },
       {
        'curso' : "Introduccion a la ingenieria",
        'creditos' : (3),
        'horas_lectivas' : 3,
        'fecha_inicio' : int,
        'fecha_final' : int,
        'horario_de_clases' : (),
        'codigo' : (16)
    },
       {
        'curso' : "Calculo diferencial e integral ",
        'creditos' : (4),
        'horas_lectivas' : 3,
        'fecha_inicio' : int,
        'fecha_final' : int,
        'horario_de_clases' : (),
        'codigo' : (17)
    },
)

usuarios = [
    {
        'nombre':'Brithanny Arguello',
        'tipo' : 'admin',
        'autenticacion':
        {
            'usuario':tuple(("barguello",)),
            'contraseña':hashlib.md5('12345'.encode('ascii')).hexdigest()
        }
    },
    {
        'nombre':'Steven Chacón',
        'tipo' : 'admin',
        'autenticacion':
        {
            'usuario':tuple(("shcacon",)),
            'contraseña':hashlib.md5('12345'.encode('ascii')).hexdigest()
        }
    }
]


estudiantes = [
    {
        'nombre':'Estudiante 1',
        'tipo' : 'estudiante',
        'tiempo' : int,
        'estudios' : 
        {
            'carreras' : (),
            'cursos'   : ()
        },
        'autenticacion':
        {
            'usuario': 'e1',
            'contraseña':hashlib.md5('12345'.encode('ascii')).hexdigest()
        },
        'horario':
                    {
            'lunes' :      {7 :  (), 8:   (), 9 :  (), 10 : (), 11 : (), 12 : (), 13 : (),14 : (), 15 : (), 16 : (),17 : (),18 : (),19 : (),},
            'martes' :     {7 :  (), 8 :  (), 9 :  (), 10 : (), 11 : (), 12 : (), 13 : (),14 : (), 15 : (), 16 : (),17 : (),18 : (),19 : (),},
            'miercoles' :  {7 :  (), 8 :  (), 9 :  (), 10 : (), 11 : (), 12 : (), 13 : (),14 : (), 15 : (), 16 : (),17 : (),18 : (),19 : (),},
            'jueves' :     {7 :  (), 8 :  (), 9 :  (), 10 : (), 11 : (), 12 : (), 13 : (),14 : (), 15 : (), 16 : (),17 : (),18 : (),19 : (),},
            'viernes' :    {7 :  (), 8 :  (), 9 :  (), 10 : (), 11 : (), 12 : (), 13 : (),14 : (), 15 : (), 16 : (),17 : (),18 : (),19 : (),},
            'sabado' :     {7 :  (), 8 :  (), 9 :  (), 10 : (), 11 : (), 12 : (), 13 : (),14 : (), 15 : (), 16 : (),17 : (),18 : (),19 : (),},
            'domingo' :    {7 :  (), 8 :  (), 9 :  (), 10 : (), 11 : (), 12 : (), 13 : (),14 : (), 15 : (), 16 : (),17 : (),18 : (),19 : (),},
                        
                    }

    },
    {
        'nombre':'Estudiente 2',
        'tipo' : 'estudiante',
        'tiempo' : int,
        'estudios' : 
        {
            'carreras' : (),
            'cursos'   : ()
        },
        'autenticacion':
        {
            'usuario': "e2",
            'contraseña':hashlib.md5('12345'.encode('ascii')).hexdigest()
        },
        'horario':
                    {
            'lunes' :      {7 :  (), 8:   (), 9 :  (), 10 : (), 11 : (), 12 : (), 13 : (),14 : (), 15 : (), 16 : (),17 : (),18 : (),19 : (),},
            'martes' :     {7 :  (), 8 :  (), 9 :  (), 10 : (), 11 : (), 12 : (), 13 : (),14 : (), 15 : (), 16 : (),17 : (),18 : (),19 : (),},
            'miercoles' :  {7 :  (), 8 :  (), 9 :  (), 10 : (), 11 : (), 12 : (), 13 : (),14 : (), 15 : (), 16 : (),17 : (),18 : (),19 : (),},
            'jueves' :     {7 :  (), 8 :  (), 9 :  (), 10 : (), 11 : (), 12 : (), 13 : (),14 : (), 15 : (), 16 : (),17 : (),18 : (),19 : (),},
            'viernes' :    {7 :  (), 8 :  (), 9 :  (), 10 : (), 11 : (), 12 : (), 13 : (),14 : (), 15 : (), 16 : (),17 : (),18 : (),19 : (),},
            'sabado' :     {7 :  (), 8 :  (), 9 :  (), 10 : (), 11 : (), 12 : (), 13 : (),14 : (), 15 : (), 16 : (),17 : (),18 : (),19 : (),},
            'domingo' :    {7 :  (), 8 :  (), 9 :  (), 10 : (), 11 : (), 12 : (), 13 : (),14 : (), 15 : (), 16 : (),17 : (),18 : (),19 : (),},
                        
                    }
    }
        ]
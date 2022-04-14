import hashlib

carreras = [
    {
        'carrera' : 'Ingenieraia en computacion',
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

cursos = [
    {
        'curso' : "Matematica general",
        'creditos' : (3),
        'Profesor' : "Rocio De Los Angeles Quiros Oviedo",
        'codigo' : (1)
    },
    {
        'curso' : "Comunicacion escrita",
        'creditos' : (2),
        'Profesor' : "",
        'codigo' : (2)
    }, 
    {
        'curso' : "Ingles 1",
        'creditos' : (2),
        'Profesor' : "",
        'codigo' : (3)
    },
    {
        'curso' : "Introduccion a la programacion",
        'creditos' : (2),
        'Profesor' : "",
        'codigo' : (4)
    },
    {
        'curso' : "Taller de programacion",
        'creditos' : (3),
        'Profesor' : "",
        'codigo' : (5)
    },
    {
        'curso' : "Fundamentos de organizacion de computadoras",
        'creditos' : (2),
        'Profesor' : "",
        'codigo' : (6)
    },
    {
        'curso' : "Matematica discreta",
        'creditos' : (3),
        'Profesor' : "",
        'codigo' : (7)
    },
    {
        'curso' : "Introduccion a la agronomia",
        'creditos' : (2),
        'Profesor' : "",
        'codigo' : (8)
    },
    {
        'curso' : "Agromatica",
        'creditos' : (3),
        'Profesor' : "",
        'codigo' : (9)
    },
    {
        'curso' : "Biologia general",
        'creditos' : (3),
        'Profesor' : "",
        'codigo' : (10)
    },
    {
        'curso' : "Introduccion a la administracion de empresas",
        'creditos' : (2),
        'Profesor' : "",
        'codigo' : (11)
    },
    {
        'curso' : "Computacion para administracion",
        'creditos' : (2),
        'Profesor' : "",
        'codigo' : (12)
    },
    {
        'curso' : "Matematica para administracion",
        'creditos' : (3),
        'Profesor' : "",
        'codigo' : (13)
    },
       {
        'curso' : "Dibujo tecnico",
        'creditos' : (2),
        'Profesor' : "",
        'codigo' : (14)
    },
       {
        'curso' : "Quimica basica",
        'creditos' : (2),
        'Profesor' : "",
        'codigo' : (15)
    },
       {
        'curso' : "Introduccion a la ingenieria",
        'creditos' : (3),
        'Profesor' : "",
        'codigo' : (16)
    },
       {
        'curso' : "Calculo diferencial e integral ",
        'creditos' : (4),
        'Profesor' : "",
        'codigo' : (17)
    },
]

usuarios = [
    {
        'nombre':'Brithanny Arguello',
        'tipo' : 'admin',
        'autenticacion':
        {
            'usuario':tuple(("barguello",)),
            'contraseña':hashlib.md5('98765'.encode('ascii')).hexdigest()
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
        'estudios' : 
        {
            'carreras' : (),
            'cursos'   : ()
        },
        'autenticacion':
        {
            'usuario':tuple(("e1",)),
            'contraseña':hashlib.md5('12345'.encode('ascii')).hexdigest()
        }
    },
    {
        'nombre':'Estudiente 2',
        'tipo' : 'estudiante',
        'estudios' : 
        {
            'carreras' : (),
            'cursos'   : ()
        },
        'autenticacion':
        {
            'usuario':tuple(("e2",)),
            'contraseña':hashlib.md5('12345'.encode('ascii')).hexdigest()
        }
    }
        ]

import hashlib
from re import X


carreras = [
    {
        'carrera' : 'Ingenieraia en computacion',
        'semestres' : (8),
        'cursos' : tuple(1,2,3,4,5,6,7)
    },
    {
        'carrera' : 'Ingenieria en agronomia',
        'semestres' : (8),
        'cursos' : tuple(1,2,3,4,8,9,10)
    },
    {
        'carrera' : 'Administracion de empresas',
        'semestres' : (10),
        'cursos' : tuple(1,2,3,4,11,12,13)
    },
    {
        'carrera' : 'Ingenieria en procuccion industrial',
        'semestres' : (12),
        'cursos' : tuple(1,2,3,4,14,15)
    },
    {
        'carrera' : 'Ingenieria electronica',
        'semestres' : (10),
        'cursos' : tuple(1,2,3,4,16,17)
    }
        ]

cursos = [
    {
        'curso' : "Matematica general",
        'creditos' : (3),
        'Profesor' : "Rocio De Los Angeles Quiros Oviedo",
        'código' : (1)
    },
    {
        'curso' : "Comunicacion escrita",
        'creditos' : (2),
        'Profesor' : "",
        'código' : (2)
    }, 
    {
        'curso' : "Ingles 1",
        'creditos' : (2),
        'Profesor' : "",
        'código' : (3)
    },
    {
        'curso' : "Introduccion a la programacion",
        'creditos' : (2),
        'Profesor' : "",
        'código' : (4)
    },
    {
        'curso' : "Taller de programacion",
        'creditos' : (3),
        'Profesor' : "",
        'código' : (5)
    },
    {
        'curso' : "Fundamentos de organizacion de computadoras",
        'creditos' : (2),
        'Profesor' : "",
        'código' : (6)
    },
    {
        'curso' : "Matematica discreta",
        'creditos' : (3),
        'Profesor' : "",
        'código' : (7)
    },
    {
        'curso' : "Introduccion a la agronomia",
        'creditos' : (2),
        'Profesor' : "",
        'código' : (8)
    },
    {
        'curso' : "Agromatica",
        'creditos' : (3),
        'Profesor' : "",
        'código' : (9)
    },
    {
        'curso' : "Biologia general",
        'creditos' : (3),
        'Profesor' : "",
        'código' : (10)
    },
    {
        'curso' : "Introduccion a la administracion de empresas",
        'creditos' : (2),
        'Profesor' : "",
        'código' : (11)
    },
    {
        'curso' : "Computacion para administracion",
        'creditos' : (2),
        'Profesor' : "",
        'código' : (12)
    },
    {
        'curso' : "Matematica para administracion",
        'creditos' : (3),
        'Profesor' : "",
        'código' : (13)
    },
       {
        'curso' : "Dibujo tecnico",
        'creditos' : (2),
        'Profesor' : "",
        'código' : (14)
    },
       {
        'curso' : "Quimica basica",
        'creditos' : (2),
        'Profesor' : "",
        'código' : (15)
    },
       {
        'curso' : "Introduccion a la ingenieria",
        'creditos' : (3),
        'Profesor' : "",
        'código' : (16)
    },
       {
        'curso' : "Calculo diferencial e integral ",
        'creditos' : (4),
        'Profesor' : "",
        'código' : (17)
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


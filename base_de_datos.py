import hashlib


carreras = [
    {
        'carrera' : 'Ingenieraia en computacion',
        'semestres' : (8),
        'cursos' : {}
    },
    {
        'carrera' : 'Administracion de empresas',
        'semestres' : (10),
    },
    {
        'carrera' : 'Administracion electronica',
        'semestres' : (10),
    },
    {
        'carrera' : 'Ingenieria en agronomia',
        'semestres' : (8),
    },
    {
        'carrera' : 'Ingenieria en procuccion industrial',
        'semestres' : (12),
    }
        ]

cursos = [
    {
        'curso' : "Matematica general",
        'creditos' : (2),
        'Profesor' : "Rocio De Los Angeles Quiros Oviedo",
        'código' : (1)
    },
    {
        'curso' : "Comunicacion escrita",
        'creditos' : (4),
        'Profesor' : "Rocio De Los Angeles Quiros Oviedo",
        'código' : (2)
    }, 
    {
        'curso' : "Ingles 1",
        'creditos' : (6),
        'Profesor' : "Rocio De Los Angeles Quiros Oviedo",
        'código' : (3)
    },
    {
        'curso' : "Matematica general",
        'creditos' : (2),
        'Profesor' : "Rocio De Los Angeles Quiros Oviedo",
        'código' : (4)
    },
    {
        'curso' : "Matematica general",
        'creditos' : (2),
        'Profesor' : "Rocio De Los Angeles Quiros Oviedo",
        'código' : (5)
    },
    {
        'curso' : "Matematica general",
        'creditos' : (2),
        'Profesor' : "Rocio De Los Angeles Quiros Oviedo",
        'código' : (6)
    },
    {
        'curso' : "Matematica general",
        'creditos' : (2),
        'Profesor' : "Rocio De Los Angeles Quiros Oviedo",
        'código' : (7)
    },
    {
        'curso' : "Matematica general",
        'creditos' : (2),
        'Profesor' : "Rocio De Los Angeles Quiros Oviedo",
        'código' : (8)
    },
    {
        'curso' : "Matematica general",
        'creditos' : (2),
        'Profesor' : "Rocio De Los Angeles Quiros Oviedo",
        'código' : (9)
    },
    {
        'curso' : "Matematica general",
        'creditos' : (2),
        'Profesor' : "Rocio De Los Angeles Quiros Oviedo",
        'código' : (10)
    },
    {
        'curso' : "Matematica general",
        'creditos' : (2),
        'Profesor' : "Rocio De Los Angeles Quiros Oviedo",
        'código' : (11)
    },
    {
        'curso' : "Matematica general",
        'creditos' : (2),
        'Profesor' : "Rocio De Los Angeles Quiros Oviedo",
        'código' : (12)
    },
    {
        'curso' : "Matematica general",
        'creditos' : (2),
        'Profesor' : "Rocio De Los Angeles Quiros Oviedo",
        'código' : (13)
    },
    {
        'curso' : "Matematica general",
        'creditos' : (2),
        'Profesor' : "Rocio De Los Angeles Quiros Oviedo",
        'código' : (14)
    },
    {
        'curso' : "Matematica general",
        'creditos' : (2),
        'Profesor' : "Rocio De Los Angeles Quiros Oviedo",
        'código' : (15)
    },
    {
        'curso' : "Matematica general",
        'creditos' : (2),
        'Profesor' : "Rocio De Los Angeles Quiros Oviedo",
        'código' : (16)
    },
    {
        'curso' : "Matematica general",
        'creditos' : (2),
        'Profesor' : "Rocio De Los Angeles Quiros Oviedo",
        'código' : (17)
    },
    {
        'curso' : "Matematica general",
        'creditos' : (2),
        'Profesor' : "Rocio De Los Angeles Quiros Oviedo",
        'código' : (18)
    },
    {
        'curso' : "Matematica general",
        'creditos' : (2),
        'Profesor' : "Rocio De Los Angeles Quiros Oviedo",
        'código' : (19)
    },
    {
        'curso' : "Matematica general",
        'creditos' : (2),
        'Profesor' : "Rocio De Los Angeles Quiros Oviedo",
        'código' : (20)
    }
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
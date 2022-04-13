import hashlib


carreras = [
    {
        'carrera' : 'Ingenieraia en computacion',
    },
    {
        'carrera' : 'Administracion de empresas'
    },
    {
        'carrera' : 'Administracion electronica'
    },
    {
        'carrera' : 'Ingenieria en agronomia'
    },
    {
        'carrera' : 'Ingenieria en procuccion industrial'
    }
        ]

cursos = [
    {
        'curso' : "Fundamentos de organización de computadores",
        'creditos' : (2),
        'Profesor' : "Rocio De Los Angeles Quiros Oviedo"
        'código',
    }
]

usuarios = [
    {
        'usuario': "barguello",
        'contra': (123456789)
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
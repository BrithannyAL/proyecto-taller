import hashlib

cursos = [
    {
        'curso' : "Fundamentos de organización de computadores",
        'creditos' : (2),
        'Profesor' : "Rocio De Los Angeles Quiros Oviedo",
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
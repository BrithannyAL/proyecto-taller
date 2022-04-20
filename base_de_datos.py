import hashlib

carreras = (
    {
        'carrera': 'Ingenieria en computacion',
        'semestres': 8,
        'cursos': [1, 2, 3, 4, 5, 6, 7],
        'codigo': 1
    },
    {
        'carrera': 'Ingenieria en agronomia',
        'semestres': 8,
        'cursos': [1, 2, 3, 4, 8, 9, 10],
        'codigo': 2
    },
    {
        'carrera': 'Administracion de empresas',
        'semestres': 10,
        'cursos': [1, 2, 3, 4, 11, 12, 13],
        'codigo': 3
    },
    {
        'carrera': 'Ingenieria en procuccion industrial',
        'semestres': 12,
        'cursos': [1, 2, 3, 4, 14, 15],
        'codigo': 4
    },
    {
        'carrera': 'Ingenieria electronica',
        'semestres': 10,
        'cursos': [1, 2, 3, 4, 16, 17],
        'codigo': 5
    }
)

cursos = [
    {
        'curso': "Matematica general",
        'creditos': 3,
        'horas_lectivas': 3,
        'fecha_inicio': int,
        'fecha_final': int,
        'horario_de_clases': ['lunes', 9, 12],
        'codigo': 1
    },
    {
        'curso': "Comunicacion escrita",
        'creditos': 2,
        'horas_lectivas': 3,
        'fecha_inicio': int,
        'fecha_final': int,
        'horario_de_clases': ['martes', 9, 12],
        'codigo': 2
    },
    {
        'curso': "Ingles 1",
        'creditos': 2,
        'horas_lectivas': 3,
        'fecha_inicio': int,
        'fecha_final': int,
        'horario_de_clases': ['miercoles', 9, 12],
        'codigo': 3
    },
    {
        'curso': "Introduccion a la programacion",
        'creditos': 2,
        'horas_lectivas': 3,
        'fecha_inicio': int,
        'fecha_final': int,
        'horario_de_clases': ['martes', 7, 8],
        'codigo': 4
    },
    {
        'curso': "Taller de programacion",
        'creditos': 3,
        'horas_lectivas': 3,
        'fecha_inicio': int,
        'fecha_final': int,
        'horario_de_clases': ['jueves', 9, 12],
        'codigo': 5
    },
    {
        'curso': "Fundamentos de organizacion de computadoras",
        'creditos': 2,
        'horas_lectivas': 3,
        'fecha_inicio': int,
        'fecha_final': int,
        'horario_de_clases': ['viernes', 9, 12],
        'codigo': 6
    },
    {
        'curso': "Matematica discreta",
        'creditos': 3,
        'horas_lectivas': 3,
        'fecha_inicio': int,
        'fecha_final': int,
        'horario_de_clases': ['lunes', 13, 14],
        'codigo': 7
    },
    {
        'curso': "Introduccion a la agronomia",
        'creditos': 2,
        'horas_lectivas': 3,
        'fecha_inicio': int,
        'fecha_final': int,
        'horario_de_clases': ['martes', 13, 14],
        'codigo': 8
    },
    {
        'curso': "Agromatica",
        'creditos': 3,
        'horas_lectivas': 3,
        'fecha_inicio': int,
        'fecha_final': int,
        'horario_de_clases': ['miercoles', 14, 15],
        'codigo': 9
    },
    {
        'curso': "Biologia general",
        'creditos': 3,
        'horas_lectivas': 3,
        'fecha_inicio': int,
        'fecha_final': int,
        'horario_de_clases': ['jueves', 16, 17],
        'codigo': 10
    },
    {
        'curso': "Introduccion a la administracion de empresas",
        'creditos': 2,
        'horas_lectivas': 3,
        'fecha_inicio': int,
        'fecha_final': int,
        'horario_de_clases': ['viernes', 18, 19],
        'codigo': 11
    },
    {
        'curso': "Computacion para administracion",
        'creditos': 2,
        'horas_lectivas': 3,
        'fecha_inicio': int,
        'fecha_final': int,
        'horario_de_clases': ['lunes', 18, 19],
        'codigo': 12
    },
    {
        'curso': "Matematica para administracion",
        'creditos': 3,
        'horas_lectivas': 3,
        'fecha_inicio': int,
        'fecha_final': int,
        'horario_de_clases': ['martes', 15, 14],
        'codigo': 13
    },
    {
        'curso': "Dibujo tecnico",
        'creditos': 2,
        'horas_lectivas': 3,
        'fecha_inicio': int,
        'fecha_final': int,
        'horario_de_clases': ['miercoles', 19, 19],
        'codigo': 14
    },
    {
        'curso': "Quimica basica",
        'creditos': 2,
        'horas_lectivas': 3,
        'fecha_inicio': int,
        'fecha_final': int,
        'horario_de_clases': ['martes', 9, 12],
        'codigo': 15
    },
    {
        'curso': "Introduccion a la ingenieria",
        'creditos': 3,
        'horas_lectivas': 3,
        'fecha_inicio': int,
        'fecha_final': int,
        'horario_de_clases': ['martes', 13, 14],
        'codigo': 16
    },
    {
        'curso': "Calculo diferencial e integral ",
        'creditos': 4,
        'horas_lectivas': 3,
        'fecha_inicio': int,
        'fecha_final': int,
        'horario_de_clases': ['miercoles', 18, 19],
        'codigo': 17
    }
]

usuarios = [
    {
        'nombre': 'Brithanny Arguello',
        'tipo': 'admin',
        'telefono' : 12345678,
        'autenticacion':
        {
            'usuario': 'barguello',
            'contraseña': hashlib.md5('12345'.encode('ascii')).hexdigest()
        }
    },
    {
        'nombre': 'Steven Chacón',
        'tipo': 'admin',
        'telefono' : 12345678,
        'autenticacion':
        {
            'usuario': 'shcacon',
            'contraseña': hashlib.md5('12345'.encode('ascii')).hexdigest()
        }
    }
]


estudiantes = [
    {
        'nombre': 'Estudiante 1',
        'tipo': 'estudiante',
        'tiempo': int,
        'estudios':
        {
            'carreras': ['Ingenieria en computacion'],
            'cursos': [1, 2, 3, 4, 5, 6, 7]
        },
        'autenticacion':
        {
            'usuario': 'e1',
            'contraseña': hashlib.md5('12345'.encode('ascii')).hexdigest()
        },
        'horario':
        {
            'lunes':      {7: [], 8:[], 9:["Matematica general"], 10:["Matematica general"], 11:["Matematica general"], 12:["Matematica general"], 13:["Matematica discreta"], 14:["Matematica discreta"], 15:[], 16:[], 17:[], 18:[], 19:[], },
            'martes':     {7: ["Introduccion a la programacion"], 8:["Introduccion a la programacion"], 9:["Comunicacion escrita"], 10:["Comunicacion escrita"], 11:["Comunicacion escrita"], 12:["Comunicacion escrita"], 13:[], 14:[], 15:[], 16:[], 17:[], 18:[], 19:[], },
            'miercoles':  {7: [], 8:[], 9:["Ingles 1"], 10:["Ingles 1"], 11:["Ingles 1"], 12:["Ingles 1"], 13:[], 14:[], 15:[], 16:[], 17:[], 18:[], 19:['a'], },
            'jueves':     {7: [], 8:[], 9:["Taller de programacion"], 10:["Taller de programacion"], 11:["Taller de programacion"], 12:["Taller de programacion"], 13:[], 14:[], 15:[], 16:[], 17:[], 18:[], 19:[], },
            'viernes':    {7: [], 8:[], 9:["Fundamentos de organizacion de computadoras"], 10:["Fundamentos de organizacion de computadoras"], 11:["Fundamentos de organizacion de computadoras"], 12:["Fundamentos de organizacion de computadoras"], 13:[], 14:[], 15:[], 16:[], 17:[], 18:[], 19:[], },
            'sabado':     {7: [], 8:[], 9:[], 10:[], 11:[], 12:[], 13:[], 14:[], 15:[], 16:[], 17:[], 18:[], 19:[], },
            'domingo':    {7: [], 8:[], 9:[], 10:[], 11:[], 12:[], 13:[], 14:[], 15:[], 16:[], 17:[], 18:[], 19:[], },

        }

    },
    {
        'nombre': 'Estudiente 2',
        'tipo': 'estudiante',
        'tiempo': int,
        'estudios':
        {
            'carreras': ['Ingenieria en procuccion industrial'],
            'cursos': [1, 2, 3, 4, 14, 15]
        },
        'autenticacion':
        {
            'usuario': "e2",
            'contraseña': hashlib.md5('12345'.encode('ascii')).hexdigest()
        },
        'horario':
        {
            'lunes':      {7: [], 8: [], 9: [], 10:[], 11:[], 12:[], 13:[], 14:[], 15:[], 16:[], 17:[], 18:[], 19:[], },
            'martes':     {7: ["Introduccion a la programacion"], 8: ["Introduccion a la programacion"], 9: ["Comunicacion escrita"], 10:["Comunicacion escrita"], 11:["Comunicacion escrita"], 12:["Comunicacion escrita"], 13:[], 14:[], 15:[], 16:[], 17:[], 18:[], 19:[], },
            'miercoles':  {7: [], 8: [], 9: ["Ingles 1"], 10:["Ingles 1"], 11:["Ingles 1"], 12:["Ingles 1"], 13:[], 14:[], 15:[], 16:[], 17:[], 18:[], 19:[], },
            'jueves':     {7: [], 8: [], 9: [], 10:[], 11:[], 12:[], 13:[], 14:[], 15:[], 16:[], 17:[], 18:[], 19:[], },
            'viernes':    {7: [], 8: [], 9: [], 10:[], 11:[], 12:[], 13:[], 14:[], 15:[], 16:[], 17:[], 18:[], 19:[], },
            'sabado':     {7: [], 8: [], 9: [], 10:[], 11:[], 12:[], 13:[], 14:[], 15:[], 16:[], 17:[], 18:[], 19:[], },
            'domingo':    {7: [], 8: [], 9: [], 10:[], 11:[], 12:[], 13:[], 14:[], 15:[], 16:[], 17:[], 18:[], 19:[], },
        }
    }
]

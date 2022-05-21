from cargar_en_archivos import cargar_archivos_estudiantes, cargar_archivos_admins

estudiantes = cargar_archivos_estudiantes()
admins = cargar_archivos_admins()

registro_actual = None

comparar = 'nada'

puntero = admins
while registro_actual == None:
    if puntero.usuario == comparar:
        registro_actual = puntero
    else:
        if puntero.sig != None:
            puntero = puntero.sig
        else:
            registro_actual = False
        
print(registro_actual)
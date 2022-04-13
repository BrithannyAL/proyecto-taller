import hashlib
from base_de_datos import usuarios

def login():
    correcto = False
    while correcto == False:
        print("Digite el usuario y contraseña para ingresar")
        usuario = input("Usuario: ")
        contra = hashlib.md5(input("Contraseña: ").encode('ascii')).hexdigest()
        for item in usuarios:
            if (usuario in item['autenticacion']['usuario']) and (contra in item['autenticacion']['contraseña']):
                correcto = True
                print("Ha ingresado como", item['tipo'])
                menu(item['tipo'])
        if correcto == False:
            print("Vuelva a intentar")
            
def menu(tipo):
    print("""
        ********************************* Bienvenido usuario {} *********************************
        Menu de opciones:
        1: Agregar cursos
        2: Modificar cursos
        3: Agregar carreras
        4: Modificar carreras
          """.format(tipo))
    
    opcion = input("¿Qué acción desea realizar? ")
    return opcion
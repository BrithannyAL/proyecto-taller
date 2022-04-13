import hashlib
from base_de_datos import usuarios

correcto = False

while correcto == False:
    print("Digite el usuario y contraseña para ingresar")

    usuario = input("Usuario: ")
    contra = hashlib.md5(input("Contraseña: ").encode('ascii')).hexdigest()

    for item in usuarios:
        if (usuario in item['autenticacion']['usuario']) and (contra in item['autenticacion']['contraseña']):
            correcto = True
            print("Ha ingresado como", item['tipo'])
    
    if correcto == False:
        print("Vuelva a intentar")
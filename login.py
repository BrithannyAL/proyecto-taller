from base_de_datos import usuarios

correcto = False

nameU = "barguello"
passw = "123456789"
    
while correcto == False:
    print("Digite el usuario y contraseña para ingresar")

    usuario = input("Usuario: ")
    contra = input("Contraseña: ")

    #BUSCAR LA CONTRASEÑA Y USUARIO CORRECTO

    if (usuario in nameU) and (contra in passw):
        correcto = True
        print("Ha ingresado")
    
    if correcto == False:
        print("Vuelva a intentar")
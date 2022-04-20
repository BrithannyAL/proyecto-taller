#Desde aquí se llama a la función que realiza el login y al mismo timepo une todas los archivos
from login import login
from login import registrar

opcion = input("""Digite 1 si desea iniciar sesión 
Digite 2 si desea registrarse
""")


if opcion == '1':
    login()
elif opcion == '2':
    registrar()

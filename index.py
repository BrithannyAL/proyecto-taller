#Desde aquí se llama a la función que realiza el login y al mismo timepo une todas los archivos
import msvcrt
from login import inicio
import shutil


shutil.copy('txt.txt', 'base_de_datos.py')

inicio()

msvcrt.getch()



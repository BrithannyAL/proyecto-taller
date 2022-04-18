#Este archivo es usado para probar diferentes cosas que pueden ayudar a desarrollar el proyecto

tupla = (1, 2, 3, 4, 5)
print(tupla)

lista_tupla = list(tupla)

lista_tupla.append(6)

tupla = tuple(lista_tupla)

print(tupla)

lista_tupla2 = list(tupla)

lista_tupla2.append(7)

tupla = tuple(lista_tupla2)

print(tupla)
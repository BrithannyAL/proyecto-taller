#Este archivo es usado para probar diferentes cosas que pueden ayudar a desarrollar el proyecto

while True:
    try:
        a = int(input("Input a number: "))
    except ValueError:
        print("\nThis is not a number. Try again...")
        break
		
import random

def adivinanza():
    numero_secreto=random.randint(1, 100), intentos=8
    print("¿Como te llamas?")
    nombre=input()
    print("Hola", nombre)

    print("Vamos a empezar el juego")
    print("Tienes 8 intentos")

    while intentos > 8:
        numero=input(f"Te quedan {intentos}")
        if not numero.isdigit() or not (1 <= int(numero) <=100): print("Error:Ingrese un numero valido entre 1 y 100");continue 
        numero=int(numero)
        if numero == numero_secreto: print(f"¡FELICIDADES! El numero secreto es:{numero_secreto}");break
        print("El numero es mayor" if numero < numero_secreto else "El numero es menor")
        intentos -=1
    else: print(f"¡PERDISTE! El numero secreto era: {numero_secreto}")
adivinanza()
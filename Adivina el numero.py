from random import *
my_random=randint(1,100)
#print(my_random) #creamos un numero cualquiera

name=input("Cual es tu nombre? ")
print(f"Genial {name}, He pensado en un numero del 1 al 100 puedes adivinarlo? Solo tienes 8 intentos" )

tries=1 #intentos
while tries<=8:
    number=int(input("Cuál número crees que sea?"))
    if number<1 or number>100:
        print("Escogiste un numero fuera del rango")
        tries+=1
        continue
    elif number<my_random:
        print("la respuesta es incorrecta,escogiste un numero más pequeño que el número secreto")
        tries+=1
        continue
    elif number>my_random:
        print("la respuesta es incorrecta,escogiste un numero más grande que el número secreto")
        tries+=1
        continue
    elif number==my_random:
        print(f"escogiste el numero correcto, ganaste en {tries} intentos")
        break


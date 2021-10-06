import random
def Humanguess(): 
    number =random.randrange(0,10)
    print(number)
    numero=-1
    while numero!=number:
     numero=int(input("Adivina el numero que estoy pensando: "))
     if number==numero:
        print(f"Felicidades, el numero era: {number}")
     elif numero > number:
        print("Te pasaste el numero es menor")
     else:
        print("El numero es mayor")

Humanguess()
       
import random
#def Humanguess(): 
    #number =random.randrange(0,10)
    #print(number)
    #numero=-1
    #while numero!=number:
     #numero=int(input("Adivina el numero que estoy pensando: "))
     #if number==numero:
     #   print(f"Felicidades, el numero era: {number}")
    # elif numero > number:
   #     print("Te pasaste el numero es menor")
  #   else:
 #       print("El numero es mayor")

#Humanguess()

def computerGuess():
    #number = random.randrange(0,10)
    bandera =False
    NumMax=100
    NumMin=0
    number=random.randrange(NumMin,NumMax)

    while (bandera == False):
        print(number)
        print ("Este es tu numero? ")
        opc = input("Si | No: ").lower()
        if(opc == "no"):
            print("Es mayor o menor?")
            opc2 = input("Mayor | Menor: ").lower()
            if (opc2 == "menor"):
                NumMax=number
                newNumber =random.randrange(NumMin,NumMax)
                number = newNumber
            else:
                NumMin=number
                newNumber = random.randrange(NumMin,NumMax)
                number = newNumber
        else:
            bandera = True
            print("¡Eres muy bueno, has ganado!")

computerGuess()            

       
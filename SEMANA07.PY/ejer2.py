import random

print ("*****************************************")
print ("*     BIENVENIDO AL JUEGO ADIVINADOR    *")
print ("*  1.-ADIVINAR EL NÚMERO ENTRE 1 Y 20   *")
print ("*  2.-      TIENES 3 INTENTOS           *")
print ("*****************************************")

intentos = 3
secreto = random.randint(1,20)
while intentos > 0:
    num = int(input("INGRESE NÚMERO: "))

    if secreto == num:
        print("\nCORRECTO! ADIVINASTE EL NÚMERO. ")
        break
    else: 
        intentos-=1
        if num < secreto: print(f"\nPISTA: EL NÚMERO ES MAYOR. TE QUEDAN {intentos} intentos")
        else: print(f"\nPISTA: EL NÚMERO ES MENOR. TE QUEDAN {intentos} intentos")
else: print ("\nNO LOGRASTE ADIVINAR EL NÚMERO ", secreto)

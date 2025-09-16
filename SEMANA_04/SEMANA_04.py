def ejerc1():
    edad = int(input ("Ingrese una edad: "))

    if edad < 18:
        print ("Menor de edad")
    else:
        if edad>=18 and edad <=64:
            print("adulto")
        else:
            print ("adulto mayor")

def ejer2():
    año = int (input("Ingrese el año: "))

    if año %4 == 0 and año %100 !=0 or año %400 ==0:
        print ("El año es bisiesto")
    else: 
        print ("El año no es bisiesto")

    if año %2 ==0:
        print("El año es par")
    else:
        print("El año no es par")

def ejer3():
    monto = float(input("Ingrese el monto en soles: "))

    print("\n1. Dolares\n2. Euros")

    opcion = int(input("\nIngrese una opción: "))

    match opcion:
        case 1: print ("Dolares: ", round(monto/3.75))
        case 2: print (f"Euros: {monto/4.05:.2f}")
        case _: print ("Opción incorrecta")
import math
def ejer4():
    print ("Bienvenido al sistema de calculos de áreas")
    print ("1. CUADRADO")
    print ("2. RECTANGULO")
    print ("3. TRIANGULO")
    print ("4. CIRCULO\n")

    opcion = int(input("Ingrese una opción: "))

    match opcion:
        case 1:
            lado =int(input("Ingrese lado:"))
            print ("Área del Cuadrado: ", lado * lado)
        case 2:
            bas1 = int(input("Ingrese base:"))
            altur1 = int(input("Ingrese altura:"))
            print ("Área de Reactangulo: ", (bas1 * altur1))
        case 3:
            bas2 = int(input("Ingrese base:"))
            altur2 = int(input("Ingrese altura:"))
            print("Área del Triángulo: ", (bas2 * altur1)/2)
        case 4:
            radio = int(input("Ingrese radio:"))
           
            print("Área del Circulo: ",(round(math.pi * radio**2),2))

        case _: print ("Opción incorrecta")



ejer4()

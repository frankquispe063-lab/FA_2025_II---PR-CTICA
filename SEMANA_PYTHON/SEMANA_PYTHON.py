def ejer1():
    nombre = input("INGRESE SU NOMBRE")
    carrera = input("INGRESE SU CARRERA")
    
    print(f"{nombre}, BIENVENIDO A FUND.ALGORIT {carrera}")

def ejer2():
    print ("\"FRANK\"")

def ejer3():
    x= int(input("Ingresa el valor de x: "))
    y= int(input("Ingresa el valor de y: "))

    print ("suma: ", (x+y))
    print ("resta: ", (x-y))
    print ("multiplicación: ", (x*y))
    print ("división: ", (x/y))

    import math #importando la libreria math

def ejer4():
    num = float(input("Ingrese un número decimal:"))

    print ("Raaiz 2: ", math.sqrt(num))
    print ("Redondeado", round(num, 0))
    print ("al cubo: ", math.pow(num, 3))
    print ("Raaiz 3: ", num ** (1/3))

def ejer5():
    num =  input  ("Ingrese número: ")

    entero = int(num)
    deci = float(num)

    print ("Resto: ", (entero%2))
    print ("División: ", (deci/3))

ejer5()

def ejerc1():
    edad = int(input("Ingrese su edad: "))

    if edad>=18:
        print ("PUEDE VOTAR")

        if edad >= 25:
            print ("CANDIDATO PARA UN CARGO POLITICO")
        else:
            print ("NO ES CANDIDATO PARA UN CARGO POLITICO")

    else: 
        print ("NO PUEDE VOTAR ")
        print ("NO PUEDE EJERCER UN CARGO POLITICO")

def ejerc2():
    lado1 = int(input("Ingrese lado1: "))
    lado2 = int(input("Ingrese lado2: "))
    lado3 = int(input("Ingrese lado3: "))

    if (lado1 == lado2 == lado3):
        print ("EQUILATERO")
    elif lado1 == lado2 or lado1 ==lado3 or lado2 == lado3:
        print ("ISOCELES")
    else:
        print ("ESCALENO")

def ejerc3():
    n = int(input("ingrese un número: "))
    suma = 0
    for i in range(1, n+1):
        print(i)
 
        if i % 2 == 0:
            suma +=i

        print ("\nSuma de pares: ", suma)

def ejerc4():
    cant = int(input("Ingrese la cantidad de números: "))
    ceros = pares = impares = 0
    for i in range(1, cant+1): 
        num= int(input(f"Ingrese el número {i}: "))

        if num == 0:
            ceros+=1 # CEROS ++
        elif num % 2 == 0:
            pares+=1 # PARES ++
        else:
            impares +=1 # IMPAR ++

            print("\n# ceros: ", ceros)
            print("# pares: ", pares)
            print("# impares: ", impares)

ejerc4()


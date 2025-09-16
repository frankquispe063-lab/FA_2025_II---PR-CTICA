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
 

ejerc2()


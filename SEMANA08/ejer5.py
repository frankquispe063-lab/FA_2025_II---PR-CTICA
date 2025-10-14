def suma(a,b): print("\nLa suma es: ", a+b)
def resta(a,b): print("\nLa suma es: ", a-b)
def multi(a,b): print("\nLa Multiplicai�n es: ", a*b)
def divi(a,b): 
    if b!= 0 : print("\nLa Divisi�n es: ", a/b)
    else: print ("\nError. No se puede dividir por cero")

def operaciones():
    while True:
        print("Men� de operaciones")
        print("1. Suma")
        print("2. Resta")
        print("3. Multiplicaci�n")
        print("4. Divisi�n")

        opc = int (input("\nIngrese una opci�n: "))

        a = int(input("Ingrese el primer numero: "))
        b = int(input("Ingrese el segundo numero: "))

        if opc in (1, 2, 3, 4):
            if 1: suma(a,b)
            elif 2: resta(a,b)
            elif 3: multi(a,b)
            elif 4: divi(a,b)
            else : print ("Opcion no v�lida")

        conti = input("�Desea continuar? presione (y): ")

        if conti != "y":
            print ("\n Programa finalizado!")
            break

operaciones()

    

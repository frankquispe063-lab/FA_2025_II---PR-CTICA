p = i = 0

while True:
    num = int(input("INGRESE NÚMERO ENTERO (NEGATIVO PARA SALIR): "))

    if num < 0: 
        break
    if num %2 == 0: p+=1
    else: i+=1

print ("\nCANTIDAD DE PARES: ", p)
print("CANTIDAD DE IMPARES: ", i)

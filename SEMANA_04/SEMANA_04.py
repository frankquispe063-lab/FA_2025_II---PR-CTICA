def ejerc1():
    edad = int(input ("Ingrese una edad: "))

    if edad < 18:
        print ("Menor de edad")
    else:
        if edad>=18 and edad <=64:
            print("adulto")
        else:
            print ("adulto mayor")

ejerc1()

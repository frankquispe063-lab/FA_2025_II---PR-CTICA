g = input("GENERE UNA CONTRASEÑA: ")

print ("----------------------------------------------")
print ("-|           VALIDA TU CONTRASEÑA           |-")
print ("-|                                          |-")
print ("-|           UD. TIENE 3 INTENTOS           |-")
print ("--------------------------------------------\n")

intentos = 3

while (intentos > 0 ):
    c = input("INGRESE LA CONTRASEÑA: ")
    
    if g == c:
        print ("\nACCESO CONCEDIDO. BIENBENIDO AL SISTEMA. ")
        break
    else: 
        intentos -= 1
        print("CONTRASEÑA INCORRECTA. INTENTOS RESTANTES ", intentos)

else: print("ACCESO DENEGADO! - CERRANDO SISTEMA") 

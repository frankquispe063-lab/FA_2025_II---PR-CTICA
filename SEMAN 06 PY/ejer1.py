num = int(input("Ingrese un número positivo: "))
print()
while num <= 0:
    num = int(input("ERROR.Ingrese un número positivo: "))

i = 1

while i <= 12:
    print (f"{i} X {num} ={i*num}")
    i+=1
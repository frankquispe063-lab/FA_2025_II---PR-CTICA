sumap = sumai = 0
while True:
    num = int(input("Ingrese un número positivo (0 salir): "))
    if num < 0:
        print("Número invalido. ingrese nuevamente")
        continue

    if num == 0:
        break
    if num%2 == 0:
        sumap+= num
    else:
        sumai += num

print("\nSuma pares: ", sumap)
print("Suma de impares: ", sumai)

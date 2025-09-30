while True:
      suma = 0
      num = int(input("INGRESE UN NÚMERO POSITIVO: "))

      for i in range(1,num+1):
          suma += i
          print(i, end=" ")

      print("\nSUMA: ",suma)
      opc = input("\n¿DESEA CONTINUAR? (S/N). ")

      if (opc == "N"): break

     









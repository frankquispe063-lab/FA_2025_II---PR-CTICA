from Triangulo import Triangulo
from Cuadrado import Cuadrado
t = Triangulo()
c = Cuadrado()
def menu1()->None:
    print("BIENVENIDOS A CALCULOS DE ÁREAS Y PERÍMETROS\n")
    print("*********Menú de opciones*********")
    print("*        1. Triángulo            *")
    print("*        2. Cuadrado             *")
    print("*        3. Rectángulo           *")
    print("*        4. Trapecio             *")
    print("*        0. Salir                *")

def menu2()->int:
     print("********* Seleccione cálculo *********")
     print("*        1. Área            *")
     print("*        2. Perímetro       *")
     print("*************************************\n")

     opcion = int(input("Ingrese una opción: "))
     return opcion

while True:
     while True:
         menu1()
         opcion = int (input("Ingrese una opción\n"))

         if opcion in (0, 1, 2, 3, 4): break
         else : print("Error. Opción no válida.\n")

         match opcion:
             case 0:exit()   # quit()
             case 1:
                 opc = menu2()

                 match opc:
                     case 1: t.area()
                     case 2: t.perimetro()
             case 2:
                 opc = menu2()
                 l = int(input("Ingrese lado. "))
                 match opc:
                     case 1: 
                         c.area(l);
                         c.perimetro(l);

                     case 2: t.perimetro()
             case 3:print()
             case 4:print()

         while True:
             conti = input("¿Desea continuar (S/N): ")
             if conti in("S","N"): break
             else: print("Error. Solo ingrese 'S' o 'N'.")

         if conti == "N": break
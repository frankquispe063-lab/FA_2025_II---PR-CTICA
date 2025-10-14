class Triangulo:
    def area(self)->None:
        b = int(input("\nIngrese la base: "))
        h = int(input("\nIngrese la altura: "))
        print("\Área: ", (b*h)/2)

    def perimetro(self)->None:
        l1 = int(input("\nIngresa lado 1: "))
        l2 = int(input("\nIngresa lado 2: "))
        l3 = int(input("\nIngresa lado 3: "))
        print("\Périmetro: ", l1+l2+l3)

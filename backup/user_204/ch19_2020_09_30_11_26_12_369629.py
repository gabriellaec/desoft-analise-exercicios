lado1 = int(input("Valor 1 "))
lado2 = int(input("Valor 2 "))
lado3 = int(input("Valor 3 "))

if lado1 == lado2 == lado3:
    print("equilátero")
elif lado1 != lado2 != lado3:
    print("escaleno")
else:
    print("isósceles")

l1 = int(input("Insira o primeiro lado: "))
l2 = int(input("Insira o segundo lado: "))
l3 = int(input("Insira o terceiro lado: "))
if l1 == l2 and l2 == l3:
    print("o triângulo é equilátero")
elif l1 == l2 or l1 == l2 or l2 == l3:
    print("o triângulo é isóceles")
else:
    print("o triângulo é escaleno")
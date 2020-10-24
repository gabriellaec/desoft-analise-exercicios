def lados(x, y, z)

if x == y and x == z:
    print("equilátero")

else:
    if x == y or x == z or y == z:
        print("isósceles")

else:
    print("escaleno")
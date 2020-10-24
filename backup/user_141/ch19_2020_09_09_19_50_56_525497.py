def classifica_triangulo(x, y, z):
    if x == y and x == z:
        print("equilátero")
    elif x == y or x == z or y == x:
        print("isósceles")
    else:
        print("escaleno")
    
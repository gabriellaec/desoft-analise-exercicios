def classifica_triangulo(x, y, z):
    if x == y == z:
        print("equilátero")
    elif x == y or x == z or y == z:
        print("isóceles")
    else:
        print("escaleno")
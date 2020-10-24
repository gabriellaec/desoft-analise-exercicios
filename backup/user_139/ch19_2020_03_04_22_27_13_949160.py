def classifica_triangulo(x, y, z):
    if x == y == z:
        print("equilátero")
    elif x == y or x == z or y == z:
        print("isóceles")
    else:
        print("escaleno")
print(classifica_triangulo(3,3,3))
print(classifica_triangulo(3,3,4))
print(classifica_triangulo(3,4,5))
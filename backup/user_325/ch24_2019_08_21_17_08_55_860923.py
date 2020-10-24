def classifica_triangulo(x, y, z):
    if x == y and y == z:
       return "equilátero"
    elif x == y and y != z:
        return "isósceles"
    else:
        return "escaleno"
print(classifica_triangulo(6, 4, 5))
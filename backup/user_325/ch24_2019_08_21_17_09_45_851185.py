def classifica_triangulo(x, y, z):
    if x == y or y == z:
       return "equilátero"
    elif x == y or y != z:
        return "isósceles"
    else:
        return "escaleno"
print(classifica_triangulo(6, 4, 5))
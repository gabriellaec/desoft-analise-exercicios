def classifica_triangulo(x, y, z):
    if x != y != z:
        return "escaleno"
    elif x != y and y == z and x != z:
        return "isósceles"
    else:
        return "equilátero"
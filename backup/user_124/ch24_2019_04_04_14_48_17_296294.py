def classifica_triangulo(x, y, z):
    if x != y != z:
        return "escaleno"
    elif x != y and y == z:
        return "isóceles"
    else:
        return "equilátero"
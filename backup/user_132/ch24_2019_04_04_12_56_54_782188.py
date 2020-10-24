def classifica_triangulo(x, y, z):
    if x != y and y != z and z != x:
        return "escaleno"
    elif x != y or x != z or y != z:
        return "isósceles"
    else:
        return "equilátero"
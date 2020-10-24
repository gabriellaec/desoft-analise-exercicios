def classifica_triangulo(x, y, z):
    if x != y and y != z and x != z:
        return "escaleno"
    elif x==y==z:
        return "equilátero"
    else:
        return "isósceles"
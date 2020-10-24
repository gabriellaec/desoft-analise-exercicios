def classifica_triangulo(x, y, z):
    if x != y and x != z and z != y:
        return "escaleno"
    elif x==y==z:
        return "equilátero"
    else:
        return "isósceles"
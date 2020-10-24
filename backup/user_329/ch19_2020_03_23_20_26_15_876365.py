def classifica_triangulo(x, y, z):
    if x==y and x==z:
        return "equilátero"
    elif x!=y and x!=z and y!=z:
        return "escaleno"
    else:
        return "isósceles"
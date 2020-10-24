def classifica_triangulo(x,y,z):
    if x == y and y ==z:
        return "equilátero"
    elif x == y and x != z:
        return "isósceles"
    elif x == z and x != y:
        return "isósceles"
    else:
        return "escaleno"
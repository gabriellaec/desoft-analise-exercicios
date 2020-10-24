def classifica_triangulo(x, y, z):
    if x == y and y == z:
        return 'equilátero'
    elif x == y and z != x:
        return 'isósceles'
    else:
        return 'escaleno'
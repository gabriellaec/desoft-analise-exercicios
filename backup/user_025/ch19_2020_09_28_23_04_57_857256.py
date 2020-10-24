def classifica_triangulo(x, y, z):
    if x == y and x == z:
        return 'Equilátero'
    elif x == y and x != z:
        return 'Isósceles'
    else:
        return 'Escaleno'
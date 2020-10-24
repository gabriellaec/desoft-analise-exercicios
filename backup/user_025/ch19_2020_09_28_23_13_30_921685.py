def classifica_triangulo(x, y, z):
    if x == y and x == z and y == z:
        return 'Equilátero'
    elif x != y and x != z and y != z:
        return 'Escaleno'
    else:
        return 'Isósceles'
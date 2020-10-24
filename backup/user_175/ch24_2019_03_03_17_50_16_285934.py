def classifica_triangulo(a, b, c):
    if (a == b) and (b == c):
        res = 'equilátero'
    elif (a == b) and (b != c):
        res = 'isósceles'
    else:
        res = 'escaleno'
    return res
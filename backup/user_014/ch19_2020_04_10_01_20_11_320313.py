def classifica_triangulo (a, b, c):
    if a == b == c:
        return 'equilátero'
    elif a == b != c or a != b == c or a == c != b:
        return 'isóceles'
    else:
        return 'escaleno'

def classifica_triangulo(a, b, c):
    if a == b and b == c:
        return 'equilatero'
    if a == b or a == c or b == c:
        return 'isoceles'
    else:
        return 'escaleno'
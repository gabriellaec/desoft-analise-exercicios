def classifica_triangulo(a, b, c):
    if a == b and b == c:
        return('Equilátero')
    if a == b and b != c:
        return('Isósceles')
    if a != b and b != c:
        return('Escaleno')
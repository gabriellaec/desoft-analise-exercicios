def classifica_triangulo(a, b, c):
    if a == b and b == c:
        return('Equilátero')
    if a == b and b != c or a == c and c != b:
        return('Isósceles')
    if a != b and b != c:
        return('Escaleno')
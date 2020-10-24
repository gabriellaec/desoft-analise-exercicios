def classifica_triangulo(a, b, c):
    if a == b and b == c:
        return('equilátero')
    if (a == b and b != c) or (a == c and c != b) or (b == c and c != a):
        return('isósceles')
    else:
        return('escaleno')
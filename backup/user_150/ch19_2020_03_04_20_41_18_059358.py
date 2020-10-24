def classifica_triangulo(a, b, c):
    if a == b and b == c:
        print('Equilátero')
    if a == b and b != c:
        print('Isósceles')
    else:
        print('Escaleno')
def classifica_triangulo(a, b, c):
    if a == b and b == c:
        print('Equilátero')
    if a == b and b != c:
        print('Isósceles')
    if a != b and b != c:
        print('Escaleno')
classifica_triangulo(10, 9, 8)
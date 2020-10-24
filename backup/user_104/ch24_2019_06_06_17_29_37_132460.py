def classifica_triangulo(a, b, c):
    if a == b and a ==c and c == b:
        x = 'equilátero'
    elif a != b and a != c and c != b:
        x = 'escaleno'
    else:
        x = 'isósceles'
    return x
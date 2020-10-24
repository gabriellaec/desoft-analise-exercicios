def classifica_triangulo(a, b, c):
    a = input('a: ')
    b = input('b: ')
    c = input('c: ')
    if a == b:
        if b == c:
            return 'equilátero'
        else:
            return 'isóceles'
    else:
        if b == c:
            return 'isóceles'
        return 'escaleno'
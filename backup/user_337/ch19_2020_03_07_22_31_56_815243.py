def classifica_triangulo (a,b,c):
    if a == b and b == c:
        return 'equilátero'
    elif a == c != b or a == b != c or b == c != a:
        return 'isósceles'
    else:
        return 'escaleno'

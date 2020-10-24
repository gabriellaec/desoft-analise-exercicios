def classifica_triangulo (a,b,c):
    if a == b == c:
        classe = 'equilátero'
    elif a == b != c or a == c != b or b == c != a:
        classe = 'isósceles'
    else:
        classe = 'escaleno'
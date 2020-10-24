def classifica_triangulo (a,b,c):
    if a == b and b == c:
        classe = 'equilátero'
    elif a==b or a==c or b==c:
        classe = 'isósceles'
    else:
        classe = 'escaleno'
    return classe
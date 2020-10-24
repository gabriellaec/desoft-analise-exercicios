def classifica_triangulo (a,b,c):
    if a ==(b and c):
        classe = 'equilátero'
    elif a != (b or c):
        classe = 'isósceles'
    else:
        classe = 'escaleno'
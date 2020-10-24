def classifica_triangulo(a,b,c):
    if a==b==c:
        return 'Equilátero'
    elif a==b!=c or a!=b==c:
        return 'Isósceles'
    else:
        return 'Escaleno'
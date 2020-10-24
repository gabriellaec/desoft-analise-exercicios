def classifica_triangulo(a,b,c):
    if a==b==c:
        return 'É equilátero'
    elif a==b!=c or a!=b==c:
        return 'É isósceles'
    else:
        return 'É escaleno'
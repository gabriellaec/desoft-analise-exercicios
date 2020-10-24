def classifica_triangulo(a,b,c):
    if a==b and b==c and a==c:
        return 'Equilátero'
    elif a!=b and b!=c and a!=c:
        return 'Escaleno'
    else:
        return 'Isósceles'
def classifica_triangulo(a,b,c):
    if a==b and b==c:
        return 'equilátero'
    if a!=b and b!=c and c!=a:
        return 'escaleno'
    else:
        return 'isósceles'
def classifica_triangulo(a,b,c):
    if a==b and b==c:
        return 'equilátero'
    elif a==b and b!=c or c==a and a!=b or c==b and c!=a:
            return 'isósceles'
    else:
            return'escaleno'
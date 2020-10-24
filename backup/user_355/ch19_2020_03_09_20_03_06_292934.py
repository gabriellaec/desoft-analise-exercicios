def Classifica_triangulo(a,b,c):
    if a==b and b==c:
        return 'equilátero'
    else:
        if a==b and b!=c or c==a and a!=b or c==b and c!=a:
            return 'isósceles'
    else:
        if a!=b and b!=c and c!=a
            return'escaleno'
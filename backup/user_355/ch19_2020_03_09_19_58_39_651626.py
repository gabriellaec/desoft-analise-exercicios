def Classifica_triangulo(a,b,c):
    if a==b and b==c:
        return 'equilátero'
    else:
        if a==b or b==c or c==a:
            return 'isósceles'
    else:
        return 'escaleno'
def classifica_triangulo(a,b,c):
    if a==b==c:
        return 'equilatero'
    elif a==b or b==c or c==a:
        return 'isoceles'
    else:
        return 'escaleno'
    
def classifica_triangulo(a,b,c):
    if a==b and a==c:
        return 'equilátero'
    elif a==b and a!=c:
        return 'isóceles'
    else:
        return 'escaleno'
def classifica_triangulo(a,b,c):
    if a==b and a==c:
        return 'equilátero'
    elif a!=b and a!=b and b!=c:
        return 'escaleno'
    else:
        return 'isóceles'

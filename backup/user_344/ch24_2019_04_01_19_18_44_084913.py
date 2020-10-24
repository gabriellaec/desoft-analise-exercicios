def classifica_triangulo(a,b,c):
    if a==b and b==c:
        return 'equilátero'
    elif a==b and b!=c or a==c and a!=b:
        return 'isóceles'
    else:
        return 'escaleno'
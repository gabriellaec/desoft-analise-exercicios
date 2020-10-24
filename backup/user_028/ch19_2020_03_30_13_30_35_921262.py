def classifica_triangulo(a,b,c):
    if a==b==c:
        return 'equilátero'
    elif a==b!=c or b==c!=a or a==c!=b:
        return 'isóceles'
    else:
        return 'escaleno'
    
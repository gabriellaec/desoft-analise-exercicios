def classifica_triangulo(a,b,c):
    if a==b==c:
        return 'equilátero'
    elif a==c and c!=b or b==c and c!=a or a==b and b!=c :
        return 'isocesles'
    else:
        return 'escaleno'
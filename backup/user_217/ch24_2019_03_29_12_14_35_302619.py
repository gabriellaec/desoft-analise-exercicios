def classifica_triangulo(a,b,c):
    if a==b==c:
        return 'equilátero'
    elif a==b!=c and a!=b==c:
        return 'isocesles'
    else:
        return 'escaleno'
   
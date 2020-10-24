def classifica_triangulo(a,b,c):
    if a==b==c :
        return 'equilátero'
    elif a!=c and b!=a and b!=c :
        return 'escaleno'
    else : 
        return 'isósceles'
        
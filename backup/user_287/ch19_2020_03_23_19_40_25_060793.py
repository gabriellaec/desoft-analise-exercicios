def classifica_triangulo(a,b,c):
    if a==b==c :
        return 'equilatero'
    elif a!=b!=c :
        return 'escaleno'
    else :
        return 'isosceles'
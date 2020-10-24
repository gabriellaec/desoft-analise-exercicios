def classifica_triangulo(x,y,z):
    if x==y and y==z:
        return 'Equilátero'
    elif x==y or y==z or x==z:
        return 'Isósceles'
    else:
        return 'Escaleno'
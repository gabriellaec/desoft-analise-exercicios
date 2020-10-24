def classifica_triangulo(x, y, z):
    if x==y and y==z:
        return 'equilátero'
    elif x==y and x!=z or x==z and x!=y or y==z and z!=x:
        return 'isósceles'
    else:
        return 'escaleno'


             
    
    
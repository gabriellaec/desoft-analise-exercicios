def classifica_triangulo(x,y,z):
    if x==y==z:
        return 'equilatero'
    elif x!=y and y!=z and z!=x:
        return 'escaleno'
    else: 
        return 'isosceles'
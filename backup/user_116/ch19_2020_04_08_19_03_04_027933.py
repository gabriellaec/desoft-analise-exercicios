def classifica_triangulo(x,y,z):
    if x==y and x==z and y==z:
        return 'equilátero'
    elif x==y and x!=z:
        return 'isóceles'
    elif  x==z and x!=y:
        return 'isóceles'
    elif  z==y and z!=x:
        return 'isóceles'
    else:
        return 'escaleno'
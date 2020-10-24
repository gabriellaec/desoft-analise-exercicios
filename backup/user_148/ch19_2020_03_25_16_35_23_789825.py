def classifica_triangulo(x, y, z):
    if x=y=z:
        return 'equilátero'
    elif x!=y!=z:
        return 'escaleno'
    elif (x=y and y!=z or x=z and z!=y or y=z and z!=x):
        return 'isósceles'
def classifica_triangulo(x, y, z):
    if x == y and y == z:
        return 'equilátero'
    elif x == y and z != x:
        return 'isósceles' 
    elif x == z and y != x:
        return 'isósceles'
    elif z == y and x!= z:
        return 'isósceles'
    else:
        return 'escaleno'
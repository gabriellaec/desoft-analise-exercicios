def   classifica_triangulo(x,y,z):
    if x == y and x == z:
        return 'equilátero'
    else:
        if x == y or y==z or x==z:
            return 'isósceles'
        else:
            return 'escaleno'

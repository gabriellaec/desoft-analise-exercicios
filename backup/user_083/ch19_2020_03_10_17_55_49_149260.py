def   classifica_triangulo(x,y,z):
    if x == y and x == z:
        return 'equilátero'
    else:
        if x == y and y != z:
            return 'isósceles'
        else:
            return 'escaleno'

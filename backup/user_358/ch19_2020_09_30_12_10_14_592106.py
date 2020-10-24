def classifica_triangulo(x,y,z):
    if (x)==(y)==(z):
        return('equilátero')
    elif (x)==(y)!=(z) and x!=z:
        return('isósceles')
    else :
        return ('escaleno')
def classifica_triangulo(x, y, z):
    if x==y==z:
        return('equilátero')
    elif x!=y!=z!=x:
        return ('escaleno')
    else:
        return ('isósceles')
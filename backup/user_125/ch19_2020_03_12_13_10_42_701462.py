def classifica_triangulo(x,y,z):
    if x==y!=z or y!=x==z:
        return ('isósceles')
    elif x==y==z:
        return ('equilátero')
    else:
        return ('escaleno')
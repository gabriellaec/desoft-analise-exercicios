def classifica_triangulo(x,y,z):
    if x==y==z:
        return('equilátero')
    if x==y!=z:
        return('isósceles')
    if x!=y!=z:
        return ('escaleno')
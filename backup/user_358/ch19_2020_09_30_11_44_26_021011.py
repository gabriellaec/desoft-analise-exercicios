def classifica_triangulo(x,y,z):
    if x==y==z:
        return('equilátero')
    elif x==y!=z:
        return('isósceles')
    elif x!=y!=z
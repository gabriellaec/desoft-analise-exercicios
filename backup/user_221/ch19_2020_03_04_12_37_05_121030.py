def classifica_triangulo(x,y,z):
    if x==y and x==z:
        return ('equilátero')
    elif x!=y and x!=z and y!=z:
        return('escaleno')
    else:
        return('isósceles')
print(classifica_triangulo(3,4,5))
print(classifica_triangulo(3,3,3))
def classifica_triangulo(x,y,z):
    if x!=y and x!=z and y!=z:
        return 'escaleno'
    if x==y and x==z and y!=z:
        return 'isósceles'
    if x==y and x==z and y==z:
        return 'equilátero'
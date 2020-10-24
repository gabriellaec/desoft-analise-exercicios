def classifica_triangulo(x,y,z):
    if x==z!=y:
        return 'isósceles'
    elif x==y!=z:
        return 'isósceles'
    elif z==y!=x:
        return 'isósceles'
    elif x==y and x==z:
        return 'equilátero'
    elif x!=y!=z:
        return 'escaleno'

   

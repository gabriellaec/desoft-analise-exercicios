def classifica_triangulo(x,y,z):
    if x==y==z:
        return 'equilátero'    
    else:
        if x!=y!=z:
            return 'escaleno'
        else:
            return'isósceles'
print(classifica_triangulo(3,4,5))
def classifica_triangulo(x, y, z):
    if x==y:
        if x==z:
            return 'equilatero'
        if x !=z:
            return 'isósceles'
    if x!=y:
        if x==z:
            return 'isósceles'
        if x!=z:
            return 'escaleno'
    if y==z and y!=x:
        return 'isósceles'
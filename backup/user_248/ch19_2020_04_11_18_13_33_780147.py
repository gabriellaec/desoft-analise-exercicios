def classifica_triangulo(x,y,z):
    if x==y and x==z:
        return"equilátero"
    elif x!=y!=z:
        return"escaleno"
    elif x==y or x==z or y==z:
        return"isósceles"
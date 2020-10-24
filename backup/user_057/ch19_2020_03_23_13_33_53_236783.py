def classifica_triangulo (x,y,z):
    if x==y==z:
        return "equilátero"
    if x==y!=z or x==z!=y or y==z!=x:
        return "isósceles"
    else:
        return "escaleno"


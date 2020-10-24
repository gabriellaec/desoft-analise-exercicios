def classifica_triangulo(x,y,z):
    if x==y and x==z:
        return "equilátero"
    if x==y or y==z and x!=z:
        return "isósceles"
    if x!=z and z!=y:
        return "escaleno"
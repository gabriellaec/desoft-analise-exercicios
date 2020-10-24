def classifica_triangulo(x,y,z):
    if x!=y!=z:
        return "escaleno"
    elif x==z==y:
        return "equilátero"
    elif x!=z==y or x==z!=y or z!=x==y:
        return "isósceles"
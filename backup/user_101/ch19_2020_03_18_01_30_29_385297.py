def classifica_triangulo(x,y,z):
    if x!=y!=z:
        return "escaleno"
    elif x==z==y:
        return "equilátero"
    else:
        return "isósceles"
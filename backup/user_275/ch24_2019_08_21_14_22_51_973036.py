def classifica_triangulo(x,y,z):
    if x==y and x==z:
        return "equilátero"
    elif x!=z and z!=y and y!=x:
        return "escaleno"
    else:
        return"isósceles"
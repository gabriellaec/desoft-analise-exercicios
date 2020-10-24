def classifica_triangulo (x,y,z):
    if x==y and x==z :
        return "equilátero"
    elif x == y or x!=y :
        return "isósceles"
    else:
        return "escaleno"
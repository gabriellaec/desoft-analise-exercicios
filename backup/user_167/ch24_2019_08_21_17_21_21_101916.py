def classifica_triangulo (x,y,z):
    if x==y and x==z :
        return "equilátero"
    elif x != y or x!=y or y!=z :
        return "isósceles"
    else:
        return "escaleno"
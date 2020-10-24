def classifica_triangulo(x,y,z):
    if x==y and x==z:
        return "equilátero"
    else:
        if x==y or y==z and x!=z:
            return "isósceles"
        else:
            if x!=z and z!=y:
                return "escaleno"
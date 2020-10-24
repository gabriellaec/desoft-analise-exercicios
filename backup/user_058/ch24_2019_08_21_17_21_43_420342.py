def classifica_triangulo(x,y,z):
    if (x==z and y==z):
        return "equilátero"
    else:
        if(x==y):
            return "isóseles"
        if(y==z):
            return "isóseles"
        else:
            return "escaleno"
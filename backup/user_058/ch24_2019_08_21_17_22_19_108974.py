def classifica_triangulo(x,y,z):
    if (x==z and y==z):
        return "equilátero"
    else:
        if(x==y):
            return "isóseles"
        elif(y==z):
            return "isóseles"
        else:
            return "escaleno"
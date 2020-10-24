def classifica_triangulo(x,y,z):
    if (x==z and y==z):
        return "equilátero"
    else:
        if(x==y and y!= z):
            return "isóseles"
        elif(y==z and z!=x):
            return "isóseles"
        else:
            return "escaleno"
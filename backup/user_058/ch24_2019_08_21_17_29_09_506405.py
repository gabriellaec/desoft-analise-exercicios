def classifica_triangulo(x,y,z):
    if (x==z and y==z):
        return "equilátero"
    else:
        if(x==y and y!= z):
            return "isósceles"
        elif(y==z and z!=x):
            return "isósceles"
        elif(x==z and x!=y):
            return "isósceles"
        else:
            return "escaleno"
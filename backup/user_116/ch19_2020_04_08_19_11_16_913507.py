def classifica_triangulo(x,y,z):
    if x==y and x==z:
        return ("equilátero")
    elif (x==y and x!=z) or(x==z and x!=y) or(y==z and y!=x):
        return ("isóceles")
    else:
        return ("escaleno")
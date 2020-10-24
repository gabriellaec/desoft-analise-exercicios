def classifica_triangulo(x,y,z):
    if x == y and z == x:
        return ("equilátero")
    elif x!=y and x!=z and y!=z:
        return ("escaleno")
    else:
        return ("isósceles")
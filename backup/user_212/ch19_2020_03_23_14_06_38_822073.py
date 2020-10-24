def classifica_triangulo (x,y,z):
    if x == y and y == z :
        return ("equilátero")
    if (x == y and y != z) or (x == z and z != y) or (y == z and z != x):
        return ("isóceles")
    else:
        return ("escaleno")
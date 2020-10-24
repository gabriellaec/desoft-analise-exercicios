def classifica_triangulo(x,y,z):
    if x == y and x == z:
        return("equilátero")
    
    elif y == z or y == x or x == z :
            return("isósceles")

    else:
        return("escaleno")
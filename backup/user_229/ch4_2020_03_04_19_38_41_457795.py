def classifica_triangulo(x,y,z):
    if x == y:
        if x == y and y == z: 
            return "equilátero"
        else: 
            return "isóceles"
    elif x == z:
        return "isóceles"
    elif y == z:
        return "isóceles"
    else:
        return "escaleno"
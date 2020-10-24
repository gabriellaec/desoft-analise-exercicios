def classifica_triangulo(x,y,z):
    if x == y:
        if y == z and x == z: 
            return "equilátero"
        else: 
            return "isóceles"
    elif x == z:
        return "isóceles"
    elif y == z:
        return "isóceles"
    else:
        return "escaleno"
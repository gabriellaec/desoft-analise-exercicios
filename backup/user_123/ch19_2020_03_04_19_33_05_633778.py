def classifica_triangulo(x, y , z):
    if x == y and y == z and z == x:
        return "equilátero"
    elif x != y and y != z and z != x:
        return "escaleno"
    else:
        return "isóceles"

    
    
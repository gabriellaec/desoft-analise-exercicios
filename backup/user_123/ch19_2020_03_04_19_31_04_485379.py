def classifica_triangulo(x, y , z):
    if x == y and y == z and z == x:
        return "equilátero"
    elif y != x == z:
        return "isóceles"
    elif x != y == z:
        return "isóceles"
    elif z != x != y:
        return "escaleno"

    
    
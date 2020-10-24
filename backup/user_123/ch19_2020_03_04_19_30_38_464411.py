def classifica_triangulo(x, y , z):
    if x == y == z:
        return "equilátero"
    elif y != x == z:
        return "isóceles"
    elif x != y == z:
        return "isóceles"
    elif z != x != y:
        return "escaleno"

    
    
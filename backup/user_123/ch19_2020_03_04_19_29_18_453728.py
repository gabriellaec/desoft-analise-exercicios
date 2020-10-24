def classifica_triangulo(x, y , z):
    if x == y == z:
        return "equilátero"
    if y != x == z:
        return "isóceles"
    if x != y == z:
        return "equilátero"
    if z != x != y:
        return "escaleno"

    
    
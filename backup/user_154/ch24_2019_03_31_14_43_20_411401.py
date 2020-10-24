def classifica_triangulo(a, b, c):
    if b == a or c == a or b == c:
        if b == c and b == a:
            return "equilátero"
        else:
            return "isósceles"
    return "escaleno"
def classifica_triangulo(a, b, c):
    if b == a or c == a:
        if b == c:
            return "equilátero"
        else:
            return "isósceles"
    return "escaleno"
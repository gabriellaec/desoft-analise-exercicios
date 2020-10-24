def classifica_triangulo(a, b, c):
    if a == b or c == b:
        if a == c:
            return "equilátero"
        else:
            return "isósceles"
    return "escaleno"
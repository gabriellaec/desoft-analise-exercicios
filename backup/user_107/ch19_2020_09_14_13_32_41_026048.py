def classifica_triangulo (a, b, c):
    if a == b and b == c:
        return "equilátero"
    elif a == b or a == b or b == c:
        return "isósceles"
    else:
        return "escaleno"
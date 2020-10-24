def classifica_triangulo(a, b, c):
    if a == b and a == c and b == c:
        return "equilátero"
    elif a == b and a == c and b != c:
        return "isósceles"
    else:
        return "escaleno"
    
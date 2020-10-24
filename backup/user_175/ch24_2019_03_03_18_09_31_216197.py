def classifica_triangulo(a, b, c):
    if a == b and b == c:
        return "equilátero"
    elif a == b and b != c:
        return "isósceles"
    elif b == c and c != a:
        return "isósceles"
    else:
        return "escaleno"
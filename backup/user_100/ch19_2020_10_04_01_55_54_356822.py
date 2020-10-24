def classifica_triangulo(a, b, c):
    if a == b and b == c:
        return "equilátero"
    elif a == b and a != c:
        return  "isósceles"
    else:
        return "escaleno"
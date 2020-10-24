def classifica_triangulo (a, b, c):
    if a != b and b != c and c != a:
        return "escaleno"
    elif a == b or b == c or c == a:
        return "isóceles"
    else:
        return "equilátero"
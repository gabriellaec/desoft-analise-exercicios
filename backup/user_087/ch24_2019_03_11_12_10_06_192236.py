def classifica_triangulo(a, b, c):
    if a == b and b == c and c == a:
        return "Equilátero"
    elif a == b and b != c and c != a:
        return "Isósceles"
    else:
        return "Escaleno"
    
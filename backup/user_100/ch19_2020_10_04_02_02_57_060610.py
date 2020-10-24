def classifica_triangulo(a, b, c):
    if a == b and b == c and c == a:
        return "equilátero"
    elif a == b and b != c or a !=b and b == c:
        return  "isósceles"
    elif a != b and b != c:
        return "escaleno"
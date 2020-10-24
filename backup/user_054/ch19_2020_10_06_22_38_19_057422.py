def classifica_triangulo (a, b, c):
    if a == b and a == c and b == c:
        return "equilátero"
    elif a == b or b == c or c == a:
        return "isósceles"
    else:
        return "escaleno"
       
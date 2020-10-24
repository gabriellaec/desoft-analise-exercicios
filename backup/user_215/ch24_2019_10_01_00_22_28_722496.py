def classifica_triangulo(a,b,c):
    if a == b == c:
        return "equilátero"
    elif a == b and a != c or b == c and a != b or a == c and a != b:
        return "isósceles"
    else:
        return "escaleno"
def classifica_triangulo(a,b,c):
    if a == b and b == c:
        return "equilátero"
    else:
        if a == b and b != c:
            return "isósceles"
        else:
            return "escaleno"
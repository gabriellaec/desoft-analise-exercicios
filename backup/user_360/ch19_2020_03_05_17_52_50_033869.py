def classifica_triangulo(a,b,c):
    if a != b != c:
        return("escaleno")
    elif a == b == c:
        return("equilátero")
    else:
        return("isósceles")
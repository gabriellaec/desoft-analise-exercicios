def classifica_triangulo(a, b, c):
    if a == b and b ==c and a == c:
        return("equilátero")
    elif a != b or b != c or a != c:
        return("escaleno")
    else:
        return("isósceles")     

    
def classifica_triangulo(a, b, c):
    if (a == b) and (b == c):
        res = "equilatero"
    elif (a == b) and (b != c):
        res = "isosceles"
    else:
        res = "escaleno"
    return res
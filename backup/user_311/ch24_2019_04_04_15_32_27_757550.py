def classifica_triangulo(a,b,c):
    if a == b == c:
        return "equilátero"
    if a == b or a == c or b == c:
        return "isóceles"
    else:
        return "escaleno"
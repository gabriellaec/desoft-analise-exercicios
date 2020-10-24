def  classifica_triangulo(x, y, w):
    if x == y and x == w:
        return "equilátero"
    elif x == y and x == w and y != w:
        return "isósceles"
    else:
        return "escaleno"
    
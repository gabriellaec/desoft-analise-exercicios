def classifica_triangulo(a, b, c):
    if (float(a)) == (float(b)) and (float(b)) == (float(c)):
        return "equilátero"
    elif (float(a)) == (float(b)) and (float(b)) != (float(c)):
        return "isósceles"
    else:
        return "escaleno"
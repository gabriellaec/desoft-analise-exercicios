def classifica_triangulo(c1,c2,hip):
    if c1 == c2 == hip:
        return('equilátero')
    if c1 != c2 != hip:
        return('escaleno')
    else:
        return('isósceles')
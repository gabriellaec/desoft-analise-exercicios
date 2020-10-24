def classifica_triangulo(c1,c2,hip):
    if c1 == c2 and c1 == hip and c1 == hip:
        return('equilátero')
    if c1 != c2 and c2 != hip and  c1 != hip:
        return('escaleno')
    else:
        return('isósceles')
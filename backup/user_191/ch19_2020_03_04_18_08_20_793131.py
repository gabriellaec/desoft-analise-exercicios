def classifica_triangulo(a,b,c):
    if a==b:
        if b==c:
            return('equilátero')
        else:
            return('isósceles')
    elif b==c:
        return('isósceles')
    else:
        return('escaleno')
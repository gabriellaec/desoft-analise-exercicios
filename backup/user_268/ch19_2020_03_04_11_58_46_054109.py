def classifica_triangulo(a, b, c):
    if a==b and b==c and a==c:
        return (str('esquilátero'))
    elif a==b and or b==c or c==a:
        return (str('isósceles'))
    else:
        return (str('escaleno'))
def classifica_triangulo (a, b, c):
    if a == b == c:
        return 'equilátero'
    elif (a == b and b!= c) or (a != b and b == c) or (a == c and c != b):
        return 'isóceles'
    else:
        return 'escaleno'

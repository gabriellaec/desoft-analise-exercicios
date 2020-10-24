def classifica_triangulo (a, b, c):
    if a == b == c: 
        return 'equilátero'
    elif a == b != c and a == c != b:
        return 'isóceles'
    else:
        return 'escaleno'
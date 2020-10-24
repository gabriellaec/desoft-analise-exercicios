def classifica_triangulo(a, b, c):
    if a == b and a == c :
        return 'equilátero'
    elif a != b and b != c and a != c :
        return 'escaleno'
    else:
        return 'isóceles'
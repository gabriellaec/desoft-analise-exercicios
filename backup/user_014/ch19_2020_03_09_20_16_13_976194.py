def classifica_triangulo (a, b, c):
    if a != b and a != c and c != b:
        return 'escaleno'
    elif a == b == c: 
        return 'equilátero'
    else a == b or a == c or b == c:
        return 'escaleno'
    
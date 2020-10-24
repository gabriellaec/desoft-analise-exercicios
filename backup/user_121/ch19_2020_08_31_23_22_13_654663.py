def classifica_triangulo(a, b, c):
    if a == b == c:
        resultado = 'equilátero'
    else:
        if a != b and a != c and b != c:
            resultado = 'escaleno'
        else:
            resultado = 'isósceles'
    return resultado
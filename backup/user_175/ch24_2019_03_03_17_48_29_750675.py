def classifica_triangulo(l1, l2, l3):
    if l1 == l2 and l2 == l3:
        resultado = 'equilátero'
    elif l1 == l2 and l2 != l3:
        resultado = 'isósceles'
    else:
        resultado = 'escaleno'
    return resultado
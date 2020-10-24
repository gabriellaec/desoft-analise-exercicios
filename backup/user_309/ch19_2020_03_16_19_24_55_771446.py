def classifica_triangulo(l1,l2,l3):
    if l1 != l2 and l2 != l3 and l3 != l1:
        return 'escaleno'
    elif l1 == l2 and l2 == l3 and l3 == l1:
        return 'equilátero'
    else:
        return 'isósceles'
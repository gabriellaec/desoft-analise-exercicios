def classifica_triangulo(l1,l2,l3):
    if l1==l2==l3:
        return'equilatero'
    if l1<l2==l3:
        return 'isoscelis'
    if l1!=l2!=l3:
        return 'escaleno'
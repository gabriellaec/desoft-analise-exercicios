def classifica_triangulo(l1,l2,l3):
    if l1==l2 and l1==l3 and l2==l3:
        return "equilátero"
    elif l1!=l3 and l1!=l2 and l3!=l2:
        return "isóceles"
    else:
        return "escaleno"
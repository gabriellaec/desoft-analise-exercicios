def classifica_triangulo(l1, l2, l3):
    if l1==l2==l3:
        return ('equilátero')
    elif l1!=l2!=l3:
        return ('escaleno')
    elif l1==l2!=l3 or l1!=l2==l3 or l1==l3!=l2:
        return ('isósceles')
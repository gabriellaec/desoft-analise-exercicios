def classifica_triangulo(l1, l2, l3):
    if l1!=l2 and l1!=l3 and l2!=l3:
        print("escaleno")
    elif l1==l2 and l1==l3 and l2==l3:
        print("equilátero")
    else:
        print("isósceles")

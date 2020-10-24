def classifica_triangulo(l1,l2,l3):
    if l1 == l2 == l3:
        print("equilátero")
    if l1 == l2 != l3 or l1 == l3 != l2 or l2 == l3 != l1:
        print("isósceles")
    if l1 != l2 != l3:
        print("escaleno")
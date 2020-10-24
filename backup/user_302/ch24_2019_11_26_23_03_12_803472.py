def classifica_triangulo(l1,l2,l3):
    if l1 == l2 and l2 == l3:
        a = print("equilátero")
    if l1 == l2 or l2 == l3:
        a = print("isóceles")
    else:
        a = print ("escaleno")
    
    return a
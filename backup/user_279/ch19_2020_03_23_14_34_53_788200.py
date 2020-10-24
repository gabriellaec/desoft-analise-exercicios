def classifica_triangulo:
    if l1 == l2 == l3:
        return("equilátero")
    elif l1==l2!=l3 or l1==l3!=l2 or l2==l3!=l1:
        return("isóceles")
    elif l1 != l2 != l3:
        return ("escaleno")
   
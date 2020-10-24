def classifica_trianglo (l1, l2, l3):
    if l1==l2==l3 :
        return ("equilatero")
    elif (l1 == l2 and l1 !=l3) or (l1!=l2 and l2==l3) or (l1==l3 and l2!=l3):
        return ("isosceles")
    elif l1 != l2 and l2 != l3 and l1 != l3:
        return  ("escaleno")

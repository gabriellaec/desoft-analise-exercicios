def classifica_Triangulo (l1,l2,l3):
    if l1 == l2 == l3: 
        return ("equilátero")
    elif l1 != l2 != l3:
        return ("escaleno")
    else l1 == l2 or l2 == l3 or l1 == l3:
        return ("isósceles")
   
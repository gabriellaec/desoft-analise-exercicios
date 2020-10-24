def classifica_triangulo (l1 ,l2, l3):
    if l1 == l2 and l2 == l3:
        print ('equilátero')
    elif l1 ==l2 or l2==l3:
        print ("isósceles")
    else:
        print ("escaleno")
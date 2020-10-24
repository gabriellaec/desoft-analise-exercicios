def calssifica_triangulo(l1 ,l2, l3):
    if l1 == l2 and l2 == l3:
        print ('equilátero')
    if l1 !=l2 and l2!=l3:
        print ('escaleno')
    else:
        print ('isosceles')
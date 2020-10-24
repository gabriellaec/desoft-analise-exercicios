def classifica_triangulo (lado_1, lado_2, lado_3):
    if lado_1 == lado_2 == lado_3:
        print ('equilátero')
    elif lado_1 == lado_2 != lado_3 or lado_1 == lado_3 != lado_2 or lado_2 == lado_3 != lado_1:
        print ('isósceles')
    else:
        print ('escaleno')
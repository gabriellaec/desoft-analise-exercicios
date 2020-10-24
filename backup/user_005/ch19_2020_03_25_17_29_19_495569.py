def classifica_triangulo (lado_1, lado_2, lado_3)
lado_1 = int(input('lado 1:'))
lado_2 = int(input('lado 2:'))
lado_3 = int(input('lado 3:'))
if lado_1 == lado_2 == lado_3:
    print ('equilátero')
elif lado_1 == lado_2 != lado_3 or lado_1 == lado_3 != lado_2 or lado_2 == lado_3 != lado_1:
    print ('isósceles')
else:
    print ('escaleno')
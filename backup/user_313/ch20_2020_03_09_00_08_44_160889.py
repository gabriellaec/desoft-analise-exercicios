a = float(input('Qual distancia voce deseja percorrer: '))

if ( a<=200):
    print('%.2f' % (a*0.50))

if ( a >= 201):
    print('%.2f' % ((a*0.50)+(0.45*(a-200))))
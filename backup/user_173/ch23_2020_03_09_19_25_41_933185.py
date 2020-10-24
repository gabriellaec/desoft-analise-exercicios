velo = int(input('Escreva a sua velocidade:'))
if velo > 80:
    multa = 5*(velo - 80)
    print ('Você foi multado no valor de: {0}'.format(multa))
else:
    print ('Não foi multado')

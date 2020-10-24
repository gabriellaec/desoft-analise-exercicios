velocidade= int(input('Qual a sua velocidade?'))
if velocidade > 80:
    acima= (velocidade - 80)
    multa=acima*5.00
    print('Você foi multado com {}.'.format(multa))
else:
    print('Não foi multado')
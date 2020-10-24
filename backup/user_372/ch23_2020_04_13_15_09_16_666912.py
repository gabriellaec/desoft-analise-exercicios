velocidade=int(input('Qual a velocidade do seu carro? '))
if velocidade>80:
    multa=5*(velocidade-80)
    print('Você recebeu uma multa de R${0:2f}.'.format(multa))
else:
    print('Não foi multado')
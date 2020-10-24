velocidade = int(input('qual sua velo? '))
if velocidade > 80:
    multa = (velocidade - 80)*5
    print('voce foi multado {0:.2f}'.format(multa))
else:
    print('Não foi multado')
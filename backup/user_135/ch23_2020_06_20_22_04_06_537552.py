velocidade = input()

if velocidade > 80:
    multa = (velocidade - 80)*5
    print('R${:.2f}'.format(multa))
else:
    print('Não foi multado')
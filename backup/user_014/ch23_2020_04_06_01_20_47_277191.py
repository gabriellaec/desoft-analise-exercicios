velocidade = int(input('Qual a velocidade do carro? '))
velocidade_maior = velocidade - 80

if velocidade > 80:
    multa = velocidade_maior * 5
    print('Você foi multado e a multa tem valor de R$ {0:.2f}'.format(multa))
else:
    print('Não foi multado')

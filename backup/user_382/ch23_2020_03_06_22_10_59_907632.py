velocidade = float(input('Qual a velocidade do carro?'))

if velocidade >= 80:
    multa = 5*velocidade 
    print('Você foi multado no valor de R${0:.2f}'.format(multa))
else:
    print('Não foi multado')
    
velocidade = int(input('qual a velocidade do seu carro? '))
if velocidade > 80:
    multa = 5*(velocidade - 80)
    float(print('voce foi multado por R${0:.2f}'.format(multa))
else:
    print('Não foi multado')
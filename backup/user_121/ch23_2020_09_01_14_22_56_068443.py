velocidade = int(input('Qual a velocidade do carro em km/h? '))
if velocidade > 80:
    multa = (velocidade - 80) * 5.00
    resultado = print('Você foi multado em R$ {:.2f}'.format(multa))
else:
    resultado = print('Não foi multado')
return resultado
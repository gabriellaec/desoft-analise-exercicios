v= float(input('Qual é a velocidade do carro? '))
if v> 80:
    multa = 5*(v-80)
    print('Você recebeu uma multa de R${0:.2f}'.format(multa))
else:
    print('Não foi multado')
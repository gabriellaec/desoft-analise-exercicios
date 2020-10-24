vel = int(input('Qual a velocidade do carro? '))

if vel<=80:
    print('Não foi multado')
else:
    multa = (vel-80)*5
    print('{:.2f}'.format(multa))
vel = int(input('digite a velocidade do carro: '))
if vel > 80:
    multa = (vel-80)*5
    print('Você foi multado. Sua multa é de R${0:.2f}'.format(multa))
else:
    print('Não foi multado')
    
    
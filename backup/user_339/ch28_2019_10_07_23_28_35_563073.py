v = float(input('Qual a velocidade do carro em km/h?' ))
if v > 80:
	multa = (v - 80) * 5
    print('Você foi multado e será cobrado R${0},00'.format(multa))
else:
	print('Não foi multado')
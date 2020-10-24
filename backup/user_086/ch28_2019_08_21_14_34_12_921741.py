velocidade=float(input('Qual a velocidade do seu carro? '))
if velocidade>80:
	multa=5*(velocidade-80)
	print('Você foi multado em {0:.2f} reais'.format(multa))
else:
	print('Não foi multado')
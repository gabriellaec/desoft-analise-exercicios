v = float(input('Qual a velocidade do carro em km/h?'))

if v > 80:
	x = (v - 80) * 5
    print('Foi multado à {0:.02f} reais'.format(x))
else:
	print('Não foi multado')
v = float(input('Qual a velocidade do carro em km/h?'))

if v > 80:
	x = (v - 80) * 5
    print('Foi multado {0:.02f}'.format(x))
else:
	print('Não foi multado')
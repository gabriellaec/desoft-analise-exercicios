v = float(input('Qual a velocidade do carro em km/h?' ))
if v > 80:
	multa = (v - 80) * 5
    print('Foi multado')
    print(multa)
else:
	print('Não foi multado')
velocidade = int(input('Qual a sua velocidade? '))

if velocidade > 80:
	multa = (velocidade - 80) * 5
	return 'Sua multa foi de {0}'.format(multa)
velo=float(input('Qual a sua velocidade? '))

if velo>80:
	y=(velo-80)*5
	print(('{0:.2f}').format(y))
else:
	print('Não foi multado')
velocidade=float(input('Qual sua velocidade? '))
multa = (velocidade-80)*5
if velocidade >= 80:
	print('Você foi multado')
	print({:.2f}) .format(multa)
else:
    print('Você não foi multado')
def calcula_valor_devido(valor, meses, taxa):
	'''	retorna o valor total devido de um empréstimo a juros composto a uma taxa de juros mensal 		"taxa" (porcentagem), ao longo de "meses" meses, sobre um valor "valor" '''
	
	# cálculo do valor total acumulado
	total = valor * (1 + taxa) ** meses

	# retorno do valor total
	return total
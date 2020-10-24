def calcula_valor_devido(valor, meses, juros):
	total = valor*((1+juros)**meses)
	return total
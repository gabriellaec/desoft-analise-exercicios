def calcula_valor_devido (valor, meses, taxa):
	valor_devido = (valor * ((1 + taxa) ** meses))
	return valor_devido


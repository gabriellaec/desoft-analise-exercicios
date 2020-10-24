def calcula_valor_devido(valor_emprestado, numero_meses, taxa_juros):
	y=valor_emprestado*(1+taxa_juros)**numero_meses
	return y
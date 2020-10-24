def calcula_valor_devido(valor_emprestado, n_meses, taxa_de_juros):
	for i in range(1, n_meses+1):
		valor_emprestado = valor_emprestado * (1+(taxa_de_juros/100))**i
	return valor_emprestado
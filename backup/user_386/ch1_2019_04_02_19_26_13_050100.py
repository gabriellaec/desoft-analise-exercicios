def calcula_valor_devido(valor_emprestado, num_meses, taxa_juros):
	total = valor_emprestado*((1 + taxa_juros)**num_meses)
   	return total
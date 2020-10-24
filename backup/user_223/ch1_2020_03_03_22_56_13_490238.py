def calcula_valor_devido(valor_emprestado, taxa_juros, meses):
	valor_final = valor_emprestado * (taxa_juros**meses)
	return valor_final

calcula_valor_devido(10, 20, 30)

print (calcula_valor_devido)
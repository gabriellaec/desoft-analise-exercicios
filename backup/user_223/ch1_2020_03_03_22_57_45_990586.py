def calcula_valor_devido(valor_emprestado, meses, taxa_juros):
	valor_final = valor_emprestado * ((1 + taxa_juros)**meses)
	return valor_final

print (calcula_valor_devido(10, 20, 30))
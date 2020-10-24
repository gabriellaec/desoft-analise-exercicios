def calcula_valor_devido(valoremprestado, taxadejuros, numerodemeses):
calcula_valor_devido = ( valoremprestado * ( 1 + taxadejuros)**numerodemeses)
	return calcula_valor_devido
print (calcula_valor_devido)
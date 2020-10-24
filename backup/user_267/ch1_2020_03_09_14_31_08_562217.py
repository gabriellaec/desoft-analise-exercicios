def calcula_valor_devido(valoremprestado, numerodemeses,taxadejuros):
	valor_devido = ( valoremprestado * ( 1 + taxadejuros)**numerodemeses)
	return calcula_valor_devido

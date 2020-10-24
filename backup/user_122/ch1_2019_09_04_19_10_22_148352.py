def calcula_valor_devido(entrada, n, taxa):
    	valor_final = entrada*(1 + taxa/100)**n
    	return valor_final
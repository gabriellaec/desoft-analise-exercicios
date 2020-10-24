def calcula_valor_devido(entrada, n, taxa):
    if n %= 0:
    	valor_final = entrada*(1 + taxa/100)**n
    	return valor_final
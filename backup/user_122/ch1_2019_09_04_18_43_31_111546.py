def calcula_valor_devido(entrada, n, taxa):
    if n %= 0:
    	valor_final = entrada*(1 + taxa)**n
    	return valor_final
def calcula_valor_devido(c,t,i):
	m = c * (1+i)**t
    return m
print (calcula_valor_devido(1000,2,5))
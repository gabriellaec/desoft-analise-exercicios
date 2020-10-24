def calcula_valor_devido(c,t,i):
	d = c*(1+i)**t
    return d
print(calcula_valor_devido(1000,2,5))
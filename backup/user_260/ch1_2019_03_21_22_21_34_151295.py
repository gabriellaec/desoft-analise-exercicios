def calcula_valor_devido(c, i, t):
	m= c*((1+i)**t)
    return m
valor_emprestado = 1000
número_de_meses = 2
taxa_de_juros = 10
print (calcula_valor_devido(valor_emprestado, número_de_meses, taxa_de_juros))

def calcula_valor_devido (valor emprestado, número de meses, taxa de juros):
	M= valor emprestado*(1+taxa de juros)**número de meses
    return M
print (calcula_valor_devido (1000, 2, 0.2))
       
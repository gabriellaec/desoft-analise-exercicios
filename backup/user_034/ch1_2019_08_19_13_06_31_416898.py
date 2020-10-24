def calcula_valor_devido(valor_emprestado,meses,juros):
	total=valor_emprestado*(1 + juros)**meses
    return(total)

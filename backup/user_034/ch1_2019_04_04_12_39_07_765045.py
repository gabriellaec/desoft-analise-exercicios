def calcula_valor_devido(emprestado,meses,juros):
	valor_devido=emprestado*(1+juros)**meses
    return valor_devido
    
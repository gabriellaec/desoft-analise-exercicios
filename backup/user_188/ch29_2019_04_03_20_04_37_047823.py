def calcula_aumento(salario):
	if salario <= 1250.00 :
		novo_salario = salario * 0.15
	else:
		novo_salario = salario * 0.10
	return novo_salario
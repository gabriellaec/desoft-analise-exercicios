def calcula_aumento(salario):
	if salario <= 1250.00 :
		novo_salario = salario * 1.15
	else:
		novo_salario = salario * 1.10
	return novo_salario
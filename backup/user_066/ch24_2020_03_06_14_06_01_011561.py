def calcula_aumento(salario):
    if salario > 1250:
        salario_novo = salario*1.1
        aumento = salario_novo-salario
        return aumento
    else:
        salario_novo= salario*1.15
        aumento = salario_novo-salario
    	return aumento
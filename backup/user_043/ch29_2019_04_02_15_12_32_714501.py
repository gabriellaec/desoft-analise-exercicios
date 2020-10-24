def calcula_aumento(salario_atual):
    if salario_atual>1250:
        salario_atual+=salario_atual*0.1
	else:
        salario_atual+=salario_atual*0.15
    return salario_atual
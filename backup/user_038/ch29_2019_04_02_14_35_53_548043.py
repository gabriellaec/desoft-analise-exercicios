def calcula_aumento(salario)
	if salario>1250:
        aumento = salario*0.1
        return(aumento)
    else:
        aumento = salario*0.15
        return(aumento)
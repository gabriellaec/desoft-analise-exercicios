def calcula_aumento(salario):
    if salario > 1250.00:
        return salario + (salario*0.1)
    else:
        return salario + (salario*0.15)
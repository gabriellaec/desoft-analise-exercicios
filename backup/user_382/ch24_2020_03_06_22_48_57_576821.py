def calcula_aumento(salario):
    if salario <= 1250 and salario >= 0:
        salario_novo = salario*0.15
        return salario_novo
    else:
        salario_novo = salario*0.1
        return salario_novo
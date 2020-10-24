def calcula_aumento(salario):
    if salario<=1250:
        salario=salario*1.15
    else:
        salario=salario*1.1
        return salario
    
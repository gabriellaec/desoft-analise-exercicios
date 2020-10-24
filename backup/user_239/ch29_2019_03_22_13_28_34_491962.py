def calcula_aumento(salario):
    if salario>1250:
        y=(salario*1.5)-salario
    else:
        y=(salario*1.1)-salario
    return y
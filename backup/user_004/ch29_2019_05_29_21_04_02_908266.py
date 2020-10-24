def calcula_aumento(salario):
    if salario > 1250.00:
        salariototal=(salario*0.1)+salario
    elif salario <= 1250.00:
        salariototal=(salario*0.15)+salario
    return salariototal
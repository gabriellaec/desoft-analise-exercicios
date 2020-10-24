def calcula_aumento(salario):
    if salario > 1250:
        salarionovo = salario*1.1
    else:
        salarionovo = salario*1.15
    return salarionovo

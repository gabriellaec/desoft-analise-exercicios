def calcula_aumento(salario):
    if salario>1250:
        novo_salario = salario*1.1
    else:
        novo_salario = salario*1.15
    return novo_salario
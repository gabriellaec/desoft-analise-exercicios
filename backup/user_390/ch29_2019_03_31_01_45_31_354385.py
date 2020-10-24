def calcula_aumento(salario):
    if salario>12500:
        salario=salario+(0.1*salario)
    else:
        salario=salario+(0.15*salario)
    return salario

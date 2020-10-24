def calcula_aumento(salario):
    if (salario <= 1250.00):
        new_salario = (salario + 0.15*salario)
    else:
        new_salario = (salario + 0.10*salario)
    return new_salario
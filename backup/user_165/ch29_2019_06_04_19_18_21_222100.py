def calcula_aumento(salario_atual):
    if salario_atual > 1250:
        calcula_a = salario_atual*0.1
    else:
        calcula_a = salario_atual*0.15
    return calcula_a 
def calcula_aumento(salario_atual):
    if salario_atual > 1250:
        salario_novo = salario_atual * 1.1
    else:
        salario_novo = salario_atual * 1.15
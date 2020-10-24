def calcula_aumento(salario):
    float(salario)
    if salario > 1250.00:
        salario_novo = salario * 1.10
        return salario_novo - salario

    elif salario <= 1250.00:
        salario_novo = salario * 1.15
        return salario_novo - salario

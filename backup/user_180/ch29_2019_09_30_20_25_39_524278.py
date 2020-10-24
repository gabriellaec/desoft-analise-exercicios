def calcula_aumento(salario_atual):
    if salario_atual > 1250:
        return salario_atual*0.1
    elif salario_atual <= 1250:
        return salario_atual*0.15
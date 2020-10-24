def calcula_aumento(salario_atual):
    
    if salario_atual > 1250:
        salario_novo = salario_atual * 1.1 - salario_novo
    elif salario_atual <= 1250 and salario_atual > 0:
        salario_novo = salario_atual * 1.15 - salario_novo
    
    return salario_novo
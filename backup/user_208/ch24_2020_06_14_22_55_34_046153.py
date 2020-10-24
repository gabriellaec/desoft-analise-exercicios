def calcula_aumento (salario):
    if salario > 1250:
        x = salario*1.1
        y = x - salario
        return y
    elif salario <= 1250:
        x = salario*1.15
        y = x - salario
        return y


    

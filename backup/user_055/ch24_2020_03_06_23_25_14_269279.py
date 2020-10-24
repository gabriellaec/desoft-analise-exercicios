def calcula_aumento(salario):
    if salario > 1250:
        aumento = salario*0.1
    if salario <= 1250:
        aumento = salario*0.15
    return aumento
    
    
    
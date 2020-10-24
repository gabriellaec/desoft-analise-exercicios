def calcula_aumento(salario):
    if salario> 1250.00:
        aumento= 10/100
    elif salario <= 1250.00:
        aumento= 15/100
    return salario*aumento
def calcula_aumento(salario):
    if salario > 1250:
        valor_aumento = int(salario) * 10/100
        return valor_aumento
    elif salario <= 1250:
        valor_aumento = int(salario) * 15/100
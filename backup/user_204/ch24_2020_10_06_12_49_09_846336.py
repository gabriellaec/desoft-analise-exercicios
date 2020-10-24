def calcula_aumento(salario):
    if salario > 1250:
        final = salario * 1.10
        return final
    elif salario <= 1250:
        final = salario * 1.15
        return final
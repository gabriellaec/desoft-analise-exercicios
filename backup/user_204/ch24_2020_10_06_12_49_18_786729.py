def calcula_aumento(salario):
    if salario > 1250:
        final = salario * 0.10
        return final
    elif salario <= 1250:
        final = salario * 0.15
        return final
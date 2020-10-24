def calcula_aumento(salario):
    if salario > 1250:
        final = salario * 1.1
        return final
    else:
        final = salario * 1.15
        return final
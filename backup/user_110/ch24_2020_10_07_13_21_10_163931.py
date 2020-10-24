def calcula_aumento(salario):
    if salario > 1250:
        aumento = (salario * 0.1) + salario
        return aumento
    else:
        aumento1 = (salario * 0.15) + salario
        return aumento1
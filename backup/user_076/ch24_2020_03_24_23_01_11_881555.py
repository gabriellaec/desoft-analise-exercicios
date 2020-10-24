def calcula_aumento(salario):
    if salario > 1250:
        y = salario * 1.1
        return y
    elif salario <= 1250:
        z = salario * 1.15
        return  z

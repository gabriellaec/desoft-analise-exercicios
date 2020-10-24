def calcula_aumento(salario):
    a = float(salario)
    if a > 1250.00:
        return salario * 1.1
    else:
        return salario * 1.15
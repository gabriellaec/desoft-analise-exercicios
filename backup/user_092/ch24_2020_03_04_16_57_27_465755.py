def calcula_aumento(salario):
    a = float(salario)
    if a > 1250.00:
        return a*1.1
    else:
        return a*1.15
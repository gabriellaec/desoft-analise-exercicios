def calcula_aumento(salario):
    a = float(salario)
    if a > 1250.00:
        b = a*1.1
        return b
    else:
        c = a*1.15
        return c
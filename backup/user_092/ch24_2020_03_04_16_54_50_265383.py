def calcula_aumento(salario):
    a = float(salario)
    if a > 1250.00:
        return salario + salario * 0.1
    else:
        return salario + salario * 0.15
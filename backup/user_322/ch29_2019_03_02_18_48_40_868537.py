def aumento_salario(salario):
    if salario > 1250:
        aumento = salario * (1.10)
        return aumento
    else:
        aumento = salario * (1.15)
        return aumento
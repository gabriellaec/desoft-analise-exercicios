aumentodez = 1.1
aumentoquinze = 1.15
def calcula_aumento(salario):
    if salario > 1250.00:
        return salario*aumentodez
    else:
        return salario*aumentoquinze
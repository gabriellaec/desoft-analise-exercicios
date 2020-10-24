
def calcula_aumento(salario):
    if salario>12500:
        return salario+(0.1*salario)
    if salario<=12500:
        return salario+(0.15*salario)


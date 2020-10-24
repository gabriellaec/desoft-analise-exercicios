salario= 1000
def calcula_aumento(salario):
    if salario>12500:
        return salario+(0.1*salario)
    else:
        return salario+(0.15*salario)
print (calcula_aumento(salario))

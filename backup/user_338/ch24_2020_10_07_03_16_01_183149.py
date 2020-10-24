def calcula_aumento(salario):
    if salario>1250:
        return (salario*1.1)
    else:
        return (salario*1.15)
c=calcula_aumento(1500)
print(c)
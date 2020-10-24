def calcula_aumento(salario):
    if salario>1250:
        valor=salario*0.1
    else:
        valor=salario*0.15
    return valor
print(calcula_aumento(1200))

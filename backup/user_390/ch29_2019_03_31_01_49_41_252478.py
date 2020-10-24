def calcula_aumento(salario):
    if salario<12,500:
        novo=salario+((15/100)*salario)
    else:
        novo=salario+((10/100)*salario)
    return novo

def calcula_aumento(salario):
    if salario>12500:
        novo=salario+(0.1*salario)
    else:
        novo=salario+(0.15*salario)
    return novo

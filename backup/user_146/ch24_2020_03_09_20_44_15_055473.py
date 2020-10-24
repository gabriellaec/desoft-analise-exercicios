def calcula_aumento(grana):
    if grana > 1250:
        novo_salario = grana*(0.1)
        return novo_salario
    elif grana <= 1250:
        novo_salario = grana*(0.15)
        return novo_salario

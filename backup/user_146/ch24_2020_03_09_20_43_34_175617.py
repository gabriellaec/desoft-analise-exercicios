def calcula_aumento(grana):
    if grana > 1250:
        novo_salario = grana*(1.1)
        return novo_salario
    elif grana <= 1250:
        novo_salario = grana*(1.15)
        return novo_salario
print(calcula_aumento(1250))

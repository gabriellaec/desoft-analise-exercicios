def calcula_aumento(salário):
    if salário <= 1250:
        aumento = salário * 0.15
    else:
        aumento = salário * 0.1
    return aumento
def calcula_aumento(salário):
    if salário > 1250:
        aumento = salário * 1.1
    else:
        aumento = salário *1.15
    return aumento
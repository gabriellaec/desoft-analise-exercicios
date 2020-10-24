def calcula_aumento(salário):
    if salário > 1250:
        salário = salário * 1.1
    else:
        salário = salário * 1.15
    return salário
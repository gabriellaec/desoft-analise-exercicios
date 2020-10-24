def calcula_aumento(salário):
    if salário >= 1250.00:
        pc_aumento = 0.10
    else:
        pc_aumento = 0.15
aumento = salário * pc_aumento
    return aumento
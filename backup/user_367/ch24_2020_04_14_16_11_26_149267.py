def calcula_aumento(salário):
    if salário >= 1250.00:
        pc_aumento = salário * 0.10
        return pc_aumento
    else:
        pc_aumento = salário * 0.15
        return pc_aumento

        
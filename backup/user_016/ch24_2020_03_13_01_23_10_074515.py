def calcula_aumento(salário):
    if salário>1250:
        aumento = 0.10*salário
        return aumento
    else:
        aumento = 0.15*salário
        return aumento
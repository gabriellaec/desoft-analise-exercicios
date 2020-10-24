def calcula_aumento(valor):
    if valor > 1250:
        aumento1 = valor * 10/100
        return aumento1
    elif valor<=1250:
        aumento2 = valor *15/100
        return aumento2
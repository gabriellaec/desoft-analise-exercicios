def calcula_aumento(atual):
    if atual > 1250.00:
        aumento1= atual * 0.1
        return aumento1
    elif atual <= 1250.00:
        aumento2= atual * 0.15
        return aumento2

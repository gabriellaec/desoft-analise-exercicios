def calcula_aumento(atual):
    if atual > 1250:
        aumento1= atual * 1.1
        return aumento1
    elif atual <= 1250:
        aumento2= atual * 1.15
        return aumento2
print(calcula_aumento(atual))
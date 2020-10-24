def calcula_aumento (a):
    if a > 1250.00:
        aumento = a * 10/100 + a
    elif a < 1250.00:
        aumento = a * 15/100 + a
    return aumento
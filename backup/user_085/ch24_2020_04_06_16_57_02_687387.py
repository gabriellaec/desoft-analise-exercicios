def calcula_aumento(a):
    if a<=1250:
        return a * 1.15
    else:
        return a * 1.10
print(calcula_aumento(10000))
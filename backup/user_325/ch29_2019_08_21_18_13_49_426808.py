def calcula_aumento(x):
    if x > 1250:
        y = x + (x * 0.1)
        return y
    else:
        y = x + (x * 0.15)
        return y
print(calcula_aumento(10000))
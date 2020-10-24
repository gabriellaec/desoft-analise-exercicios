def calcula_aumento(x):
    if x<=1250:
        z=x*(0.15)
    else:
        z=x*(0.1)
    return z
print(calcula_aumento(1000))
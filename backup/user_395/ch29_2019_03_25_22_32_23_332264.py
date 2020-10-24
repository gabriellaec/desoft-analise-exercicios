def calcula_aumento(x):
if x > 1250:
    return x*0.1
if x <= 1250:
    return x*0.15
print(calcula_aumento(1300))
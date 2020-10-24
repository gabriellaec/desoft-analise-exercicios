def calcula_aumento(x):
    if x>1250:
        return x*0.10
    elif x<=1250:
        return x*0.15
print(calcula_aumento(980))
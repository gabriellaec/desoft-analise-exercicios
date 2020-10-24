def calcula_aumento(a):
    if a > 1250:
        return (a*1.1)
    elif a <= 1250:
        return (a*1.15)
print (calcula_aumento(a))
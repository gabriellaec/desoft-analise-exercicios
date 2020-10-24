def calcula_aumento(x):
    if x > 1250:
        return  x*1.1
    if x <= 1250:
        return x*1.15
a = calcula_aumento(1800)
print (a)
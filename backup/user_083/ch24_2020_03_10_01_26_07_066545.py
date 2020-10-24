def    calcula_aumento(x):
    if x >= 1.250:
        f= x*1.1
        return f
    else:
        g= x*1.15
        return g
print(calcula_aumento(1000))
print(calcula_aumento(2000))
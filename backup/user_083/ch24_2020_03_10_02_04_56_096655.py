def    calcula_aumento(a):
    if a > 1250.00:
        f= a*1.1
        return f
    else:
        if a <= 1250.00:
            g= a*1.15
            return g
print(calcula_aumento(1000))
print(calcula_aumento(2000))

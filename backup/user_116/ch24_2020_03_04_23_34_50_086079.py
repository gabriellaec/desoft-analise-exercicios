def calcula_aumento(sl):
    if (sl) > 1200:
        z=sl*(10/100)
        return(z)
    else:
        y=sl*(15/100)
        return(y)
sl=float(input('digite salario'))
print(calcula_aumento(sl))
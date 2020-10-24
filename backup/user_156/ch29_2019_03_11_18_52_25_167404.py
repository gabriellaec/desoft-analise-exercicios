def calcula_aumento(x):
    if x>1250:
        y=0.1*x
    elif x<=1250 and x>0:
        y=0.15*x
        return y
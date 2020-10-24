def calcula_aumento(x):
    if(x>1250):
        s=x*1.1
    if(x>0 and x<=1250):
        s=x*1.15
    return s
def calcula_aumento(x):
    
    
    if x > 1250:
        x = x + (x*0.1)
    else:
        x = x + (x*0.15)
    return x
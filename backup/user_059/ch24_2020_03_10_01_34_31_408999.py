def calcula_aumento(x):
    if x>1250:
        novo = x+(x*0.10)
        return(novo)
    else: 
        novo = x+(x*0.15)
        return(novo)
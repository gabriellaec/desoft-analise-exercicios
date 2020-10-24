def calcula_aumento(s):
    if s<=1250:
        return s*(1.15)
    elif s>1250:
        return s*(1.1)
    
print (calcula_aumento(1300))
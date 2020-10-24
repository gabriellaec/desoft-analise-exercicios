def calcula_aumento(sal):
    if sal>1250:
        aumento=0.1
    else: 
        aumento=0.15
    
    salM = sal*(1+aumento)
    return salM
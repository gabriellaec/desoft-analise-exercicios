def calcula_aumento(sal):
    if sal>1250:
        sal*=1.1
        aumento=0.1
    else: 
        sal*=1.15
        aumento=0.15
    return aumento
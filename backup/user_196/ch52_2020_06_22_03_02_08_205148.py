def calcula_total_da_nota (preço, quant):
    for i in range(len(preço)):
        pfinal += preço[i]*quant[i]      
    return pfinal

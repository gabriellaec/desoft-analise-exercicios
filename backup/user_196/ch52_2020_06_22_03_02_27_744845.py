def calcula_total_da_nota (preço, quant):
    pfinal = 0
    for i in range(len(preço)):
        pfinal += preço[i]*quant[i]      
    return pfinal

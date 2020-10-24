def calcula_total_da_nota(preço,quant):
    s=0
    i=0
    while i<len(preço):
        t=preço[i]*quant[i]
        s+=t
        i+=1
    return s

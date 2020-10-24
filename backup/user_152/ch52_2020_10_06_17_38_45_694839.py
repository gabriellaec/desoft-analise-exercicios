def calcula_total_da_nota (precos, quant):
    total = []
    soma = 0
    if len(precos) == len(quant):
        if len(precos)>0:
            i = 0
            while i<len(quant):
                total.append(precos[i]*quant[i])
                i += 1
            i = 0
            while i<len(total):
                soma += total[i]
                i += 1
    
    return soma
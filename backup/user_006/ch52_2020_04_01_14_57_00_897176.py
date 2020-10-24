def calcula_total_da_nota(preco, quant):
    total=[]
    i=0
    while i< len(preco):
        total.append(preco[i]*quant[i])
        i=i+1
    return total
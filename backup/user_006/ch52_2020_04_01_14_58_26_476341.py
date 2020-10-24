def calcula_total_da_nota(preco, quant):
    total=0
    i=0
    while i< len(preco):
        total=total+preco[i]*quant[i]
        i=i+1
    return total
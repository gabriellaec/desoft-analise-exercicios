def calcula_total_da_nota(precos,quant):
    total=0
    for i in range(len(precos)):
        total+=precos[i]*quant[i]
    return total
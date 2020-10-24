def calcula_total_da_nota(valor, qtd):
    total=0
    i=0
    while i<len(valor):
        total+=valor[i]*qtd[i]
        i+=1
    return total
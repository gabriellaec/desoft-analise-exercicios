def calcula_total_da_nota(precos,qtd):
    i=0
    total=0
    while i<len(precos):
        total+=precos[i]*qtd[i]
        i+=1
    return total
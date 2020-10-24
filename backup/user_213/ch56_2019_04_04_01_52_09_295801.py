def calcula_total_da_nota(precos,qtd):
    i=0
    total=0
    while i<=len(precos):
        total+=preco[i]*qtd[i]
    return total
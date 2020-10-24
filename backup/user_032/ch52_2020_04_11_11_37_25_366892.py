def calcula_total_da_nota(produtos,quantidade):
    i = 0
    total_nota = 0
    while i < len(produtos):
        total = produtos[i] * quantidade[i]
        total_nota+=total
        i = i + 1
    return total_nota

def calcula_total_da_nota(precos,quantidade):
    total = 0
    for i in range(len(quantidade)):
        total += precos[i]*quantidade[i]
    return total

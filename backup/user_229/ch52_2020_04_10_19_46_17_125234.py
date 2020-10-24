def calcula_total_da_nota(produtos, quantidade):
    total = 0
    for i in range(len(produtos)):
        total += produtos[i]*quantidade[i]
    return total
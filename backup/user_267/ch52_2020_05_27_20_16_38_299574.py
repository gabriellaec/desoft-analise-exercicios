def calcula_total_da_nota(preco, quantidade):
    total = 0
    for i in range(len(preco)):
        total += (preco[i]*quantidade[i])
    return total
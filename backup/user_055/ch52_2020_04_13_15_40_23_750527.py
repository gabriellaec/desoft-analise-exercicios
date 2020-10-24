def calcula_total_da_nota(produtos, quantidade):
    nota_fiscal = []
    for preco in range(len(produtos) - 1):
        nota_fiscal.append(produtos[preco]*quantidade[preco])
    return nota_fiscal
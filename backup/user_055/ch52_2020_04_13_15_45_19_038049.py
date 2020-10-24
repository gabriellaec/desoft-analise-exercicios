def calcula_total_da_nota(produtos, quantidade):
    nota_fiscal = []
    preco = 0
    while preco < len(produtos - 1):
        nota_fiscal.append(produtos[preco]*quantidade[preco])
        preco += 1
    return nota_fiscal
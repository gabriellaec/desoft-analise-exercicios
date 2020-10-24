def calcula_total_da_nota(produtos, quantidade):
    nota_fiscal = []
    preco = 0
    while preco < len(produtos):
        nota_fiscal.append(produtos[preco]*quantidade[preco])
        preco += 1
    return sum(nota_fiscal)
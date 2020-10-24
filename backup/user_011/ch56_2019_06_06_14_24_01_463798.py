def calcula_total_da_nota(quantidade, preco):
    preco_total = 0
    i = 0
    while i < len(preco):
        preco_produto = int(quantidade[i])*int(preco[i])
        preco_total = preco_total + preco_produto
        i += 1
    return preco_total
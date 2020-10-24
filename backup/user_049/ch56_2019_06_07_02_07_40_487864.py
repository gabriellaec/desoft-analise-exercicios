def calcula_total_da_nota(preco, quantidade):
    preco_produto=0
    for i in range(len(preco)):
        preco_produto=preco[i]*quantidade[i]
        preco_total+=preco_produto
    return preco_total
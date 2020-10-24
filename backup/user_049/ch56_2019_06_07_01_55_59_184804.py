def calcula_total_da_nota(preco, quantidade):
    for i range(len(preco)):
        preco_individual=preco[i]*quantidade[i]
        preco_total+=preco_individual
    return preco_total
def calcula_total_da_nota(produto,quantidade):
    i=0
    preco=0
    while i< len(produto):
        preco +=produto[i]*quantidade[i]
        i+=1
    return preco
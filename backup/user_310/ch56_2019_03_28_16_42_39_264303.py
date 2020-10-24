def calcula_total_da_nota(preco, quantidade):
    total=0
    i=0
    
    while i<len(preco):
        produto=preco[i]*quantidade[i]
        total+=produto
    
    return total
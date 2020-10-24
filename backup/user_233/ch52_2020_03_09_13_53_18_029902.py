def calcula_total_da_nota(preco, quantidade):
    
    total = 0
    
    for i in preco:
        total += preco * quantidade[i]
    
    return total
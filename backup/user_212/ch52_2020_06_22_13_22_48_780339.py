def calcula_total_da_nota (preco,quantidades):
    
    total = 0
    i = 0
    
    while i < len(preco):
        preco_prod = preco[i] * quantidades[i]
        total += preco_prod
        
        i +=1
        
    return total

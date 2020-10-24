def calcula_total_da_nota(preco, quantidade):
    i = 0
    total = 0
    
    while i<len(preco):
        t = preco[i]*quantidade[i]
        total = total + t
        i += 1
        
    return total

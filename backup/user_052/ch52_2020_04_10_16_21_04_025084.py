def calcula_total_da_nota (preco, quantidade):
    i = 0
    total = 0
    while i < len(quantidade):
        if quantidade[i] != 0:
            total += quantidade[i]*preco[i]
            i += 1
        else:
            i += 1
            
    
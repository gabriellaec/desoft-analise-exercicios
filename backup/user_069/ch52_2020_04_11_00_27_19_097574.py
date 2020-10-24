def calcula_total_da_nota (preco, quantidade):
    preco_total = []
    len(preco) == len(quantidade)
    i = 0 
    s = 0
    while i < len(quantidade):
        preco_total[i] = preco[i]*quantidade[i]
        s += preco_total[i]
        i += 1
    return s
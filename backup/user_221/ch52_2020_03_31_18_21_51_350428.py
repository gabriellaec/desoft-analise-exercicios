def calcula_total_nota(preco, quantidade):
    i = 0
    preco_total = []
    s = 0
    while i < len(preco):
        preco_total.append(preco[i]*quantidade[i])
        s += preco_total[i]
        i += 1
    return s
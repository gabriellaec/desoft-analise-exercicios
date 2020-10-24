def calcula_total_da_nota(quantidade, preco):
    preco_total = 0
    i = 0
    while i < len(preco):
        preco_total = int(quantidade[i])*int(preco[i])
        i += 1
    return preco_total
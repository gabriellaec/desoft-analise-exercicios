def calcula_total_da_nota(preco, quantidade):
    i = 0
    total = 0
    while i < (len(preco)):
        total += (preco[i]*quantidade[i])
        i += 1
    print(total)